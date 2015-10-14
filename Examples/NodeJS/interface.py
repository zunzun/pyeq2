import os, sys, json

# we want *exceptions* but not *warnings* from the optimizers
# to be propagated back to javascript.  Ignore only optimizer warnings
import warnings
from scipy.optimize import OptimizeWarning
warnings.simplefilter("ignore", OptimizeWarning)


# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2


pythonFileName = sys.argv[0] # unused
equationInfoFromNodeJS = json.loads(sys.argv[1])
textDataFromNodeJS = json.loads(sys.argv[2])
fittingTargetFromNodeJS = json.loads(sys.argv[3])

moduleName = equationInfoFromNodeJS['pythonModuleName']
className = equationInfoFromNodeJS['pythonClassName']
extendedVersionString = equationInfoFromNodeJS['extendedVersionString']
dimensionality = equationInfoFromNodeJS['dimensionality']

eqStringToEvaluate = 'equation = pyeq2.Models_'
eqStringToEvaluate += str(dimensionality) + 'D.'
eqStringToEvaluate += moduleName + '.'
eqStringToEvaluate += className + '('
eqStringToEvaluate += '"' + fittingTargetFromNodeJS + '",'
eqStringToEvaluate += '"' + extendedVersionString + '")'

exec(eqStringToEvaluate)

pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(textDataFromNodeJS, equation, False)

equation.Solve()

# output could include data statistics, error statistics, fit
# and coefficients statistics, etc. from the other Python examples
print json.dumps(equation.solvedCoefficients.tolist())
print(json.dumps(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(equation)))
