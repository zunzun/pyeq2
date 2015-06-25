from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, inspect, dispy

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2



# Standard lowest sum-of-squared errors in this example, see IModel.fittingTargetDictionary
fittingTargetString = 'SSQABS'

#####################################################
# this value is used to make the example run faster, you
# will very likely want equations with more than 2 coefficients
#####################################################
smoothnessControl = 2

textData = '''
    X      Y       Z
  3.017  2.175   0.0320
  2.822  2.624   0.0629
  1.784  3.144   6.570
  1.712  3.153   6.721
  2.972  2.106   0.0313
  2.719  2.542   0.0643
  2.0 2.6 4.0  ending text is ignored
  1.479  2.957   6.583
  1.387  2.963   6.744
  2.843  1.984   0.0315
  2.485  2.320   0.0639
  0.742  2.568   6.581
  0.607  2.571   6.753
'''



# this is the function to be run on the cluster
def SetParametersAndFit(equationString, inFittingTargetString, inExtendedVersionString, inTextData):
    
    # individual cluster nodes must be able to import pyeq2
    import pyeq2

    exec('equation = ' + equationString +'("' + inFittingTargetString + '", "' + inExtendedVersionString + '")')
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(inTextData, equation, False)
 
    try:
        # check for number of coefficients > number of data points to be fitted
        if len(equation.GetCoefficientDesignators()) > len(equation.dataCache.allDataCacheDictionary['DependentData']):
            return None

        # check for functions requiring non-zero nor non-negative data such as 1/x, etc.
        if equation.ShouldDataBeRejected(equation):
            return None

        equation.Solve()

        fittedTarget = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
        if fittedTarget > 1.0E290: # error too large
            return None
    except:
        return None

    return [fittedTarget, equation.GetDisplayName(), equation.solvedCoefficients, equationString, inExtendedVersionString]



print()
print('Creating dispy JobCluster')
cluster = dispy.JobCluster(SetParametersAndFit)

jobs = []

# this example has named equations only, for simplicity it has no polyrationals or polyfunctions
for submodule in inspect.getmembers(pyeq2.Models_3D):
    if inspect.ismodule(submodule[1]):
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                
                # ignore these special classes for simplicity
                if equationClass[1].splineFlag or \
                   equationClass[1].userSelectablePolynomialFlag or \
                   equationClass[1].userCustomizablePolynomialFlag or \
                   equationClass[1].userSelectablePolyfunctionalFlag or \
                   equationClass[1].userSelectableRationalFlag or \
                   equationClass[1].userDefinedFunctionFlag:
                    continue
                
                for extendedVersionString in ['Default', 'Offset']:
                    
                    if (extendedVersionString == 'Offset') and (equationClass[1].autoGenerateOffsetForm == False):
                        continue
                    
                    equationInstance = equationClass[1](fittingTargetString, extendedVersionString)

                    if len(equationInstance.GetCoefficientDesignators()) > smoothnessControl:
                        continue
                    
                    equationString = equationInstance.__module__ + "." + equationInstance.__class__.__name__
                    
                    job = cluster.submit(equationString, fittingTargetString, extendedVersionString, textData)
                    jobs.append(job)



print('Waiting on jobs to complete  and collecting results')
allResultList = []
for job in jobs:
    results = job()
    if job.exception: # can also use job.status
        print('Remote Exception in one of the jobs\n', str(job.exception))
    else:
        if results:
            print("Remotely fitted", results[1])
            allResultList.append(results)


print()
print('Done. Fitted named equations only.')
print()


allResultList.sort()
topResult = allResultList[0]

fittedTargetValue = topResult[0]
equationDisplayName = topResult[1]
equationSolvedCoefficients = topResult[2]
equationString = topResult[3]
extendedVersionString = topResult[4]

exec('equation = ' + equationString +'("' + fittingTargetString + '", "' + extendedVersionString + '")')

print('Lowest fitting target result was ' + fittingTargetString + " of " + str(fittedTargetValue))
print('for the equation "' + equationDisplayName + '"')
