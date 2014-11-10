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


class FullCubicLogarithmic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Cubic Logarithmic"
    _HTML = 'z = a + b*ln(x) + c*ln(y) + d*ln(x)<sup>2</sup> + f*ln(y)<sup>2</sup> + g*ln(x)<sup>3</sup> + h*ln(y)<sup>3</sup> + i*ln(x)*ln(y) + j*ln(x)<sup>2</sup>*ln(y) + k*ln(x)*ln(y)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX_PowLogY(NameOrValueFlag=1, args=[2.0, 1.0]), [2.0, 1.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX_PowLogY(NameOrValueFlag=1, args=[1.0, 2.0]), [1.0, 2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        PowLogX2 = inDataCacheDictionary['PowLogX_2.0'] # only need to perform this dictionary look-up once
        PowLogY2 = inDataCacheDictionary['PowLogY_2.0'] # only need to perform this dictionary look-up once
        PowLogX3 = inDataCacheDictionary['PowLogX_3.0'] # only need to perform this dictionary look-up once
        PowLogY3 = inDataCacheDictionary['PowLogY_3.0'] # only need to perform this dictionary look-up once
        LogX_LogY = inDataCacheDictionary['LogX_LogY'] # only need to perform this dictionary look-up once
        PowLogXPowLogY21 = inDataCacheDictionary['PowLogX_PowLogY_2.01.0'] # only need to perform this dictionary look-up once
        PowLogXPowLogY12 = inDataCacheDictionary['PowLogX_PowLogY_1.02.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]
        j = inCoeffs[8]
        k = inCoeffs[9]

        try:
            temp = a
            temp += b * LogX
            temp += c * LogY
            temp += d * PowLogX2
            temp += f * PowLogY2
            temp += g * PowLogX3
            temp += h * PowLogY3
            temp += i * LogX_LogY
            temp += j * PowLogXPowLogY21
            temp += k * PowLogXPowLogY12
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(x_in);\n"
        s += "\ttemp += c * log(y_in);\n"
        s += "\ttemp += d * pow(log(x_in), 2.0);\n"
        s += "\ttemp += f * pow(log(y_in), 2.0);\n"
        s += "\ttemp += g * pow(log(x_in), 3.0);\n"
        s += "\ttemp += h * pow(log(y_in), 3.0);\n"
        s += "\ttemp += i * log(x_in) * log(y_in);\n"
        s += "\ttemp += j * pow(log(x_in), 2.0) * log(y_in);\n"
        s += "\ttemp += k * log(x_in) * pow(log(y_in), 2.0);\n"
        return s



class FullCubicLogarithmicTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Full Cubic Logarithmic"
    _HTML = 'z = a + b*ln(m*x+n) + c*ln(o*y+p) + d*ln(m*x+n)<sup>2</sup> + f*ln(o*y+p)<sup>2</sup> + g*ln(m*x+n)<sup>3</sup> + h*ln(o*y+p)<sup>3</sup> + i*ln(m*x+n)*ln(o*y+p) + j*ln(m*x+n)<sup>2</sup>*ln(o*y+p) + k*ln(m*x+n)*ln(o*y+p)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p']
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
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]
        j = inCoeffs[8]
        k = inCoeffs[9]
        m = inCoeffs[10]
        n = inCoeffs[11]
        o = inCoeffs[12]
        p = inCoeffs[13]

        try:
            temp = a
            temp += b * numpy.log(m * x_in + n)
            temp += c * numpy.log(o * y_in + p)
            temp += d * numpy.square(numpy.log(m * x_in + n))
            temp += f * numpy.square(numpy.log(o * y_in + p))
            temp += g * numpy.power(numpy.log(m * x_in + n), 3.0)
            temp += h * numpy.power(numpy.log(o * y_in + p), 3.0)
            temp += i * numpy.log(m * x_in + n) * numpy.log(o * y_in + p)
            temp += j * numpy.power(numpy.log(m * x_in + n), 2.0) * numpy.log(o * y_in + p)
            temp += k * numpy.log(m * x_in + n) * numpy.square(numpy.log(o * y_in + p))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(m * x_in + n);\n"
        s += "\ttemp += c * log(o * y_in + p);\n"
        s += "\ttemp += d * pow(log(m * x_in + n), 2.0);\n"
        s += "\ttemp += f * pow(log(o * y_in + p), 2.0);\n"
        s += "\ttemp += g * pow(log(m * x_in + n), 3.0);\n"
        s += "\ttemp += h * pow(log(o * y_in + p), 3.0);\n"
        s += "\ttemp += i * log(m * x_in + n) * log(o * y_in + p);\n"
        s += "\ttemp += j * pow(log(m * x_in + n), 2.0) * log(o * y_in + p);\n"
        s += "\ttemp += k * log(m * x_in + n) * pow(log(o * y_in + p), 2.0);\n"
        return s



