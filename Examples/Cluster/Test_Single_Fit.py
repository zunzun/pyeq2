from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, dispy

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
importDir =  os.path.join(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'), '..')
if importDir not in sys.path:
    sys.path.append(importDir)
    
import pyeq2



# this is the function to be run on the cluster
def fitEquationUsingDispyCluster(inEquationString, inFittingTargetString, inTextData):
	
    # individual cluster nodes must be able to import pyeq2
    import pyeq2

    exec('equation = ' + inEquationString +'("' + inFittingTargetString + '")')
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(inTextData, equation, False)
    equation.Solve()
    fittedTarget = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
   
    # this result list allows easy sorting of multiple results later
    return [fittedTarget, inEquationString, equation.solvedCoefficients]


equationString = 'pyeq2.Models_2D.Polynomial.Linear'

# see the pyeq2.IModel.fittingTargetDictionary
fittingTargetString = 'SSQABS'

textData = '''
1.0   1.1
2.0   2.2
3.0   3.4159
'''

print()
print('Creating dispy JobCluster')
cluster = dispy.JobCluster(fitEquationUsingDispyCluster)

print('Submitting job to the cluster')
job = cluster.submit(equationString, fittingTargetString, textData)

print('Waiting on job completion  and collecting results')
results = job()

print()
if job.exception: # can also use job.status
    print('Remote Exception in job!')
    print()
    print(str(job.exception))
else:
    equationString = 'equation = ' + results[1] + '("' + fittingTargetString + '")'
    exec(equationString)
    equation.solvedCoefficients = results[2]
    print('Success! Results from job:')
    print('The equation ' + results[1])
    print('yielded ' + fittingTargetString + ' of ' + str(results[0]))
    print('with coefficients  ' + str(results[2]))
