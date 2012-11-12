from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from __future__ import generators
import os, sys, inspect, copy

# ensure pyeq2 can be imported
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



def SetParametersAndFit(inEquation, resultList, inPrintStatus): # utility function
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(inEquation.GetCoefficientDesignators()) > len(inEquation.dataCache.allDataCacheDictionary['DependentData']):
            return

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if inEquation.ShouldDataBeRejected(inEquation):
            return

        if inPrintStatus:
            print('Fitting', inEquation.__module__, "'" + inEquation.GetDisplayName() + "'")
        
        inEquation.Solve()
        
        target = inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)
        if target > 1.0E290: # error too large
            return
    except:
        print("Exception in " + inEquation.__class__.__name__ + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n')
        return

    t0 = copy.deepcopy(inEquation.__module__)
    t1 = copy.deepcopy(inEquation.__class__.__name__)
    t2 = copy.deepcopy(inEquation.extendedVersionHandler.__class__.__name__.split('_')[1])
    t3 = copy.deepcopy(target)
    t4 = copy.deepcopy(inEquation.solvedCoefficients)
    t5 = copy.deepcopy(inEquation.polyfunctional3DFlags)
    t6 = copy.deepcopy(inEquation.xPolynomialOrder)
    t7 = copy.deepcopy(inEquation.yPolynomialOrder)

    resultList.append([t0,t1,t2,t3,t4,t5,t6,t7])




rawData = '''
3.017  2.175   0.320
2.822  2.624   0.629
2.632  2.839   0.950
2.287  3.030   1.574
2.207  3.057   1.725
2.048  3.098   2.035
1.963  3.115   2.204
1.784  3.144   2.570
1.712  3.153   2.721
2.972  2.106   0.313
2.719  2.542   0.643
2.495  2.721   0.956
2.070  2.878   1.597
1.969  2.899   1.758
1.768  2.929   2.088
1.677  2.939   2.240
1.479  2.957   2.583
1.387  2.963   2.744
2.843  1.984   0.315
2.485  2.320   0.639
2.163  2.444   0.954
1.687  2.525   1.459
1.408  2.547   1.775
1.279  2.554   1.927
1.016  2.564   2.243
0.742  2.568   2.581
0.607  2.571   2.753
'''


# this example yields a sorted output list to inspect after completion
resultList = []

# Standard lowest sum-of-squared errors in this example, see IModel.fittingTargetDictionary
fittingTargetText = 'SSQABS'

# we are using the same data set repeatedly, so create a cache external to the equations
externalCache = pyeq2.dataCache()
reducedDataCache = {}


#####################################################
# this value is used to make the example run faster #
#####################################################
smoothnessControl = 3


##########################
# fit named equations here
for submodule in inspect.getmembers(pyeq2.Models_3D):
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

                    SetParametersAndFit(equationInstance, resultList, True)
                    
                    if not reducedDataCache.has_key(equationInstance.numberOfReducedDataPoints):
                        reducedDataCache[equationInstance.numberOfReducedDataPoints] = equationInstance.dataCache.reducedDataCacheDictionary



# Sort the result list by fitting target value
resultList.sort(ResultListSortFunction) # ResultListSortFunction() currently requires the 4th result element to be fitting target
bestResult = resultList[0]


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
polyfunctional3DFlags = bestResult[5]
polynomialOrderX = bestResult[6]
polynomialOrderY = bestResult[7]


# now instantiate the "best fit" equation based on the name stored in the result list
if polyfunctional3DFlags:
    equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polyfunctional3DFlags) + ")")
elif polynomialOrderX != None:
    equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polynomialOrderX) + ", " + str(polynomialOrderY) + ")")
else:
    equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "')")


pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equation, False)
equation.fittingTarget = fittingTargetText
equation.solvedCoefficients = solvedCoefficients
equation.dataCache.FindOrCreateAllDataCache(equation)
equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)


print()
print('\"Best fit\" was', moduleName + "." + className)

print('Fitting target value', equation.fittingTarget + ":", equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))

if polyfunctional3DFlags:
    print()
    print('Polyfunctional flags:', polyfunctional3DFlags)
    print()
if polynomialOrderX != None:
    print()
    print('Polynomial order:', polynomialOrderX)
    print()

for i in range(len(equation.solvedCoefficients)):
    print("Coefficient " + equation.GetCoefficientDesignators()[i] + ": " + str(equation.solvedCoefficients[i]))
print()
for i in range(len(equation.dataCache.allDataCacheDictionary['DependentData'])):
    print('X:', equation.dataCache.allDataCacheDictionary['IndependentData'][0][i],)
    print('Y:', equation.dataCache.allDataCacheDictionary['IndependentData'][1][i],)
    print('Z', equation.dataCache.allDataCacheDictionary['DependentData'][i],)
    print('Model:', equation.modelPredictions[i],)
    print('Abs. Error:', equation.modelAbsoluteError[i],)
    if not equation.dataCache.DependentDataContainsZeroFlag:
        print('Rel. Error:', equation.modelRelativeError[i],)
        print('Percent Error:', equation.modelPercentError[i])
    else:
        print()
