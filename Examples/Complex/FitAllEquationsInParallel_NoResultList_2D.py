#    Version info: $Id$

from __future__ import generators
import os, sys, inspect, copy, multiprocessing

if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



def ResultListSortFunction(a, b): # utility function
    if a[3] < b[3]:
        return -1
    if a[3] > b[3]:
        return 1
    return 0

def UniqueCombinations(items, n): # utility function
    if n==0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in UniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def UniqueCombinations2(items2, n2): # utility function
    if n2==0:
        yield []
    else:
        for i2 in xrange(len(items2)):
            for cc2 in UniqueCombinations2(items2[i2+1:],n2-1):
                yield [items2[i2]]+cc2



def SetParametersAndFit(inEquation, inBestResult, inPrintStatus, processIdentifier = 0): # utility function=
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(inEquation.GetCoefficientDesignators()) > len(inEquation.dataCache.allDataCacheDictionary['DependentData']):
            return

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if inEquation.ShouldDataBeRejected(inEquation):
            return

        if inPrintStatus:
            print 'Process ID', processIdentifier, 'Fitting', inEquation.__module__, "'" + inEquation.GetDisplayName() + "'"
        
        inEquation.Solve()
        
        target = inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)
        if target > 1.0E290: # error too large
            return
    except:
        print 'Process ID', processIdentifier, "Exception in " + inEquation.__class__.__name__ + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n'
        return None

    if (not inBestResult) or (target < inBestResult[3]):
        t0 = copy.deepcopy(inEquation.__module__)
        t1 = copy.deepcopy(inEquation.__class__.__name__)
        t2 = copy.deepcopy(inEquation.extendedVersionHandler.__class__.__name__.split('_')[1])
        t3 = copy.deepcopy(target)
        t4 = copy.deepcopy(inEquation.solvedCoefficients)
        t5 = copy.deepcopy(inEquation.polyfunctional2DFlags)
        t6 = copy.deepcopy(inEquation.xPolynomialOrder)
        t7 = copy.deepcopy(inEquation.rationalNumeratorFlags)
        t8 = copy.deepcopy(inEquation.rationalDenominatorFlags)
    
        return [t0,t1,t2,t3,t4,t5,t6,t7,t8]



