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


equation = pyeq2.Models_2D.Polynomial.Linear()

pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)

##########################################################

# first solve with no bounds
equation.Solve()

print("Fitted Parameters With No Bounds:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print()

##########################################################

# now with an upper bound
equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded

equation.Solve()

print("Fitted Parameters With One Upper Bound:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
()

##########################################################

# now with a lower bound
equation.upperCoefficientBounds = [] # reset to have no upper bounds
equation.lowerCoefficientBounds = [-8.0, None] # None means the parameter is unbounded

equation.Solve()

print("Fitted Parameters With One Lower Bound:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print()

##########################################################

# now with an upper bound and a fixed coefficient
# note that fixed coefficients override bounds
equation.fixedCoefficients = [-8.5, None] # None means the parameter is not fixed
equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded
equation.lowerCoefficientBounds = [] # reset to have no lower bounds

equation.Solve()

print("Fitted Parameters With One Upper Bound And One Fixed Coefficient (fixed coeffs override bounds):")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
