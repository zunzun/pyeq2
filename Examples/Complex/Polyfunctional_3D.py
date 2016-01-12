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



def UniqueCombinations(items, n): # utility function
    if n==0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in UniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc



def SetParametersAndFit(inEquation, resultList): # utility function
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(inEquation.GetCoefficientDesignators()) > len(inEquation.dataCache.allDataCacheDictionary['DependentData']):
            return

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if inEquation.ShouldDataBeRejected(inEquation):
            return

        inEquation.Solve()
        
        target = inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)
        if target > 1.0E290: # error too large
            return
    except:
        print("Exception in " + inEquation.__class__.__name__ + '\n' + str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1]) + '\n')
        return

    t0 = copy.copy(inEquation.__module__)
    t1 = copy.copy(inEquation.__class__.__name__)
    t2 = copy.copy(inEquation.extendedVersionHandler.__class__.__name__.split('_')[1])
    t3 = copy.copy(target)
    t4 = copy.copy(inEquation.solvedCoefficients)
    t5 = copy.copy(inEquation.polyfunctional3DFlags)
    t6 = copy.copy(inEquation.xPolynomialOrder)
    t7 = copy.copy(inEquation.yPolynomialOrder)

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

fittingTargetText = 'SSQABS' # required for high-speed linear solver

# we are using the same data set repeatedly, so create a cache external to the equations
externalDataCache = pyeq2.dataCache()


equation = pyeq2.Models_3D.Polyfunctional.UserSelectablePolyfunctional(fittingTargetText)
equation.dataCache = externalDataCache
pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equation, False)

functionList = []
for k in range(len(equation.polyfunctionalEquationList_X)):
    for l in range(len(equation.polyfunctionalEquationList_Y)):
        if [l,k] not in functionList:
            functionList.append([k,l])

# WARNING: increasing this value creates huge numbers
# of combinations and causes very large memory use. If
# you change this, count the total number of generated
# equations before actually performing any fitting
maxCombinationCount = 2

combinationGenerator = UniqueCombinations(functionList, maxCombinationCount)

fitCount = 0
print('Fitting polyfunctionals')
for k in combinationGenerator:
    equation.__init__(fittingTargetText)
    equation.polyfunctional3DFlags = k
    equation.dataCache = externalDataCache        

    # for display only
    fitCount += 1
    if fitCount % 250 == 0:
        print('Fitted ' + str(fitCount))

    SetParametersAndFit(equation, resultList)


# Sort the result list by fitting target value
resultList.sort(key=lambda item: item[3]) # currently requires the 4th result element to be fitting target


print()
print()
print('While \"Best Fit\" may be the lowest fitting target value,')
print('it requires further evaluation to determine if it is the best')
print('for your needs.  For example, it may interpolate badly.')
print()

# in this example, only the top-sorted result list item is used
bestResult = resultList[0]

moduleName = bestResult[0]
className = bestResult[1]
extendedVersionHandlerName = bestResult[2]
fittingTarget = bestResult[3]
solvedCoefficients = bestResult[4]
polyfunctional3DFlags = bestResult[5]


# now instantiate the "best fit" equation based on the name stored in the result list
equation = eval(moduleName + "." + className + "('" + fittingTargetText + "', '" + extendedVersionHandlerName + "', " + str(polyfunctional3DFlags) + ")")

pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equation, False)
equation.fittingTarget = fittingTargetText
equation.solvedCoefficients = solvedCoefficients
equation.dataCache.FindOrCreateAllDataCache(equation)
equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)


print()
print('\"Best fit\" was', moduleName + "." + className)

print('Fitting target value', equation.fittingTarget + ":", equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))

print()
print('Polyfunctional flags:', polyfunctional3DFlags)
print()
for i in range(len(equation.solvedCoefficients)):
    print("Coefficient " + equation.GetCoefficientDesignators()[i] + ": " + str(equation.solvedCoefficients[i]))
print()

##########################################################

print('Generated source code section commented out')
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeCSHARP(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeVBA(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodePYTHON(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVA(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeSCILAB(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeMATLAB(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJULIA(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeFORTRAN90(equation))
