import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2


if __name__ == "__main__":

    # see IModel.fittingTargetDictionary
    equation = pyeq2.Models_3D.BioScience.HighLowAffinityIsotopeDisplacement('SSQABS')
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
    
    
    # Note that all coefficients are set with estimated values
    equation.estimatedCoefficients = [2.0, 3.0E13]
    
    
    equation.Solve()
    
    
    ##########################################################
    
    
    print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print "Fitted Parameters:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
