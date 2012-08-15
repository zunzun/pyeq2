import os, sys, inspect, time

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



if __name__ == "__main__":

    # see IModel.fittingTargetDictionary
    equation = pyeq2.Models_3D.BioScience.ChenClayton('SSQABS')
    
    data = equation.exampleData
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
    equation.Solve()
    
    
    ##########################################################
    
    
    print "Equation:", equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
    print "Fitting target of", equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print "Fitted Parameters:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
