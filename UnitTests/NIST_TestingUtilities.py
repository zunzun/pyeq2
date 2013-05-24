from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, math

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
import pyeq2

# from http://www.itl.nist.gov/div898/strd/nls/nls_info.shtml
#
# The certified results are reported to 11 decimal places for each dataset.
# Clearly, most of these digits are not statistically significant, and we
# are not advocating that results should be reported to this number of
# digits in a statistical context. We do believe, however, that this
# number of digits can be useful when testing the numerical properties of
# a procedure. Except in cases where the certified value is essentially
# zero (for example, as occurs for the three Lanczos problems), a good
# nonlinear least squares procedure should be able to duplicate the
# certified results to at least 4 or 5 digits.

class NistDataObject(object):
    
    def __init__(self):
        self.Start_1_Values = []
        self.Start_2_Values = []
        self.CertifiedValues = []
        self.CertifiedValuesStandardDeviation = []
        self.RawDataIn_XY_Format = ''
        self.RawDataIn_XYZ_Format = ''
        self.ResidualSumOfSquaresString = ''
        self.ResidualSumOfSquaresValue = None



# inTakeLogOfDependantDataFlag used for the Nelson 3D fit, where data and
# fit statistics use log(y) but the data file contains y and not log(y)
def LoadDataFileFromNIST(inFileName, inTakeLogOfDependantDataFlag = False):
    
    f = open(inFileName, 'rt')
    fileLines = f.readlines()
    f.close()
    
    nistDataObject = NistDataObject()
    
    # starting values
    splitted = fileLines[4].replace(')', '').split()
    beginLine = int(splitted[3])
    endLine = int(splitted[5])
    
    for lineIndex in range(beginLine - 1, endLine):
        splitted = fileLines[lineIndex].split()
        nistDataObject.Start_1_Values.append(float(splitted[2]))
        nistDataObject.Start_2_Values.append(float(splitted[3]))
        nistDataObject.CertifiedValues.append(float(splitted[4]))
        nistDataObject.CertifiedValuesStandardDeviation.append(float(splitted[5]))

    # SSQ
    nistDataObject.ResidualSumOfSquaresString = fileLines[endLine + 1].split()[-1:][0]
    nistDataObject.ResidualSumOfSquaresValue = float(nistDataObject.ResidualSumOfSquaresString)
        
    # data in x y (z) format (reverse of NIST data file)
    splitted = fileLines[6].replace(')', '').split()
    beginLine = int(splitted[2])
    endLine = int(splitted[4])
    
    for lineIndex in range(beginLine - 1, endLine):
        splitted = fileLines[lineIndex].split()
        
        depString = splitted[0]
        if inTakeLogOfDependantDataFlag == True:
            depString = str(math.log(float(depString)))
            
        if len(splitted) == 2:
            nistDataObject.RawDataIn_XY_Format += splitted[1] + ' ' + depString + '\n'
        else:
            nistDataObject.RawDataIn_XYZ_Format += splitted[1] + ' ' + splitted[2] + ' ' + depString + '\n'
        
    return nistDataObject


def CalculateAndPrintResults(equation, nistDataObject, inStartValues, inStartValuesString, inPrintFlag):

    if nistDataObject.RawDataIn_XY_Format != "": # 2D data
        rawData = nistDataObject.RawDataIn_XY_Format
    else: # 3D data
        rawData = nistDataObject.RawDataIn_XYZ_Format
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(rawData, equation, False)
    
    equation.estimatedCoefficients = inStartValues
    
    equation.Solve()
    
    ssq = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    
    #
    # See the NIST note at the top of this file regarding dignificant digits.
    # NIST files truncate SSQ to 10 decimal places.  First check if 8 decimal
    # places (to allow for machine precision, rounding, etc) in Python
    # gives the same result as NIST, then compare actual values if that fails
    # as it is possible though very, very unlikely that pyeq2 fits better than NIST.
    ssqString = "%-.11E" % (ssq)
    if (ssqString[:10] + ssqString[-4:]) == (nistDataObject.ResidualSumOfSquaresString[:10] + nistDataObject.ResidualSumOfSquaresString[-4:]):
        compareString = '- equal to NIST'
        betterThanOrEqualToNIST = True
    else:
        deltaSSQ = nistDataObject.ResidualSumOfSquaresValue - ssq
        if deltaSSQ > 0.0: # NIST gives values to 10 decimal places
            compareString = '- better than NIST'
            betterThanOrEqualToNIST = True
        elif deltaSSQ < 0.0:
            compareString = '- worse than NIST'
            betterThanOrEqualToNIST = False
        else:
            compareString = '- equal to NIST'
            betterThanOrEqualToNIST = True
    
    
    if inPrintFlag:
        print(equation.GetDisplayName(), str(equation.GetDimensionality()) + "D", '- using "' + inStartValuesString + '" values')
        print(equation.fittingTargetDictionary[equation.fittingTarget], '=',)
        print(ssqString + ', should be',)
        print(nistDataObject.ResidualSumOfSquaresValue, compareString)
        
        print("Parameters:")
        for i in range(len(equation.solvedCoefficients)):
            spacer = ' '
            if equation.solvedCoefficients[i] < 0.0:
                spacer = ''
            print("    %s = %s%-.10E" % (equation.GetCoefficientDesignators()[i], spacer, equation.solvedCoefficients[i]),)
            print('(NIST Cert. %s%-.10E, NIST est. %s%-.5E' % (spacer, nistDataObject.CertifiedValues[i], spacer, inStartValues[i]))
        
        print()
    
    return betterThanOrEqualToNIST
