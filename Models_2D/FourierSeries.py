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

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2

import numpy
numpy.seterr(all= 'ignore')


import pyeq2.Model_2D_BaseClass


class ScaledX_1Term(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "1 Term (Scaled X)"
    _HTML = 'y = a0 + a1*sin(c1*x)+b1*cos(c1*x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', 'a1', 'b1', 'c1']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s



class Standard_1Term(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "1 Term Standard"
    _HTML = 'y = a0 + a1*sin(x)+b1*cos(x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', 'a1', 'b1']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        sinX = inDataCacheDictionary['SinX'] # only need to perform this dictionary look-up once
        cosX = inDataCacheDictionary['CosX'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]

        try:
            temp = a0
            temp += a1 *sinX + b1 *cosX
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1*sin(x_in) + b1*cos(x_in);\n"
        return s



class Standard_2Term(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "2 Term Standard"
    _HTML = 'y = a0 + a1*sin(x)+b1*cos(x) + a2*sin(2x)+b2*cos(2x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', 'a1', 'b1', 'a2', 'b2']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        sinX = inDataCacheDictionary['SinX'] # only need to perform this dictionary look-up once
        cosX = inDataCacheDictionary['CosX'] # only need to perform this dictionary look-up once
        sin2X = inDataCacheDictionary['SinMultX_2.0'] # only need to perform this dictionary look-up once
        cos2X = inDataCacheDictionary['CosMultX_2.0'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        a2 = inCoeffs[3]
        b2 = inCoeffs[4]

        try:
            temp = a0
            temp += a1 *sinX + b1 *cosX
            temp += a2 *sin2X + b2 *cos2X
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1*sin(x_in) + b1*cos(x_in);\n"
        s += "\ttemp +=  a2*sin(2.0 * x_in) + b2*cos(2.0 * x_in);\n"
        return s



class Standard_3Term(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "3 Term Standard"
    _HTML = 'y = a0 + a1*sin(x)+b1*cos(x) + a2*sin(2x)+b2*cos(2x) + a3*sin(3x)+b3*cos(3x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', 'a1', 'b1', 'a2', 'b2', 'a3', 'b3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        sinX = inDataCacheDictionary['SinX'] # only need to perform this dictionary look-up once
        cosX = inDataCacheDictionary['CosX'] # only need to perform this dictionary look-up once
        sin2X = inDataCacheDictionary['SinMultX_2.0'] # only need to perform this dictionary look-up once
        cos2X = inDataCacheDictionary['CosMultX_2.0'] # only need to perform this dictionary look-up once
        sin3X = inDataCacheDictionary['SinMultX_3.0'] # only need to perform this dictionary look-up once
        cos3X = inDataCacheDictionary['CosMultX_3.0'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        a2 = inCoeffs[3]
        b2 = inCoeffs[4]
        a3 = inCoeffs[5]
        b3 = inCoeffs[6]

        try:
            temp = a0
            temp += a1 *sinX + b1 *cosX
            temp += a2 *sin2X + b2 *cos2X
            temp += a3 *sin3X + b3 *cos3X
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1*sin(x_in) + b1*cos(x_in);\n"
        s += "\ttemp +=  a2*sin(2.0 * x_in) + b2*cos(2.0 * x_in);\n"
        s += "\ttemp +=  a3*sin(3.0 * x_in) + b3*cos(3.0 * x_in);\n"
        return s



class Standard_4Term(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "4 Term Standard"
    _HTML = 'y = a0 + a1*sin(x)+b1*cos(x) + a2*sin(2x)+b2*cos(2x) + a3*sin(3x)+b3*cos(3x) + a4*sin(4x)+b4*cos(4x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', 'a1', 'b1', 'a2', 'b2', 'a3', 'b3', 'a4', 'b4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.SinMultX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.CosMultX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        sinX = inDataCacheDictionary['SinX'] # only need to perform this dictionary look-up once
        cosX = inDataCacheDictionary['CosX'] # only need to perform this dictionary look-up once
        sin2X = inDataCacheDictionary['SinMultX_2.0'] # only need to perform this dictionary look-up once
        cos2X = inDataCacheDictionary['CosMultX_2.0'] # only need to perform this dictionary look-up once
        sin3X = inDataCacheDictionary['SinMultX_3.0'] # only need to perform this dictionary look-up once
        cos3X = inDataCacheDictionary['CosMultX_3.0'] # only need to perform this dictionary look-up once
        sin4X = inDataCacheDictionary['SinMultX_4.0'] # only need to perform this dictionary look-up once
        cos4X = inDataCacheDictionary['CosMultX_4.0'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        a2 = inCoeffs[3]
        b2 = inCoeffs[4]
        a3 = inCoeffs[5]
        b3 = inCoeffs[6]
        a4 = inCoeffs[7]
        b4 = inCoeffs[8]

        try:
            temp = a0
            temp += a1 *sinX + b1 *cosX
            temp += a2 *sin2X + b2 *cos2X
            temp += a3 *sin3X + b3 *cos3X
            temp += a4 *sin4X + b4 *cos4X
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1*sin(x_in) + b1*cos(x_in);\n"
        s += "\ttemp +=  a2*sin(2.0 * x_in) + b2*cos(2.0 * x_in);\n"
        s += "\ttemp +=  a3*sin(3.0 * x_in) + b3*cos(3.0 * x_in);\n"
        s += "\ttemp +=  a4*sin(4.0 * x_in) + b4*cos(4.0 * x_in);\n"
        return s
