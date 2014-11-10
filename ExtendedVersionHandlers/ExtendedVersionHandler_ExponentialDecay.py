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

import pyeq2
from . import IExtendedVersionHandler

import numpy
numpy.seterr(all= 'ignore')


class ExtendedVersionHandler_ExponentialDecay(IExtendedVersionHandler.IExtendedVersionHandler):
    
    def AssembleDisplayHTML(self, inModel):
        x_or_xy = 'xy'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / exp(' + x_or_xy + ')'
        else:
            try:
                cd = inModel.GetCoefficientDesignators()
                return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / (' + cd[-1] + ' * exp(' + x_or_xy + '))'
            except:
                return inModel._HTML + '<br>' + inModel._leftSideHTML + ' = ' + inModel._leftSideHTML + ' / (exp(' + x_or_xy + '))'


    def AssembleDisplayName(self, inModel):
        return inModel._baseName + ' With Exponential Decay'


    def AssembleSourceCodeName(self, inModel):
        return inModel.__module__.split('.')[-1] + '_' + inModel.__class__.__name__ + "_ExponentialDecay"


    def AssembleCoefficientDesignators(self, inModel):
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel._coefficientDesignators
        else:
            return inModel._coefficientDesignators + [inModel.listOfAdditionalCoefficientDesignators[len(inModel._coefficientDesignators)]]


    # overridden from abstract parent class
    def AppendAdditionalCoefficientBounds(self, inModel):
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return
        else:
            if inModel.upperCoefficientBounds != []:
                inModel.upperCoefficientBounds.append(None)
            if inModel.lowerCoefficientBounds != []:
                inModel.lowerCoefficientBounds.append(None)


    def AssembleOutputSourceCodeCPP(self, inModel):
        x_or_xy = 'x_in * y_in'
        if inModel.GetDimensionality() == 2:
            x_or_xy = 'x_in'
            
        if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
            return inModel.SpecificCodeCPP() + "\ttemp = temp / exp(" + x_or_xy + ");\n"
        else:
            cd = inModel.GetCoefficientDesignators()
            return inModel.SpecificCodeCPP() + "\ttemp = temp / ("  + cd[-1] + ' * exp(' + x_or_xy + "));\n"
        

    def GetAdditionalDataCacheFunctions(self, inModel, inDataCacheFunctions):
        foundX = False
        foundXY = False
        for i in inDataCacheFunctions: # if these are already in the cache, we don't need to add them again
            if i[0] == 'ExpX' and inModel.GetDimensionality() == 2:
                foundX = True
            if i[0] == 'ExpXY' and inModel.GetDimensionality() == 3:
                foundXY = True
                
        if inModel.GetDimensionality() == 2:
            if not foundX:
                return inDataCacheFunctions + \
                       [[pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []]]
        else:
            if not foundXY:
                return inDataCacheFunctions + \
                       [[pyeq2.DataCache.DataCacheFunctions.ExpXY(NameOrValueFlag=1), []]]
        return inDataCacheFunctions


    def GetAdditionalModelPredictions(self, inBaseModelCalculation, inCoeffs, inDataCacheDictionary, inModel):
        if inModel.GetDimensionality() == 2:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return self.ConvertInfAndNanToLargeNumber(inBaseModelCalculation / inDataCacheDictionary['ExpX'])
            else:
                return self.ConvertInfAndNanToLargeNumber(inBaseModelCalculation / (inCoeffs[len(inCoeffs)-1] * inDataCacheDictionary['ExpX']))
        else:
            if inModel.baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions:
                return self.ConvertInfAndNanToLargeNumber(inBaseModelCalculation / inDataCacheDictionary['ExpXY'])
            else:
                return self.ConvertInfAndNanToLargeNumber(inBaseModelCalculation / (inCoeffs[len(inCoeffs)-1] * inDataCacheDictionary['ExpXY']))
