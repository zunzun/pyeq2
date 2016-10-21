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


class ExtendedVersionHandler_Default(IExtendedVersionHandler.IExtendedVersionHandler):
    

    def AssembleDisplayHTML(self, inModel):
        return inModel._HTML


    def AssembleDisplayName(self, inModel):
        return inModel._baseName


    def AssembleSourceCodeName(self, inModel):
        return inModel.__module__.split('.')[-1] + '_' + inModel.__class__.__name__


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators


    # overridden from abstract parent class
    def AppendAdditionalCoefficientBounds(self, inModel):
        return


    def AssembleOutputSourceCodeCPP(self, inModel):
        return inModel.SpecificCodeCPP()


    # overridden from abstract parent class
    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        return self.ConvertInfAndNanToLargeNumber(inBaseModelCalculation)


    # overridden from abstract parent class
    def CanLinearSolverBeUsedForSSQABS(self, inModelFlag):
        return inModelFlag
