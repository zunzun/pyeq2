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


import pyeq2.Model_3D_BaseClass


class RationalA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational A"
    _HTML = 'z = (a + bx + cy)/(1 + dx + fy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*x_in + c*y_in) / (1.0 + d*x_in + f*y_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in) / (1.0 + d*x_in + f*y_in);\n"
        return s



class RationalB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational B"
    _HTML = 'z = (a + b*ln(x) + c*ln(y))/(1 + dx + fy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = (a + b*LogX + c*LogY) / (1.0 + d*x_in + f*y_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*log(x_in) + c*log(y_in)) / (1.0 + d*x_in + f*y_in);\n"
        return s



class RationalC(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational C"
    _HTML = 'z = (a + b*exp(x) + c*ln(y))/(1 + dx + fy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = (a + b*ExpX + c*LogY) / (1.0 + d*x_in + f*y_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*exp(x_in) + c*log(y_in)) / (1.0 + d*x_in + f*y_in);\n"
        return s



class RationalD(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational D"
    _HTML = 'z = (a + b*ln(x) + c*exp(y))/(1 + dx + fy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = (a + b*LogX + c*ExpY) / (1.0 + d*x_in + f*y_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*log(x_in) + c*exp(y_in)) / (1.0 + d*x_in + f*y_in);\n"
        return s



class RationalE(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational E"
    _HTML = 'z = (a + b*exp(x) + c*exp(y))/(1 + dx + fy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = (a + b*ExpX + c*ExpY) / (1.0 + d*x_in + f*y_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*exp(x_in) + c*exp(y_in)) / (1.0 + d*x_in + f*y_in);\n"
        return s



class RationalF(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational F"
    _HTML = 'z = (a + bx + cy)/(1 + d*ln(x) + f*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*x_in + c*y_in) / (1.0 + d*LogX + f*LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in) / (1.0 + d*log(x_in) + f*log(y_in));\n"
        return s



class RationalG(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational G"
    _HTML = 'z = (a + bx + cy)/(1 + d*exp(x) + f*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*x_in + c*y_in) / (1.0 + d*ExpX + f*LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in) / (1.0 + d*exp(x_in) + f*log(y_in));\n"
        return s



class RationalH(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational H"
    _HTML = 'z = (a + bx + cy)/(1 + d*ln(x) + f*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*x_in + c*y_in) / (1.0 + d*LogX + f*ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in) / (1.0 + d*log(x_in) + f*exp(y_in));\n"
        return s



class RationalI(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational I"
    _HTML = 'z = (a + bx + cy)/(1 + d*exp(x) + f*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*x_in + c*y_in) / (1.0 + d*ExpX + f*ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in) / (1.0 + d*exp(x_in) + f*exp(y_in));\n"
        return s



class RationalJ(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational J"
    _HTML = 'z = (a + b*ln(x) + c*ln(y))/(1 + d*ln(x) + f*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*LogX + c*LogY) / (1.0 + d*LogX + f*LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*log(x_in) + c*log(y_in)) / (1.0 + d*log(x_in) + f*log(y_in));\n"
        return s



class RationalK(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational K"
    _HTML = 'z = (a + b*exp(x) + c*ln(y))/(1 + d*exp(x) + f*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*ExpX + c*LogY) / (1.0 + d*ExpX + f*LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*exp(x_in) + c*log(y_in)) / (1.0 + d*exp(x_in) + f*log(y_in));\n"
        return s



class RationalL(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational L"
    _HTML = 'z = (a + b*ln(x) + c*exp(y))/(1 + d*ln(x) + f*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*LogX + c*ExpY) / (1.0 + d*LogX + f*ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*log(x_in) + c*exp(y_in)) / (1.0 + d*log(x_in) + f*exp(y_in));\n"
        return s



class RationalM(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational M"
    _HTML = 'z = (a + b*exp(x) + c*exp(y))/(1 + d*exp(x) + f*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp  = (a + b*ExpX+ c*ExpY) / (1.0 + d*ExpX + f*ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*exp(x_in) + c*exp(y_in)) / (1.0 + d*exp(x_in) + f*exp(y_in));\n"
        return s



class RationalN(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational N"
    _HTML = 'z = (a + bx + cy + dxy)/(1 + fx + gy + hxy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*x_in + c*y_in + d*XY) / (1.0 + f*x_in + g*y_in + h*XY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in + d*x_in*y_in) / (1.0 + f*x_in + g*y_in + h*x_in*y_in);\n"
        return s



class RationalO(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational O"
    _HTML = 'z = (a + b*ln(x) + c*ln(y) + d*ln(x)ln(y))/(1 + fx + gy + hxy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        LogX_LogY = inDataCacheDictionary['LogX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = (a + b*LogX + c*LogY + d*LogX_LogY) / (1.0 + f*x_in + g*y_in + h*XY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*log(x_in) + c*log(y_in) + d*log(x_in)*log(y_in)) / (1.0 + f*x_in + g*y_in + h*x_in*y_in);\n"
        return s



class RationalP(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational P"
    _HTML = 'z = (a + b*exp(x) + c*ln(y) + d*exp(x)ln(y))/(1 + fx + gy + hxy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        ExpX_LogY = inDataCacheDictionary['ExpX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = (a + b*ExpX + c*LogY + d*ExpX_LogY) / (1.0 + f*x_in + g*y_in + h*XY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*exp(x_in) + c*log(y_in) + d*exp(x_in)*log(y_in)) / (1.0 + f*x_in + g*y_in + h*x_in*y_in);\n"
        return s



class RationalQ(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational Q"
    _HTML = 'z = (a + b*ln(x) + c*exp(y) + d*ln(x)exp(y))/(1 + fx + gy + hxy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogX_ExpY = inDataCacheDictionary['LogX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = (a + b*LogX + c*ExpY + d*LogX_ExpY) / (1.0 + f*x_in + g*y_in + h*XY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*log(x_in) + c*exp(y_in) + d*log(x_in)*exp(y_in)) / (1.0 + f*x_in + g*y_in + h*x_in*y_in);\n"
        return s



class RationalR(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational R"
    _HTML = 'z = (a + b*exp(x) + c*exp(y) + d*exp(x)exp(y))/(1 + fx + gy + hxy)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpX_ExpY = inDataCacheDictionary['ExpX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = (a + b*ExpX + c*ExpY + d*ExpX_ExpY) / (1.0 + f*x_in + g*y_in + h*XY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a + b*exp(x_in) + c*exp(y_in) + d*exp(x_in)*exp(y_in)) / (1.0 + f*x_in + g*y_in + h*x_in*y_in);\n"
        return s



class RationalS(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational S"
    _HTML = 'z = (a + bx + cy + dxy)/(1 + f*ln(x) + g*ln(y) + h*ln(x)*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogX_LogY = inDataCacheDictionary['LogX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*x_in + c*y_in + d*XY) / (1.0 + f*LogX + g*LogY + h*LogX_LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in + d*x_in*y_in) / (1.0 + f*log(x_in) + g*log(y_in) + h*log(x_in)*log(y_in));\n"
        return s



class RationalT(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational T"
    _HTML = 'z = (a + bx + cy + dxy)/(1 + f*exp(x) + g*ln(y) + h*exp(x)*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpX_LogY = inDataCacheDictionary['ExpX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*x_in + c*y_in + d*XY) / (1.0 + f*ExpX + g*LogY + h*ExpX_LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in + d*x_in*y_in) / (1.0 + f*exp(x_in) + g*log(y_in) + h*exp(x_in)*log(y_in));\n"
        return s



class RationalU(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational U"
    _HTML = 'z = (a + bx + cy + dxy)/(1 + f*ln(x) + g*exp(y) + h*ln(x)*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        LogX_ExpY = inDataCacheDictionary['LogX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*x_in + c*y_in + d*XY) / (1.0 + f*LogX + g*ExpY + h*LogX_ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in + d*x_in*y_in) / (1.0 + f*log(x_in) + g*exp(y_in) + h*log(x_in)*exp(y_in));\n"
        return s



class RationalV(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational V"
    _HTML = 'z = (a + bx + cy + dxy)/(1 + f*exp(x) + g*exp(y) + h*exp(x)*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        ExpX_ExpY = inDataCacheDictionary['ExpX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*x_in + c*y_in + d*XY) / (1.0 + f*ExpX + g*ExpY + h*ExpX_ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*x_in + c*y_in + d*x_in*y_in) / (1.0 + f*exp(x_in) + g*exp(y_in) + h*exp(x_in)*exp(y_in));\n"
        return s



class RationalW(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational W"
    _HTML = 'z = (a + b*ln(x) + c*ln(y) + d*ln(x)*ln(y))/(1 + f*ln(x) + g*ln(y) + h*ln(x)*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        LogX_LogY = inDataCacheDictionary['LogX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*LogX + c*LogY + d*LogX_LogY) / (1.0 + f*LogX + g*LogY + h*LogX_LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*log(x_in) + c*log(y_in) + d*log(x_in)*log(y_in)) / (1.0 + f*log(x_in) + g*log(y_in) + h*log(x_in)*log(y_in));\n"
        return s



class RationalX(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational X"
    _HTML = 'z = (a + b*exp(x) + c*ln(y) + d*exp(x)*ln(y))/(1 + f*exp(x) + g*ln(y) + h*exp(x)*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
    independentData2CannotContainZeroFlag = True
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        ExpX_LogY = inDataCacheDictionary['ExpX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = (a + b*ExpX + c*LogY + d*ExpX_LogY) / (1.0 + f*ExpX + g*LogY + h*ExpX_LogY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*exp(x_in) + c*log(y_in) + d*exp(x_in)*log(y_in)) / (1.0 + f*exp(x_in) + g*log(y_in) + h*exp(x_in)*log(y_in));\n"
        return s



class RationalY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational Y"
    _HTML = 'z = (a + b*ln(x) + c*exp(y) + d*ln(x)*exp(y))/(1 + f*ln(x) + g*exp(y) + h*ln(x)*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        LogX_ExpY = inDataCacheDictionary['LogX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*LogX + c*ExpY + d*LogX_ExpY) / (1.0 + f*LogX + g*ExpY + h*LogX_ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*log(x_in) + c*exp(y_in) + d*log(x_in)*exp(y_in)) / (1.0 + f*log(x_in) + g*exp(y_in) + h*log(x_in)*exp(y_in));\n"
        return s



class RationalZ(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rational Z"
    _HTML = 'z = (a + b*exp(x) + c*exp(y) + d*exp(x)*exp(y))/(1 + f*exp(x) + g*exp(y) + h*exp(x)*exp(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        ExpX_ExpY = inDataCacheDictionary['ExpX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp  = (a + b*ExpX + c*ExpY + d*ExpX_ExpY) / (1.0 + f*ExpX + g*ExpY + h*ExpX_ExpY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp  = (a + b*exp(x_in) + c*exp(y_in) + d*exp(x_in)*exp(y_in)) / (1.0 + f*exp(x_in) + g*exp(y_in) + h*exp(x_in)*exp(y_in));\n"
        return s



