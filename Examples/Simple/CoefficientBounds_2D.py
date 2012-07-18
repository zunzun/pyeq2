#    Version info: $Id$

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2


if __name__ == "__main__":

    equation = pyeq2.Models_2D.Polynomial.Linear()
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)

    ##########################################################
    
    # first solve with no bounds
    equation.Solve()
    
    print "Fitted Parameters With No Bounds:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print

    ##########################################################

    # now with an upper bound
    equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded
    
    equation.Solve()
    
    print "Fitted Parameters With One Upper Bound:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print
    
    ##########################################################

    # now with a lower bound
    equation.upperCoefficientBounds = [] # reset to have no upper bounds
    equation.lowerCoefficientBounds = [-8.0, None] # None means the parameter is unbounded
    
    equation.Solve()
    
    print "Fitted Parameters With One Lower Bound:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print
    
    ##########################################################

    # now with an upper bound and a fixed coefficient
    # note that fixed coefficients override bounds
    equation.fixedCoefficients = [-8.5, None] # None means the parameter is not fixed
    equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded
    equation.lowerCoefficientBounds = [] # reset to have no lower bounds
    
    equation.Solve()
    
    print "Fitted Parameters With One Upper Bound And One Fixed Coefficient (fixed coeffs override bounds):"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
