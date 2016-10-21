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


class ExtendedVersionHandler_Reciprocal(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = 1.0 / ' + inModel._leftSideHTML


    def AssembleDisplayName(self, inModel):
        return 'Reciprocal ' + inModel._baseName


    def AssembleSourceCodeName(self, inModel):
        return inModel.__module__.split('.')[-1] + '_' + inModel.__class__.__name__ + "_Reciprocal"


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators


    # overridden from abstract parent class
    def AppendAdditionalCoefficientBounds(self, inModel):
        return


    def AssembleOutputSourceCodeCPP(self, inModel):
        return inModel.SpecificCodeCPP() + "\ttemp = 1.0 / temp;\n"


    # overridden from abstract parent class
    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        return self.ConvertInfAndNanToLargeNumber(1.0 / inBaseModelCalculation)
