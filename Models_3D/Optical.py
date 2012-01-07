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

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them


import pyeq2.Model_3D_BaseClass


class SagForAsphere0(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 0"
    _HTML = 's<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + offset'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'offset']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        offset = inCoeffs[2]

        try:
            s_sq = XSQPLUSYSQ
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + offset
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s += '\tdouble s_sq = x_in * x_in + y_in * y_in;\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + offset;\n'
        return s



class SagForAsphere0_Borisovsky(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 0 Borisovsky"
    _HTML = 's<sup>2</sup> = (x - a)<sup>2</sup> + (y - b)<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + offset'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'k', 'r', 'offset']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        k = inCoeffs[2]
        r = inCoeffs[3]
        offset = inCoeffs[4]

        try:
            s_sq = (x_in - a) * (x_in - a) + (y_in - b) * (y_in - b)
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + offset
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = (x_in - a) * (x_in - a) + (y_in - b) * (y_in - b);\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + offset;\n'
        return s