def ParallelFittingFunction(rawData, fittingTargetText, smoothnessControl, modulus, modulusRemainder):
    processID = str(os.getpid())
    
    # this function yields a single item to inspect after completion
    bestResult = []
    
    # we are using the same data set repeatedly, so create a cache external to the equations
    externalCache = pyeq2.dataCache()
    reducedDataCache = {}
    
    equationCountForModulus = 0

    

    ##########################
    # add named equations here
    print
    print 'Process ID', processID, 'fitting named equations:'
    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    
                    # special classes
                    if equationClass[1].splineFlag or \
                       equationClass[1].userSelectablePolynomialFlag or \
                       equationClass[1].userSelectablePolyfunctionalFlag or \
                       equationClass[1].userSelectableRationalFlag or \
                       equationClass[1].userDefinedFunctionFlag:
                        continue
                    
                    for extendedVersion in ['Default', 'Offset']:
                        
                        if (extendedVersion == 'Offset') and (equationClass[1].autoGenerateOffsetForm == False):
                            continue                        
                        
                        if equationCountForModulus % modulus != modulusRemainder:
                            equationCountForModulus += 1
                            continue
                        equationCountForModulus += 1
                        
                        equationInstance = equationClass[1](fittingTargetText, extendedVersion)
    
                        if len(equationInstance.GetCoefficientDesignators()) > smoothnessControl:
                            continue
                            
                            
                        equationInstance.dataCache = externalCache # re-use the external cache
                        
                        if equationInstance.dataCache.allDataCacheDictionary == {}:
                            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
                            
                        equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
                        if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
                        else:
                            equationInstance.dataCache.reducedDataCacheDictionary = {}
    
                        result = SetParametersAndFit(equationInstance, bestResult, True, processID)
                        if result:
                            bestResult = result
                        
                        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
    
    
    
    ##########################
    # fit polyfunctionals here
    print
    print 'Process ID', processID, 'fitting polyfunctionals:'
    equationCount = 0
    maxPolyfunctionalCoefficients = 4 # this value was chosen to make this example more convenient
    polyfunctionalEquationList = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_2D()
    functionIndexList = range(len(polyfunctionalEquationList)) # make a list of function indices to permute
    
    for coeffCount in range(1, maxPolyfunctionalCoefficients+1):
        functionCombinations = UniqueCombinations(functionIndexList, coeffCount)
        for functionCombination in functionCombinations:
            
            if len(functionCombination) > smoothnessControl:
                continue
    
            if equationCountForModulus % modulus != modulusRemainder:
                equationCountForModulus += 1
                continue
            equationCountForModulus += 1

            equationInstance = pyeq2.Models_2D.Polyfunctional.UserSelectablePolyfunctional(fittingTargetText, 'Default', functionCombination, polyfunctionalEquationList)
                
            equationInstance.dataCache = externalCache # re-use the external cache
            
            if equationInstance.dataCache.allDataCacheDictionary == {}:
                pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
                
            equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
            if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
            else:
                equationInstance.dataCache.reducedDataCacheDictionary = {}
    
            result = SetParametersAndFit(equationInstance, bestResult, False)
            if result:
                bestResult = result
    
            if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
            
            equationCount += 1
            if (equationCount % 50) == 0:
                print '    Process ID', processID, 'fitted',  equationCount, 'equations...'

    
    
    ######################
    # fit user-selectable polynomials here
    print
    print 'Process ID', processID, 'fitting user-selectable polynomials:'
    maxPolynomialOrderX = 5 # this value was chosen to make this example more convenient
    
    for polynomialOrderX in range(maxPolynomialOrderX+1):

        if (polynomialOrderX + 1) > smoothnessControl:
            continue
        
        if equationCountForModulus % modulus != modulusRemainder:
            equationCountForModulus += 1
            continue
        equationCountForModulus += 1
        
        equationInstance = pyeq2.Models_2D.Polynomial.UserSelectablePolynomial(fittingTargetText, 'Default', polynomialOrderX)    
        
        equationInstance.dataCache = externalCache # re-use the external cache

        if equationInstance.dataCache.allDataCacheDictionary == {}:
            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
            
        equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
        if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
            equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
        else:
            equationInstance.dataCache.reducedDataCacheDictionary = {}
    
        result = SetParametersAndFit(equationInstance, bestResult, False)
        if result:
            bestResult = result
    
        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
    
    
    
    ######################
    # fit user-selectable rationals here
    print
    print 'Process ID', processID, 'fitting user-selectable rationals:'
    equationCount = 0
    maxCoeffs = smoothnessControl # arbitrary choice of maximum total coefficients for this example
    functionList = pyeq2.PolyFunctions.GenerateListForRationals_2D()
    functionIndexList = range(len(functionList)) # make a list of function indices
    
    for numeratorCoeffCount in range(1, maxCoeffs):
        numeratorComboList = UniqueCombinations(functionIndexList, numeratorCoeffCount)
        for numeratorCombo in numeratorComboList:
            for denominatorCoeffCount in range(1, maxCoeffs):
                denominatorComboList = UniqueCombinations2(functionIndexList, denominatorCoeffCount)
                for denominatorCombo in denominatorComboList:
                    
                    for extendedVersion in ['Default', 'Offset']:
                    
                        extraCoeffs = 0
                        if extendedVersion == 'Offset':
                            extraCoeffs = 1
                            
                        if (len(numeratorCombo) + len(denominatorCombo) + extraCoeffs) > smoothnessControl:
                            continue
                        
                        if equationCountForModulus % modulus != modulusRemainder:
                            equationCountForModulus += 1
                            continue
                        equationCountForModulus += 1
                        
                        equationInstance = pyeq2.Models_2D.Rational.UserSelectableRational(fittingTargetText, extendedVersion, numeratorCombo, denominatorCombo, functionList)
        
                        equationInstance.dataCache = externalCache # re-use the external cache
                        
                        if equationInstance.dataCache.allDataCacheDictionary == {}:
                            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
                            
                        equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
                        if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
                        else:
                            equationInstance.dataCache.reducedDataCacheDictionary = {}
        
                        result = SetParametersAndFit(equationInstance, bestResult, False)
                        if result:
                            bestResult = result
                        
                        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
        
                        equationCount += 1
                        if (equationCount % 5) == 0:
                            print '    ', 'Process ID', processID + ',', equationCount, 'rationals, current flags:', equationInstance.rationalNumeratorFlags, equationInstance.rationalDenominatorFlags,
                            if extendedVersion == 'Offset':
                                print 'with offset'
                            else:
                                print

    
    print 'Process ID', processID, 'has completed'
    return bestResult
    
    

