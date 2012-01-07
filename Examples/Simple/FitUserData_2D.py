#    Version info: $Id$

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



if __name__ == "__main__":

    # see IModel.fittingTargetDictionary
    equation = pyeq2.Models_2D.BioScience.HyperbolicLogistic('SSQABS')
    
    data = '''
      X        Y
    5.357    10.376
    5.457    10.489
    5.797    10.874
    5.936    11.049
    6.161    11.327
    6.697    12.054
    6.731    12.077
    6.775    12.138
    8.442    14.744
    9.769    17.068
    9.861    17.104
    '''
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
    equation.Solve()
    
    
    ##########################################################
    
    
    print equation.GetDisplayName(), str(equation.GetDimensionality()) + "D"
    print equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    print "Fitted Parameters:"
    for i in range(len(equation.solvedCoefficients)):
        print "    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i])
