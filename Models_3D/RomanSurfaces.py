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


class RomanSurfaceMinus(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (minus)"
    _HTML = 'z = (k(y<sup>2</sup>-x<sup>2</sup>) - (x<sup>2</sup>-y<sup>2</sup>)sqrt(k<sup>2</sup>-x<sup>2</sup>-y<sup>2</sup>)) / (2(x<sup>2</sup>+y<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQMINUSYSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.YSQMINUSXSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQMINUSYSQ = inDataCacheDictionary['XSQMINUSYSQ'] # only need to perform this dictionary look-up once
        YSQMINUSXSQ = inDataCacheDictionary['YSQMINUSXSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]

        try:
            temp = (k * YSQMINUSXSQ - XSQMINUSYSQ * numpy.sqrt(k * k - XSQMINUSYSQ)) / (2.0 * XSQPLUSYSQ)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (k * (y_in * y_in - x_in * x_in) - (x_in * x_in - y_in * y_in) * pow(k * k - (x_in * x_in - y_in * y_in), 0.5)) / (2.0 * (x_in * x_in + y_in * y_in));\n"
        return s



class RomanSurfaceMinus_OffsetXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (minus) Offset XY"
    _HTML = 'z = (k((y+b)<sup>2</sup>-(x+a)<sup>2</sup>) - ((x+a)<sup>2</sup>-(y+b)<sup>2</sup>)sqrt(k<sup>2</sup>-(x+a)<sup>2</sup>-(y+b)<sup>2</sup>)) / (2((x+a)<sup>2</sup>+(y+b)<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'a', 'b']
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
        
        k = inCoeffs[0]
        a = inCoeffs[1]
        b = inCoeffs[2]

        try:
            temp_x_sq = (x_in + a) * (x_in + a)
            temp_y_sq = (y_in + b) * (y_in + b)
            temp = (k * (temp_y_sq - temp_x_sq) - (temp_x_sq - temp_y_sq) * numpy.sqrt(k * k - temp_x_sq - temp_y_sq)) / (2.0 * (temp_x_sq + temp_y_sq))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble temp_x_sq = (x_in + a) * (x_in + a);\n'
        s += '\tdouble temp_y_sq = (y_in + b) * (y_in + b);\n'
        s += "\ttemp = (k * (temp_y_sq - temp_x_sq) - (temp_x_sq - temp_y_sq) * pow(k * k - temp_x_sq - temp_y_sq, 0.5)) / (2.0 * (temp_x_sq + temp_y_sq));\n"
        return s



class RomanSurfaceMinus_ScaledAndOffsetXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (minus) Scaled And Offset XY"
    _HTML = 'z = (k((cy+d)<sup>2</sup>-(ax+b)<sup>2</sup>) - ((ax+b)<sup>2</sup>-(cy+d)<sup>2</sup>)sqrt(k<sup>2</sup>-(ax+b)<sup>2</sup>-(cy+d)<sup>2</sup>)) / (2((ax+b)<sup>2</sup>+(cy+d)<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'a', 'b', 'c', 'd']
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
        
        k = inCoeffs[0]
        a = inCoeffs[1]
        b = inCoeffs[2]
        c = inCoeffs[3]
        d = inCoeffs[4]

        try:
            temp_x_sq = (a * x_in + b) * (a * x_in + b)
            temp_y_sq = (c * y_in + d) * (c * y_in + d)
            temp = (k * (temp_y_sq - temp_x_sq) - (temp_x_sq - temp_y_sq) * numpy.power(k * k - temp_x_sq - temp_y_sq)) / (2.0 * (temp_x_sq + temp_y_sq))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble temp_x_sq = (a * x_in + b) * (a * x_in + b);\n'
        s += '\tdouble temp_y_sq = (c * y_in + d) * (c * y_in + d);\n'
        s += "\ttemp = (k * (temp_y_sq - temp_x_sq) - (temp_x_sq - temp_y_sq) * pow(k * k - temp_x_sq - temp_y_sq, 0.5)) / (2.0 * (temp_x_sq + temp_y_sq));\n"
        return s



class RomanSurfacePlus(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (plus)"
    _HTML = 'z = (k(y<sup>2</sup>-x<sup>2</sup>) + (x<sup>2</sup>-y<sup>2</sup>)sqrt(k<sup>2</sup>-x<sup>2</sup>-y<sup>2</sup>)) / (2(x<sup>2</sup>+y<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQMINUSYSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.YSQMINUSXSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQMINUSYSQ = inDataCacheDictionary['XSQMINUSYSQ'] # only need to perform this dictionary look-up once
        YSQMINUSXSQ = inDataCacheDictionary['YSQMINUSXSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]

        try:
            temp = (k * YSQMINUSXSQ + XSQMINUSYSQ * numpy.sqrt(k * k - XSQMINUSYSQ)) / (2.0 * XSQPLUSYSQ)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (k * (y_in * y_in - x_in * x_in) + (x_in * x_in - y_in * y_in) * pow(k * k - (x_in * x_in - y_in * y_in), 0.5)) / (2.0 * (x_in * x_in + y_in * y_in));\n"
        return s



class RomanSurfacePlus_scaled(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (plus) Scaled"
    _HTML = 'z = Scale * (k(y<sup>2</sup>-x<sup>2</sup>) + (x<sup>2</sup>-y<sup>2</sup>)sqrt(k<sup>2</sup>-x<sup>2</sup>-y<sup>2</sup>)) / (2(x<sup>2</sup>+y<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'Scale']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQMINUSYSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.YSQMINUSXSQ(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQMINUSYSQ = inDataCacheDictionary['XSQMINUSYSQ'] # only need to perform this dictionary look-up once
        YSQMINUSXSQ = inDataCacheDictionary['YSQMINUSXSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]
        scale = inCoeffs[1]

        try:
            temp = scale * (k * YSQMINUSXSQ + XSQMINUSYSQ * numpy.sqrt(k * k - XSQMINUSYSQ)) / (2.0 * XSQPLUSYSQ)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * (k * (y_in * y_in - x_in * x_in) + (x_in * x_in - y_in * y_in) * pow(k * k - (x_in * x_in - y_in * y_in), 0.5)) / (2.0 * (x_in * x_in + y_in * y_in));\n"
        return s



class RomanSurfacePlus_OffsetXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (plus) Offset XY"
    _HTML = 'z = (k((y+b)<sup>2</sup>-(x+a)<sup>2</sup>) + ((x+a)<sup>2</sup>-(y+b)<sup>2</sup>)sqrt(k<sup>2</sup>-(x+a)<sup>2</sup>-(y+b)<sup>2</sup>)) / (2((x+a)<sup>2</sup>+(y+b)<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'a', 'b']
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
        
        k = inCoeffs[0]
        a = inCoeffs[1]
        b = inCoeffs[2]

        try:
            temp_x_sq = (x_in + a) * (x_in + a)
            temp_y_sq = (y_in + b) * (y_in + b)
            temp = (k * (temp_y_sq - temp_x_sq) + (temp_x_sq - temp_y_sq) * numpy.sqrt(k * k - temp_x_sq - temp_y_sq)) / (2.0 * (temp_x_sq + temp_y_sq))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble temp_x_sq = (x_in + a) * (x_in + a);\n'
        s += '\tdouble temp_y_sq = (y_in + b) * (y_in + b);\n'
        s += "\ttemp = (k * (temp_y_sq - temp_x_sq) + (temp_x_sq - temp_y_sq) * pow(k * k - temp_x_sq - temp_y_sq, 0.5)) / (2.0 * (temp_x_sq + temp_y_sq));\n"
        return s



class RomanSurfacePlus_ScaledAndOffsetXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Roman Surface (plus) Scaled And Offset XY"
    _HTML = 'z = (k((cy+d)<sup>2</sup>-(ax+b)<sup>2</sup>) + ((ax+b)<sup>2</sup>-(cy+d)<sup>2</sup>)sqrt(k<sup>2</sup>-(ax+b)<sup>2</sup>-(cy+d)<sup>2</sup>)) / (2((ax+b)<sup>2</sup>+(cy+d)<sup>2</sup>))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'a', 'b', 'c', 'd']
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
        
        k = inCoeffs[0]
        a = inCoeffs[1]
        b = inCoeffs[2]
        c = inCoeffs[3]
        d = inCoeffs[4]

        try:
            temp_x_sq = (a * x_in + b) * (a * x_in + b)
            temp_y_sq = (c * y_in + d) * (c * y_in + d)
            temp = (k * (temp_y_sq - temp_x_sq) + (temp_x_sq - temp_y_sq) * numpy.sqrt(k * k - temp_x_sq - temp_y_sq)) / (2.0 * (temp_x_sq + temp_y_sq))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble temp_x_sq = (a * x_in + b) * (a * x_in + b);\n'
        s += '\tdouble temp_y_sq = (c * y_in + d) * (c * y_in + d);\n'
        s += "\ttemp = (k * (temp_y_sq - temp_x_sq) + (temp_x_sq - temp_y_sq) * pow(k * k - temp_x_sq - temp_y_sq, 0.5)) / (2.0 * (temp_x_sq + temp_y_sq));\n"
        return s



