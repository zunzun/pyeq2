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


class ExtendedVersionHandler_LinearGrowthAndOffset(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        x_or_xy = 'xy'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' * ' + x_or_xy + ' + Offset'
        else:
            cd = inModel.GetCoefficientDesignators()
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' * (' + cd[len(cd)-2] + ' * ' + x_or_xy + ') + Offset'


    def AssembleDisplayName(self, inModel):
        return inModel._baseName + ' With Linear Growth And Offset'


    def AssembleSourceCodeName(self, inModel):
        return inModel.__class__.__name__ + "_LinearGrowthAndOffset"


    def AssembleCoefficientDesignators(self, inModel):
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._coefficientDesignators + ['Offset']
        else:
            return inModel._coefficientDesignators + [inModel.listOfAdditionalCoefficientDesignators[len(inModel._coefficientDesignators)], 'Offset']


    def AssembleOutputSourceCodeCPP(self, inModel):
        x_or_xy = 'x_in * y_in'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x_in'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel.SpecificCodeCPP() + "temp = temp * (" + x_or_xy + ") + Offset;\n"
        else:
            cd = inModel.GetCoefficientDesignators()
            return inModel.SpecificCodeCPP() + "temp = temp * ("  + cd[len(cd)-2] + ' * ' + x_or_xy + ") + Offset;\n"
        

    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        if inModel.GetDimensionality() == 2:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return inBaseModelCalculation * inDataCacheDictionary['X'] + inCoeffs[len(inCoeffs)-1]
            else:
                return inBaseModelCalculation * (inCoeffs[len(inCoeffs)-2] * inDataCacheDictionary['X']) + inCoeffs[len(inCoeffs)-1]
        else:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return inBaseModelCalculation * inDataCacheDictionary['XY'] + inCoeffs[len(inCoeffs)-1]
            else:
                return inBaseModelCalculation * (inCoeffs[len(inCoeffs)-2] * inDataCacheDictionary['XY']) + inCoeffs[len(inCoeffs)-1]
    
    

