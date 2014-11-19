import os, sys

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)

import pyeq2


def SaveCoefficientAndFitStatistics(in_filePathFitStatistics, in_equation):
    
    outputFile = open(in_filePathFitStatistics, 'w')
    
    if in_equation.upperCoefficientBounds or in_equation.lowerCoefficientBounds:
        outputFile.write('This model has coefficient bounds. Parameter statistics may\n')
        outputFile.write('not be valid for parameter values at or near the bounds.\n')
        outputFile.write('\n')
    
    outputFile.write('Degress of freedom error ' + str(in_equation.df_e) + '\n')
    outputFile.write('Degress of freedom regression ' + str(in_equation.df_r) + '\n')
    
    if in_equation.rmse == None:
        outputFile.write('Root Mean Squared Error (RMSE): n/a\n')
    else:
        outputFile.write('Root Mean Squared Error (RMSE): ' + str(in_equation.rmse) + '\n')
    
    if in_equation.r2 == None:
        outputFile.write('R-squared: n/a\n')
    else:
        outputFile.write('R-squared: ' + str(in_equation.r2) + '\n')
    
    if in_equation.r2adj == None:
        outputFile.write('R-squared adjusted: n/a\n')
    else:
        outputFile.write('R-squared adjusted: ' + str(in_equation.r2adj) + '\n')
    
    if in_equation.Fstat == None:
        outputFile.write('Model F-statistic: n/a\n')
    else:
        outputFile.write('Model F-statistic: ' + str(in_equation.Fstat) + '\n')
    
    if in_equation.Fpv == None:
        outputFile.write('Model F-statistic p-value: n/a\n')
    else:
        outputFile.write('Model F-statistic p-value: ' + str(in_equation.Fpv) + '\n')
    
    if in_equation.ll == None:
        outputFile.write('Model log-likelihood: n/a\n')
    else:
        outputFile.write('Model log-likelihood: ' + str(in_equation.ll) + '\n')
    
    if in_equation.aic == None:
        outputFile.write('Model AIC: n/a\n')
    else:
        outputFile.write('Model AIC: ' + str(in_equation.aic) + '\n')
    
    if in_equation.bic == None:
        outputFile.write('Model BIC: n/a\n')
    else:
        outputFile.write('Model BIC: ' + str(in_equation.bic) + '\n')
    
    
    outputFile.write('\n')
    outputFile.write("Individual Parameter Statistics:\n")
    for i in range(len(in_equation.solvedCoefficients)):
        if in_equation.tstat_beta == None:
            tstat = 'n/a'
        else:
            tstat = '%-.5E' %  ( in_equation.tstat_beta[i])
    
        if in_equation.pstat_beta == None:
            pstat = 'n/a'
        else:
            pstat = '%-.5E' %  ( in_equation.pstat_beta[i])
    
        if in_equation.sd_beta != None:
            outputFile.write("Coefficient %s = %-.16E, std error: %-.5E\n" % (in_equation.GetCoefficientDesignators()[i], in_equation.solvedCoefficients[i], in_equation.sd_beta[i]))
        else:
            outputFile.write("Coefficient %s = %-.16E, std error: n/a\n" % (in_equation.GetCoefficientDesignators()[i], in_equation.solvedCoefficients[i]))
        outputFile.write("          t-stat: %s, p-stat: %s, 95 percent confidence intervals: [%-.5E, %-.5E]\n" % (tstat,  pstat, in_equation.ci[i][0], in_equation.ci[i][1]))
    
    
    outputFile.write('\n')
    outputFile.write("Coefficient Covariance Matrix:\n")
    for i in  in_equation.cov_beta:
        outputFile.write(str(i) + '\n')
    
    outputFile.close()


def SaveSourceCode(in_sourceCodeFilePath,  in_equation):
    
    outputFile = open(in_sourceCodeFilePath, 'w')
        
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeCSHARP(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeVBA(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodePYTHON(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVA(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeSCILAB(in_equation))
    outputFile.write('\n\n\n\n\n\n\n\n')
    outputFile.write(pyeq2.outputSourceCodeService().GetOutputSourceCodeMATLAB(in_equation))
    
    outputFile.close()
