from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from __future__ import generators
import os, sys, inspect, copy

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



def SetParametersAndFit(inEquation, inBestResult, inPrintStatus, inFittingAlgorithmName): # utility function
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(inEquation.GetCoefficientDesignators()) > len(inEquation.dataCache.allDataCacheDictionary['DependentData']):
            return None

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if inEquation.ShouldDataBeRejected(inEquation):
            return None

        if inPrintStatus and inFittingAlgorithmName == 'Levenberg-Marquardt':
            print('Fitting', inEquation.__module__, "'" + inEquation.GetDisplayName() + "'")
        
        inEquation.Solve(inNonLinearSolverAlgorithmName=inFittingAlgorithmName)
        
        target = inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)
        if target > 1.0E290: # error too large
            return None
    except:
        print("Exception in " + inEquation.__class__.__name__ + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n')
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
        t9 = inFittingAlgorithmName
    
        return [t0,t1,t2,t3,t4,t5,t6,t7,t8, t9]
    return None




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

# this example yields a single item to inspect after completion
bestResult = []

# Standard lowest sum-of-squared errors in this example, see IModel.fittingTargetDictionary
fittingTargetText = 'SSQABS'

if fittingTargetText == 'ODR':
    raise Exception('ODR cannot use multiple fitting algorithms')

# we are using the same data set repeatedly, so create a cache external to the equations
externalCache = pyeq2.dataCache()
reducedDataCache = {}


#####################################################
# this value is used to make the example run faster #
#####################################################
smoothnessControl = 3



##########################
# fit named equations here
print()
print('Fitting named equations that use non-linear solvers for a fitting target of', fittingTargetText)
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
                    
                    deEstimatedCoefficients = []
                    for fittingAlgorithmName in pyeq2.solverService.ListOfNonLinearSolverAlgorithmNames:
                        equationInstance = equationClass[1](fittingTargetText, extendedVersion)
                        
                        # reject equations that use linear solvers for this fitting target
                        if equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                            continue
    
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

                        equationInstance.deEstimatedCoefficients = deEstimatedCoefficients

                        result = SetParametersAndFit(equationInstance, bestResult, True, fittingAlgorithmName)
                        
                        deEstimatedCoefficients = equationInstance.deEstimatedCoefficients # no need to re-run DE

                        if result:
                            bestResult = result
                            if bestResult[9] != 'Levenberg-Marquardt':
                                print('The', bestResult[9], 'algorithm yielded better results than Levenberg-Marquardt on this data set for a fitting target of', fittingTargetText)
                                print()
                    
                        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary



##########################
# fit polyfunctionals here
print()
print('Fitting polyfunctionals that use non-linear solvers for a fitting target of', fittingTargetText)
equationCount = 0
maxPolyfunctionalCoefficients = 4 # this value was chosen to make this example more convenient
polyfunctionalEquationList = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_2D()
functionIndexList = range(len(polyfunctionalEquationList)) # make a list of function indices to permute

for coeffCount in range(1, maxPolyfunctionalCoefficients+1):
    functionCombinations = UniqueCombinations(functionIndexList, coeffCount)
    for functionCombination in functionCombinations:
        
        if len(functionCombination) > smoothnessControl:
            continue
            
        deEstimatedCoefficients = []
        for fittingAlgorithmName in pyeq2.solverService.ListOfNonLinearSolverAlgorithmNames:
            equationInstance = pyeq2.Models_2D.Polyfunctional.UserSelectablePolyfunctional(fittingTargetText, 'Default', functionCombination, polyfunctionalEquationList)
    
            # reject equations that use linear solvers for this fitting target
            if equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                continue

            equationInstance.dataCache = externalCache # re-use the external cache
            
            if equationInstance.dataCache.allDataCacheDictionary == {}:
                pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
                
            equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
            if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
            else:
                equationInstance.dataCache.reducedDataCacheDictionary = {}
    
            equationInstance.deEstimatedCoefficients = deEstimatedCoefficients
            
            result = SetParametersAndFit(equationInstance, bestResult, False, fittingAlgorithmName)
            
            deEstimatedCoefficients = equationInstance.deEstimatedCoefficients # no need to re-run DE
            
            if result:
                bestResult = result
                if bestResult[9] != 'Levenberg-Marquardt':
                    print('The', bestResult[9], 'algorithm yielded better results than Levenberg-Marquardt on this data set for a fitting target of', fittingTargetText)
                    print()

            if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
        
        equationCount += 1
        if (equationCount % 250) == 0:
            print('    ', equationCount, '...')



######################
# fit user-selectable polynomials here
print()
print('Fitting user-selectable polynomials that use non-linear solvers for a fitting target of', fittingTargetText)
maxPolynomialOrderX = 5 # this value was chosen to make this example more convenient

for polynomialOrderX in range(maxPolynomialOrderX+1):
    
    if (polynomialOrderX + 1) > smoothnessControl:
        continue

    deEstimatedCoefficients = []
    for fittingAlgorithmName in pyeq2.solverService.ListOfNonLinearSolverAlgorithmNames:
        equationInstance = pyeq2.Models_2D.Polynomial.UserSelectablePolynomial(fittingTargetText, 'Default', polynomialOrderX)
                
        # reject equations that use linear solvers for this fitting target
        if equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
            continue

        equationInstance.dataCache = externalCache # re-use the external cache
    
        if equationInstance.dataCache.allDataCacheDictionary == {}:
            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
            
        equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
        if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
            equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
        else:
            equationInstance.dataCache.reducedDataCacheDictionary = {}
    
        equationInstance.deEstimatedCoefficients = deEstimatedCoefficients
        
        result = SetParametersAndFit(equationInstance, bestResult, False, fittingAlgorithmName)
        
        deEstimatedCoefficients = equationInstance.deEstimatedCoefficients # no need to re-run DE

        if result:
            bestResult = result
            if bestResult[9] != 'Levenberg-Marquardt':
                print('The', bestResult[9], 'algorithm yielded better results than Levenberg-Marquardt on this data set for a fitting target of', fittingTargetText)
                print()

        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary



######################
# fit user-selectable rationals here
print()
print('Fitting user-selectable rationals that use non-linear solvers for a fitting target of', fittingTargetText)
equationCount = 0
maxCoeffs = 3 # arbitrary choice of maximum total coefficients for this example
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
                    
                    deEstimatedCoefficients = []
                    for fittingAlgorithmName in pyeq2.solverService.ListOfNonLinearSolverAlgorithmNames:
                        equationInstance = pyeq2.Models_2D.Rational.UserSelectableRational(fittingTargetText, extendedVersion, numeratorCombo, denominatorCombo, functionList)
                        
                        # reject equations that use linear solvers for this fitting target
                        if equationInstance.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
                            continue
                                        
                        equationInstance.dataCache = externalCache # re-use the external cache
                        
                        if equationInstance.dataCache.allDataCacheDictionary == {}:
                            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equationInstance, False)
                            
                        equationInstance.dataCache.CalculateNumberOfReducedDataPoints(equationInstance)
                        if reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            equationInstance.dataCache.reducedDataCacheDictionary = reducedDataCache[equationInstance.numberOfReducedDataPoints]
                        else:
                            equationInstance.dataCache.reducedDataCacheDictionary = {}
        
                        equationInstance.deEstimatedCoefficients = deEstimatedCoefficients
                        
                        result = SetParametersAndFit(equationInstance, bestResult, False, fittingAlgorithmName)

                        deEstimatedCoefficients = equationInstance.deEstimatedCoefficients # no need to re-run DE

                        if result:
                            bestResult = result
                            if bestResult[9] != 'Levenberg-Marquardt':
                                print('The', bestResult[9], 'algorithm yielded better results than Levenberg-Marquardt on this data set for a fitting target of', fittingTargetText)
                                print()
                    
                        if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                            reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary
    
                    equationCount += 1
                    if (equationCount % 5) == 0:
                        print('    ', equationCount, 'rationals, current flags:', equationInstance.rationalNumeratorFlags, equationInstance.rationalDenominatorFlags,)
                        if extendedVersion == 'Offset':
                            print('with offset')
                        else:
                            print()

