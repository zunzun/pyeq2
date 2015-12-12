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


# see IModel.fittingTargetDictionary
equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')

data = '''
  X        Y      Weight
5.357    10.376     0.1
5.457    10.489     0.5
5.797    10.874     5.0
5.936    11.049     9.9
6.161    11.327     0.1
6.697    12.054     0.1
6.731    12.077     0.1
6.775    12.138     0.1
8.442    14.744     0.1
9.769    17.068     0.1
9.861    17.104     0.1
'''

# Note the True flag here, reads in weights
pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, True)
equation.Solve()


##########################################################


print("Equation:", equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print("Fitting target of", equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print("Fitted Parameters:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))


equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
print()
for i in range(len(equation.dataCache.allDataCacheDictionary['DependentData'])):
    print('X:', equation.dataCache.allDataCacheDictionary['IndependentData'][0][i],)
    print('Y:', equation.dataCache.allDataCacheDictionary['DependentData'][i],)
    print('Model:', equation.modelPredictions[i],)
    print('Abs. Error:', equation.modelAbsoluteError[i],)
    if not equation.dataCache.DependentDataContainsZeroFlag:
        print('Rel. Error:', equation.modelRelativeError[i],)
        print('Percent Error:', equation.modelPercentError[i])
    else:
        print()
print()


##########################################################


equation.CalculateCoefficientAndFitStatistics()

if equation.upperCoefficientBounds or equation.lowerCoefficientBounds:
    print('You entered coefficient bounds. Parameter statistics may')
    print('not be valid for parameter values at or near the bounds.')
    print()

print('Degress of freedom error',  equation.df_e_weighted)
print('Degress of freedom regression',  equation.df_r_weighted)

if equation.rmse_weighted == None:
    print('Root Mean Squared Error (RMSE) (weighted): n/a')
else:
    print('Root Mean Squared Error (RMSE) (weighted):',  equation.rmse_weighted)

if equation.r2_weighted == None:
    print('R-squared (weighted): n/a')
else:
    print('R-squared (weighted):',  equation.r2_weighted)

if equation.r2adj_weighted == None:
    print('R-squared adjusted (weighted): n/a')
else:
    print('R-squared adjusted (weighted):',  equation.r2adj_weighted)

if equation.Fstat_weighted == None:
    print('Model F-statistic (weighted): n/a')
else:
    print('Model F-statistic (weighted):',  equation.Fstat_weighted)

if equation.Fpv_weighted == None:
    print('Model F-statistic p-value (weighted): n/a')
else:
    print('Model F-statistic p-value (weighted):',  equation.Fpv_weighted)

if equation.ll_weighted == None:
    print('Model log-likelihood (weighted): n/a')
else:
    print('Model log-likelihood (weighted):',  equation.ll_weighted)

if equation.aic_weighted == None:
    print('Model AIC (weighted): n/a')
else:
    print('Model AIC (weighted):',  equation.aic_weighted)

if equation.bic_weighted == None:
    print('Model BIC (weighted): n/a')
else:
    print('Model BIC (weighted):',  equation.bic_weighted)


print()
print("Individual Parameter Statistics:")
for i in range(len(equation.solvedCoefficients)):
    if equation.tstat_beta_weighted == None:
        tstat = 'n/a'
    else:
        tstat = '%-.5E' %  ( equation.tstat_beta_weighted[i])

    if equation.pstat_beta_weighted == None:
        pstat = 'n/a'
    else:
        pstat = '%-.5E' %  ( equation.pstat_beta_weighted[i])

    if equation.sd_beta_weighted != None:
        print("Coefficient %s = %-.16E, std error (weighted): %-.5E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i], equation.sd_beta_weighted[i]))
    else:
        print("Coefficient %s = %-.16E, std error (weighted): n/a" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
    print("          t-stat (weighted): %s, p-stat (weighted): %s, 95 percent confidence intervals (weighted): [%-.5E, %-.5E]" % (tstat,  pstat, equation.ci_weighted[i][0], equation.ci_weighted[i][1]))


print()
print("Coefficient Covariance Matrix (weighted):")
for i in  equation.cov_beta_weighted:
    print(i)
