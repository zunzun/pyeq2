#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2012 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id$

import pyeq2
import IExtendedVersionHandler


class ExtendedVersionHandler_InverseWithOffset(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        if inModel.GetDimensionality() == 2:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = x / ' + inModel._leftSideHTML + ' + Offset'
        else:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = xy / (' + inModel._leftSideHTML + ' + Offset'


    def AssembleDisplayName(self, inModel):
        return 'Inverse ' + inModel._baseName + ' With Offset'


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__ + "_InverseWithOffset"


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators + ['Offset']


    def AssembleOutputSourceCodeCPP(self, inModel):
        if inModel.GetDimensionality() == 2:
            return inModel.SpecificCodeCPP() + "temp = x_in / temp + Offset;\n"
        else:
            return inModel.SpecificCodeCPP() + "temp = (x_in * y_in) / temp + Offset;\n"


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        if inModel.GetDimensionality() == 2:
            return self.ConvertInfAndNanToLargeNumber((inDataCacheDictionary['X'] / inBaseModelCalculation) + inCoeffs[len(inCoeffs)-1])
        else:
            return self.ConvertInfAndNanToLargeNumber((inDataCacheDictionary['XY'] / inBaseModelCalculation) + inCoeffs[len(inCoeffs)-1])
