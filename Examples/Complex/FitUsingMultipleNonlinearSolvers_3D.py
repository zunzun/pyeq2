#    Version info: $Id$

import os, sys, inspect

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2



if __name__ == "__main__":
    
    fittingTarget = 'SSQABS'
    rawData = '''
0.01 25 0.8857
0.01 50 0.8408
0.01 75 0.8082
0.01 100 0.7959
0.01 200 0.7224
0.01 300 0.7020
0.01 450 0.6612
0.01 600 0.6286
0.02 25 0.7755
0.02 50 0.7184
0.02 75 0.6857
0.02 100 0.6612
0.02 200 0.5551
0.02 300 0.5061
0.02 450 0.4531
0.02 600 0.4041
0.05 25 0.5469
0.05 50 0.4653
0.05 75 0.3959
0.05 100 0.3551
0.05 200 0.2653
0.05 300 0.1959
0.05 450 0.1347
0.05 600 0.1102
0.10 25 0.3306
0.10 50 0.2122
0.10 75 0.1673
0.10 100 0.1306
0.10 200 0.0694
0.10 300 0.0408
0.10 450 0.0286
0.10 600 0.0163
0.15 25 0.1878
0.15 50 0.1061
0.15 75 0.0694
0.15 100 0.0449
0.15 200 0.0204
0.15 300 0.0041
0.15 450 0.0041
0.15 600 0.0041
0.20 25 0.1102
0.20 50 0.0449
0.20 75 0.0408
0.20 100 0.0245
0.20 200 0.0041
0.20 300 0.0041
0.20 450 0.0
0.20 600 0.0
0.25 25 0.0694
0.25 50 0.0327
0.25 75 0.0163
0.25 100 0.0041
0.25 200 0.0041
0.25 300 0.0
0.25 450 0.0
0.25 600 0.0
    '''

    for submodule in inspect.getmembers(pyeq2.Models_3D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    
                    try:
                        if equationClass[1]._canLinearSolverBeUsedForSSQABS == True and fittingTarget == 'SSQABS': # nonlinear solvers only
                            continue
                    except:
                        continue
                        
                    differentAlgorithmResults = None
                    for fittingAlgorithmName in pyeq2.solverService.ListOfNonLinearSolverAlgorithmNames:
                        try:
                            equation = equationClass[1](fittingTarget)
                            data = equation.exampleData
                            pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
                            
                            equation.Solve(inNonLinearSolverAlgorithmName=fittingAlgorithmName)
                            
                            fittingTargetResult = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
                            
                            if differentAlgorithmResults is None:
                                differentAlgorithmResults = [fittingTargetResult, submodule[0], equationClass[0], fittingAlgorithmName]
                            elif fittingTarget < differentAlgorithmResults[0]:
                                differentAlgorithmResults = [fittingTargetResult, submodule[0], equationClass[0], fittingAlgorithmName]
                        except:
                            pass

                    if differentAlgorithmResults is not None:
                        print 'Best algorithm for', differentAlgorithmResults[1], differentAlgorithmResults[2], 'was', differentAlgorithmResults[3], 'at', differentAlgorithmResults[0]
                        sys.stdout.flush()
