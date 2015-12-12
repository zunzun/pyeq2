from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, inspect

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
importDir =  os.path.join(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'), '..')
if importDir not in sys.path:
    sys.path.append(importDir)
    
import pyeq2



# see IModel.fittingTargetDictionary
equation = pyeq2.Models_2D.Polynomial.Quadratic() # SSQABS by default

data = equation.exampleData
pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
equation.Solve()


##########################################################


print(pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeCSHARP(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeVBA(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodePYTHON(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVA(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeSCILAB(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeMATLAB(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeJULIA(equation))
print(pyeq2.outputSourceCodeService().GetOutputSourceCodeFORTRAN90(equation))