class FullQuadraticLogarithmic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Quadratic Logarithmic"
    _HTML = 'z = a + b*ln(x) + c*ln(y) + d*ln(x)<sup>2</sup> + f*ln(y)<sup>2</sup> + g*ln(x)*ln(y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX_LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        PowLogX2 = inDataCacheDictionary['PowLogX_2.0'] # only need to perform this dictionary look-up once
        PowLogY2 = inDataCacheDictionary['PowLogY_2.0'] # only need to perform this dictionary look-up once
        LogX_LogY = inDataCacheDictionary['LogX_LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a
            temp += b * LogX
            temp += c * LogY
            temp += d * PowLogX2
            temp += f * PowLogY2
            temp += g * LogX_LogY
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(x_in);\n"
        s += "\ttemp += c * log(y_in);\n"
        s += "\ttemp += d * pow(log(x_in), 2.0);\n"
        s += "\ttemp += f * pow(log(y_in), 2.0);\n"
        s += "\ttemp += g * log(x_in) * log(y_in);\n"
        return s



class FullQuadraticLogarithmicTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Full Quadratic Logarithmic"
    _HTML = 'z = a + b*ln(h*x+i) + c*ln(j*y+k) + d*ln(h*x+i)<sup>2</sup> + f*ln(j*y+k)<sup>2</sup> + g*ln(h*x+i)*ln(j*y+k)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k']
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
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]
        j = inCoeffs[8]
        k = inCoeffs[9]

        try:
            temp = a
            temp += b * numpy.log(h * x_in + i)
            temp += c * numpy.log(j * y_in + k)
            temp += d * numpy.square(numpy.log(h * x_in + i))
            temp += f * numpy.square(numpy.log(j * y_in + k))
            temp += g * numpy.log(h * x_in + i) * numpy.log(j * y_in + k)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(h * x_in + i);\n"
        s += "\ttemp += c * log(j * y_in + k);\n"
        s += "\ttemp += d * pow(log(h * x_in + i), 2.0);\n"
        s += "\ttemp += f * pow(log(j * y_in + k), 2.0);\n"
        s += "\ttemp += g * log(h * x_in + i) * log(j * y_in + k);\n"
        return s



class LinearLogarithmic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Linear Logarithmic"
    _HTML = 'z = a + b*ln(x) + c*ln(y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * LogX + c * LogY
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b * log(x_in) + c * log(y_in);\n"
        return s



class LinearLogarithmicTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Linear Logarithmic"
    _HTML = 'z = a + b*ln(d*x+f) + c*ln(g*y+h)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
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
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a + b * numpy.log(d * x_in + f) + c * numpy.log(g * y_in + h)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b * log(d * x_in + f) + c * log(g * y_in + h);\n"
        return s