if __name__ == "__main__":

    rawData = '''
    5.357    0.376
    5.457    0.489
    5.797    0.874
    5.936    1.049
    6.161    1.327
    6.697    2.054
    6.731    2.077
    6.775    2.138
    8.442    4.744
    9.769    7.068
    9.861    7.104
    '''
    
    # Standard lowest sum-of-squared errors in this example, see IModel.fittingTargetDictionary
    fittingTargetText = 'SSQABS'
        
    
    #####################################################
    # this value is used to make the example run faster #
    #####################################################
    smoothnessControl = 3
    
    
    
    ##############################################
    # Parallel region begins
    ##############################################
    
    poolItems = []

    # how many CPU cores are on this computer?
    number_of_cpu_cores = multiprocessing.cpu_count()

    # create a process pool using all CPU cores (in this example)
    pool = multiprocessing.Pool(processes=number_of_cpu_cores)
    
    # run items in parallel, see ParallelFittingFunction() above
    for i in range(number_of_cpu_cores):
        poolItems.append(pool.apply_async(ParallelFittingFunction, (rawData, fittingTargetText, smoothnessControl, number_of_cpu_cores, i))) # modulus math divides the equations among the processes
        
    # gather all results from the process pool
    allResults = []
    for i in range(number_of_cpu_cores):
        allResults.append(poolItems[i].get())
        
    # no more items will be added to the process pool
    pool.terminate()
    pool.join()

    ##############################################
    # Parallel region ends
    ##############################################
    
    
        
    # find the best result of all the parallel runs
    bestResult = []
    for result in allResults:
        if (not bestResult) or (result[3] < bestResult[3]):
            bestResult = result
    
    

    print
    print
    print 'While \"Best Fit\" may be the lowest fitting target value,'
    print 'it requires further evaluation to determine if it is the best'
    print 'for your needs.  For example, it may interpolate badly.'
    print
    print '"Smoothness Control" allowed a maximum of ' + str(smoothnessControl) + ' parameters'
    
    moduleName = bestResult[0]
    className = bestResult[1]
    extendedVersionHandlerName = bestResult[2]
    fittingTarget = bestResult[3]
    solvedCoefficients = bestResult[4]
    polyfunctional2DFlags = bestResult[5]
    polynomialOrderX = bestResult[6]
    rationalNumeratorFlags = bestResult[7]
    rationalDenominatorFlags = bestResult[8]
    
    
    # now instantiate the "best fit" equation based on the name stored in the result list
    if polyfunctional2DFlags:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polyfunctional2DFlags) + ")")
    elif polynomialOrderX != None:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polynomialOrderX) + ", " + str(polynomialOrderY) + ")")
    elif rationalNumeratorFlags and rationalDenominatorFlags:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(rationalNumeratorFlags) + ", " + str(rationalDenominatorFlags) + ")")
    else:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "')")
    
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equation, False)
    equation.fittingTarget = fittingTargetText
    equation.solvedCoefficients = solvedCoefficients
    equation.dataCache.FindOrCreateAllDataCache(equation)
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    
    
    print
    print '\"Best fit\" was', moduleName + "." + className
    
    print 'Fitting target value', equation.fittingTarget + ":", equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    
    if polyfunctional2DFlags:
        print
        print 'Polyfunctional flags:', polyfunctional2DFlags
        print
    if polynomialOrderX != None:
        print
        print 'Polynomial order:', polynomialOrderX
        print
    if rationalNumeratorFlags and rationalDenominatorFlags:
        print
        print 'Rational numerator flags:', rationalNumeratorFlags
        print 'Rational denominator flags:', rationalDenominatorFlags
        if extendedVersionHandlerName == 'Offset':
            print 'with offset'
        print
    
    for i in range(len(equation.solvedCoefficients)):
        print "Coefficient " + equation.GetCoefficientDesignators()[i] + ": " + str(equation.solvedCoefficients[i])
    print
    for i in range(len(equation.dataCache.allDataCacheDictionary['DependentData'])):
        print 'X:', equation.dataCache.allDataCacheDictionary['IndependentData'][0][i],
        print 'Y', equation.dataCache.allDataCacheDictionary['DependentData'][i],
        print 'Model:', equation.modelPredictions[i],
        print 'Abs. Error:', equation.modelAbsoluteError[i],
        if not equation.dataCache.DependentDataContainsZeroFlag:
            print 'Rel. Error:', equation.modelRelativeError[i],
            print 'Percent Error:', equation.modelPercentError[i]
        else:
            print
