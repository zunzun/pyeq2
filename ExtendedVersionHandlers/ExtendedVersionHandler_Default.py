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


class ExtendedVersionHandler_Default(IExtendedVersionHandler.IExtendedVersionHandler):
    

    def AssembleDisplayHTML(self, inModel):
        return inModel._HTML


    def AssembleDisplayName(self, inModel):
        return inModel._baseName


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__


    def AssembleCoefficientDesignators(self, inModel):
        return inModel._coefficientDesignators


    def AssembleOutputSourceCodeCPP(self, inModel):
        return inModel.SpecificCodeCPP()


    # overridden from abstract parent class
    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        return inBaseModelCalculation


    # overridden from abstract parent class
    def CanLinearSolverBeUsedForSSQABS(self, inModelFlag):
        return inModelFlag
