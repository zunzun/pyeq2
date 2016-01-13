from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, inspect

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2


# parameters are smoothing, xOrder, yOrder
equation = pyeq2.Models_3D.Spline.Spline(1.0, 3, 3) # cubic 3D spline

data = equation.exampleData

pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
equation.Solve()


##########################################################


print("Equation:", equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print("Fitting target of", equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))

print()

# at present, onlythese four languages are supported
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodePYTHON(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVA(equation))
#print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(equation))
