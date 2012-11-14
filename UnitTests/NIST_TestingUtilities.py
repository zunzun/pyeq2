from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys

# ensure pyeq2 can be imported
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
import pyeq2


class NistDataObject(object):
    
    def __init__(self):
        self.Start_1_Values = []
        self.Start_2_Values = []
        self.CertifiedValues = []
        self.CertifiedValuesStandardDeviation = []
        self.RawDataIn_XY_Format = ''
        self.ResidualSumOfSquaresString = ''
        self.ResidualSumOfSquaresValue = None



def LoadDataFileFromNIST(inFileName):
    
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
        
    # data in x y format (reverse of NIST data file)
    splitted = fileLines[6].replace(')', '').split()
    beginLine = int(splitted[2])
    endLine = int(splitted[4])
    
    for lineIndex in range(beginLine - 1, endLine):
        splitted = fileLines[lineIndex].split()
        nistDataObject.RawDataIn_XY_Format += splitted[1] + ' ' + splitted[0] + '\n'
        
    return nistDataObject


def CalculateAndPrintResults(equation, nistDataObject, inStartValues, inStartValuesString, inPrintFlag):

    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(nistDataObject.RawDataIn_XY_Format, equation, False)
    
    equation.estimatedCoefficients = inStartValues
    
    equation.Solve()
    
    ssq = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
    
    # NIST truncates SSQ to 10 decimal places.  First check if the same truncation
    # in Python gives the same result, then compare actual values if that fails
    ssqString = "%-.10E" % (ssq)
    if ssqString == nistDataObject.ResidualSumOfSquaresString:
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
