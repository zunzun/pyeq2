from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2013 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

from . import IExtendedVersionHandler


class ExtendedVersionHandler_Inverse(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        if inModel.GetDimensionality() == 2:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = x / ' + inModel._leftSideHTML
        else:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = xy / ' + inModel._leftSideHTML


    def AssembleDisplayName(self, inModel):
        return'Inverse ' + inModel._baseName


    def AssembleSourceCodeName(self, inModel):
        return inModel.__module__.split('.')[-1] + '_' + inModel.__class__.__name__ + "_Inverse"


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators


    # overridden from abstract parent class
    def AppendAdditionalCoefficientBounds(self, inModel):
        return


    def AssembleOutputSourceCodeCPP(self, inModel):
        if inModel.GetDimensionality() == 2:
            return inModel.SpecificCodeCPP() + "\ttemp = x_in / temp;\n"
        else:
            return inModel.SpecificCodeCPP() + "\ttemp = (x_in * y_in) / temp;\n"


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        if inModel.GetDimensionality() == 2:
            return self.ConvertInfAndNanToLargeNumber(inDataCacheDictionary['X'] / inBaseModelCalculation)
        else:
            return self.ConvertInfAndNanToLargeNumber(inDataCacheDictionary['XY'] / inBaseModelCalculation)
