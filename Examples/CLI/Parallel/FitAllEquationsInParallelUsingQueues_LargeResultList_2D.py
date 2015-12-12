from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from __future__ import generators
import os, sys, inspect, copy, multiprocessing, Queue

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
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



def SetParametersAndFit(inEquation, inPrintStatus): # utility function
    global globalDataCache
    global globalReducedDataCache
    global globalRawData

    inEquation.dataCache = globalDataCache
    if inEquation.dataCache.allDataCacheDictionary == {}:
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(globalRawData, inEquation, False)
        
    inEquation.dataCache.CalculateNumberOfReducedDataPoints(inEquation)
    if globalReducedDataCache.has_key(inEquation.numberOfReducedDataPoints):
        inEquation.dataCache.reducedDataCacheDictionary = globalReducedDataCache[inEquation.numberOfReducedDataPoints]
    else:
        inEquation.dataCache.reducedDataCacheDictionary = {}
 
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(inEquation.GetCoefficientDesignators()) > len(inEquation.dataCache.allDataCacheDictionary['DependentData']):
            return None

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if inEquation.ShouldDataBeRejected(inEquation):
            return None

        if inPrintStatus:
            print('Process ID', str(os.getpid()), 'Fitting', inEquation.__module__, "'" + inEquation.GetDisplayName() + "'")
        
        inEquation.Solve()

        if not globalReducedDataCache.has_key(inEquation.numberOfReducedDataPoints):
            globalReducedDataCache[inEquation.numberOfReducedDataPoints] = inEquation.dataCache.reducedDataCacheDictionary
        
        target = inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)
        if target > 1.0E290: # error too large
            return None
    except:
        print("Exception in " + inEquation.__class__.__name__ + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n')
        return None

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



def SubmitTasksToQueue(inTaskQueue, fittingTargetText, smoothnessControl, inLinearTrueOrNonLinearFalseFlag):
    totalNumberOfTasksSubmitted = 0
    
    ##########################
    # add named equations here
    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    
                    # special classes
                    if equationClass[1].splineFlag or \
                       equationClass[1].userSelectablePolynomialFlag or \
                       equationClass[1].userCustomizablePolynomialFlag or \
                       equationClass[1].userSelectablePolyfunctionalFlag or \
                       equationClass[1].userSelectableRationalFlag or \
                       equationClass[1].userDefinedFunctionFlag:
                        continue
                    
                    for extendedVersion in ['Default', 'Offset']:
                        
                        if (extendedVersion == 'Offset') and (equationClass[1].autoGenerateOffsetForm == False):
                            continue                        
                        
                        equationInstance = equationClass[1](fittingTargetText, extendedVersion)
    
                        if len(equationInstance.GetCoefficientDesignators()) > smoothnessControl:
                            continue
                        
                        if inLinearTrueOrNonLinearFalseFlag == True and (equationInstance.CanLinearSolverBeUsedForSSQABS() == False or fittingTargetText != 'SSQABS'):
                            continue
                        
                        if inLinearTrueOrNonLinearFalseFlag == False and equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                            continue

                        inTaskQueue.put((SetParametersAndFit,(equationInstance, False)))
                        totalNumberOfTasksSubmitted += 1
    
    
    ##########################
    # fit polyfunctionals here
    maxPolyfunctionalCoefficients = smoothnessControl # arbitrary choice of maximum total coefficients for this example
    polyfunctionalEquationList = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_2D()
    functionIndexList = range(len(polyfunctionalEquationList)) # make a list of function indices to permute
    
    for coeffCount in range(1, maxPolyfunctionalCoefficients+1):
        functionCombinations = UniqueCombinations(functionIndexList, coeffCount)
        for functionCombination in functionCombinations:
            
            if len(functionCombination) > smoothnessControl:
                continue
    
            equationInstance = pyeq2.Models_2D.Polyfunctional.UserSelectablePolyfunctional(fittingTargetText, 'Default', functionCombination, polyfunctionalEquationList)

            if inLinearTrueOrNonLinearFalseFlag == True and (equationInstance.CanLinearSolverBeUsedForSSQABS() == False or fittingTargetText != 'SSQABS'):
                continue
            
            if inLinearTrueOrNonLinearFalseFlag == False and equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                continue

            inTaskQueue.put((SetParametersAndFit,(equationInstance, False)))
            totalNumberOfTasksSubmitted += 1

    
    ######################
    # fit user-selectable polynomials here
    maxPolynomialOrderX = smoothnessControl # arbitrary choice of maximum total coefficients for this example
    
    for polynomialOrderX in range(maxPolynomialOrderX+1):

        if (polynomialOrderX + 1) > smoothnessControl:
            continue
                
        equationInstance = pyeq2.Models_2D.Polynomial.UserSelectablePolynomial(fittingTargetText, 'Default', polynomialOrderX)    
        
        if inLinearTrueOrNonLinearFalseFlag == True and (equationInstance.CanLinearSolverBeUsedForSSQABS() == False or fittingTargetText != 'SSQABS'):
            continue
        
        if inLinearTrueOrNonLinearFalseFlag == False and equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
            continue

        inTaskQueue.put((SetParametersAndFit,(equationInstance, False)))
        totalNumberOfTasksSubmitted += 1
    
    
    ######################
    # fit user-selectable rationals here
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
                                                
                        equationInstance = pyeq2.Models_2D.Rational.UserSelectableRational(fittingTargetText, extendedVersion, numeratorCombo, denominatorCombo, functionList)
                        
                        if inLinearTrueOrNonLinearFalseFlag == True and (equationInstance.CanLinearSolverBeUsedForSSQABS() == False or fittingTargetText != 'SSQABS'):
                            continue
                        
                        if inLinearTrueOrNonLinearFalseFlag == False and equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                            continue

                        inTaskQueue.put((SetParametersAndFit,(equationInstance, False)))
                        totalNumberOfTasksSubmitted += 1
    
    return totalNumberOfTasksSubmitted


def parallelWorker(inputQueue, outputQueue):
    for func, args in iter(inputQueue.get, 'STOP'): # iter() has different behaviors depending on number of parameters
        outputQueue.put(func(*args))
        

def serialWorker(inputQueue, outputQueue):
    for func, args in iter(inputQueue.get, 'STOP'): # iter() has different behaviors depending on number of parameters
        outputQueue.put(func(*args))
        inputQueue.task_done()
        if inputQueue.unfinished_tasks == 0:
            break




os.nice(10) ####################### I use this during development

global globalDataCache 
globalDataCache = pyeq2.dataCache()

global globalReducedDataCache
globalReducedDataCache = {}

global globalRawData
globalRawData = '''
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


##################################################
# this list will hold the results of all fitting #
##################################################
allResults = []



##############################################
# Serial region begins
##############################################

# linear fits are very fast - run these in the existing process which saves on interprocess communication overhead
fittingTasksQueue = Queue.Queue(0)
fittingResultsQueue = Queue.Queue(0)
numberOfSerialTasksSubmitted = SubmitTasksToQueue(fittingTasksQueue, fittingTargetText, smoothnessControl, True)
if numberOfSerialTasksSubmitted > 0:
    serialWorker(fittingTasksQueue, fittingResultsQueue)
    for i in range(numberOfSerialTasksSubmitted):
        allResults.append(fittingResultsQueue.get())

print(str(numberOfSerialTasksSubmitted), 'total linear fits performed in series')

##############################################
# Serial region ends
##############################################


# http://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing
if __name__ ==  '__main__':

    ##############################################
    # Parallel region begins
    ##############################################
    
    fittingTasksQueue = multiprocessing.Queue()
    fittingResultsQueue = multiprocessing.Queue()
    
    # how many CPU cores are on this computer?
    number_of_cpu_cores = multiprocessing.cpu_count()
    
    # submit nonlinear fitting tasks to the queue for parallel processing
    numberOfParallelTasksSubmitted = SubmitTasksToQueue(fittingTasksQueue, fittingTargetText, smoothnessControl, False)
    
    if numberOfParallelTasksSubmitted > 0:
        processList = []
        
        # run worker processes
        try:
            for i in range(number_of_cpu_cores):
                p = multiprocessing.Process(target=parallelWorker, args=(fittingTasksQueue, fittingResultsQueue))
                p.start()
                processList.append(p)
        
            # gather all results from the process pool
            for i in range(numberOfParallelTasksSubmitted):
                allResults.append(fittingResultsQueue.get())
                if i%10 == 0 and i > 0:
                    print(i, 'non-linear fits performed in parallel')
                
        # terminate all worker processes
        finally:
            for p in processList:
                try: # use try/except block for termination
                    p.terminate()
                except:
                    pass
    
    print(str(numberOfParallelTasksSubmitted), 'total non-linear fits performed in parallel')
    
    ##############################################
    # Parallel region ends
    ##############################################
    
    
    
    print('Completed fitting', str(numberOfSerialTasksSubmitted + numberOfParallelTasksSubmitted), 'equations.')
    
    # find the best result of all the parallel runs
    bestResult = []
    for result in allResults:
        if result != None:
            if (not bestResult) or (result[3] < bestResult[3]):
                bestResult = result
    
    print()
    print()
    print('While \"Best Fit\" may be the lowest fitting target value,')
    print('it requires further evaluation to determine if it is the best')
    print('for your needs.  For example, it may interpolate badly.')
    print()
    print('"Smoothness Control" allowed a maximum of ' + str(smoothnessControl) + ' parameters')
    
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
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polynomialOrderX) + ")")
    elif rationalNumeratorFlags and rationalDenominatorFlags:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(rationalNumeratorFlags) + ", " + str(rationalDenominatorFlags) + ")")
    else:
        equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "')")
    
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(globalRawData, equation, False)
    equation.fittingTarget = fittingTargetText
    equation.solvedCoefficients = solvedCoefficients
    equation.dataCache.FindOrCreateAllDataCache(equation)
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    
    
    print()
    print('\"Best fit\" was', moduleName + "." + className)
    
    print('Fitting target value', equation.fittingTarget + ":", equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
    
    if polyfunctional2DFlags:
        print()
        print('Polyfunctional flags:', polyfunctional2DFlags)
        print()
    if polynomialOrderX != None:
        print()
        print('Polynomial order:', polynomialOrderX)
        print()
    if rationalNumeratorFlags and rationalDenominatorFlags:
        ()
        print('Rational numerator flags:', rationalNumeratorFlags)
        print('Rational denominator flags:', rationalDenominatorFlags)
        if extendedVersionHandlerName == 'Offset':
            print('with offset')
        print()
    
    for i in range(len(equation.solvedCoefficients)):
        print("Coefficient " + equation.GetCoefficientDesignators()[i] + ": " + str(equation.solvedCoefficients[i]))
    print()
    for i in range(len(equation.dataCache.allDataCacheDictionary['DependentData'])):
        print('X:', equation.dataCache.allDataCacheDictionary['IndependentData'][0][i],)
        print('Y', equation.dataCache.allDataCacheDictionary['DependentData'][i],)
        print('Model:', equation.modelPredictions[i],)
        print('Abs. Error:', equation.modelAbsoluteError[i],)
        if not equation.dataCache.DependentDataContainsZeroFlag:
            print('Rel. Error:', equation.modelRelativeError[i],)
            print('Percent Error:', equation.modelPercentError[i],)
        print()
