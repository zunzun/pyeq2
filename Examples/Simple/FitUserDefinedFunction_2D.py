#    Version info: $Id$

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



if __name__ == "__main__":

    functionString = 'm*X+B'

    # note that the constructor is passed the function string here
    equation = pyeq2.Models_2D.UserDefinedFunction.UserDefinedFunction(inUserFunctionString = functionString)
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)

    equation.Solve()
    
    
    ##########################################################
    
    
    print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
    print 'User Defined Function:', functionString
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print "Fitted Parameters:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