class SimplifiedCubicLogarithmic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Cubic Logarithmic"
    _HTML = 'z = a + b*ln(x) + c*ln(y) + d*ln(x)<sup>2</sup> + f*ln(y)<sup>2</sup> + g*ln(x)<sup>3</sup> + h*ln(y)<sup>3</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        PowLogX2 = inDataCacheDictionary['PowLogX_2.0'] # only need to perform this dictionary look-up once
        PowLogY2 = inDataCacheDictionary['PowLogY_2.0'] # only need to perform this dictionary look-up once
        PowLogX3 = inDataCacheDictionary['PowLogX_3.0'] # only need to perform this dictionary look-up once
        PowLogY3 = inDataCacheDictionary['PowLogY_3.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a
            temp += b * LogX
            temp += c * LogY
            temp += d * PowLogX2
            temp += f * PowLogY2
            temp += g * PowLogX3
            temp += h * PowLogY3
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(x_in);\n"
        s += "\ttemp += c * log(y_in);\n"
        s += "\ttemp += d * pow(log(x_in), 2.0);\n"
        s += "\ttemp += f * pow(log(y_in), 2.0);\n"
        s += "\ttemp += g * pow(log(x_in), 3.0);\n"
        s += "\ttemp += h * pow(log(y_in), 3.0);\n"
        return s



class SimplifiedCubicLogarithmicTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Simplified Cubic Logarithmic"
    _HTML = 'z = a + b*ln(i*x+j) + c*ln(k*y+m) + d*ln(i*x+j)<sup>2</sup> + f*ln(k*y+m)<sup>2</sup> + g*ln(i*x+j)<sup>3</sup> + h*ln(k*y+m)<sup>3</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'm']
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
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]
        j = inCoeffs[8]
        k = inCoeffs[9]
        m = inCoeffs[10]

        try:
            temp = a
            temp += b * numpy.log(i * x_in + j)
            temp += c * numpy.log(k * y_in + m)
            temp += d * numpy.square(numpy.log(i * x_in + j))
            temp += f * numpy.square(numpy.log(k * y_in + m))
            temp += g * numpy.power(numpy.log(i * x_in + j), 3.0)
            temp += h * numpy.power(numpy.log(k * y_in + m), 3.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(i * x_in + j);\n"
        s += "\ttemp += c * log(k * y_in + m);\n"
        s += "\ttemp += d * pow(log(i * x_in + j), 2.0);\n"
        s += "\ttemp += f * pow(log(k * y_in + m), 2.0);\n"
        s += "\ttemp += g * pow(log(i * x_in + j), 3.0);\n"
        s += "\ttemp += h * pow(log(k * y_in + m), 3.0);\n"
        return s



class SimplifiedQuadraticLogarithmic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Quadratic Logarithmic"
    _HTML = 'z = a + b*ln(x) + c*ln(y) + d*ln(x)<sup>2</sup> + f*ln(y)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowLogY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        LogY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        PowLogX2 = inDataCacheDictionary['PowLogX_2.0'] # only need to perform this dictionary look-up once
        PowLogY2 = inDataCacheDictionary['PowLogY_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a
            temp += b * LogX
            temp += c * LogY
            temp += d * PowLogX2
            temp += f * PowLogY2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(x_in);\n"
        s += "\ttemp += c * log(y_in);\n"
        s += "\ttemp += d * pow(log(x_in), 2.0);\n"
        s += "\ttemp += f * pow(log(y_in), 2.0);\n"
        return s



class SimplifiedQuadraticLogarithmicTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Simplified Quadratic Logarithmic"
    _HTML = 'z = a + b*ln(g*x+h) + c*ln(i*y+j) + d*ln(g*x+h)<sup>2</sup> + f*ln(i*y+j)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']
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
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]
        j = inCoeffs[8]

        try:
            temp = a
            temp += b * numpy.log(g * x_in + h)
            temp += c * numpy.log(i * y_in + j)
            temp += d * numpy.square(numpy.log(g * x_in + h))
            temp += f * numpy.square(numpy.log(i * y_in + j))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * log(g * x_in + h);\n"
        s += "\ttemp += c * log(i * y_in + j);\n"
        s += "\ttemp += d * pow(log(g * x_in + h), 2.0);\n"
        s += "\ttemp += f * pow(log(i * y_in + j), 2.0);\n"
        return s



