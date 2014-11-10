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


class FullCubicExponential(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Cubic Exponential"
    _HTML = 'z = a + b*exp(x) + c*exp(y) + d*exp(x)<sup>2</sup> + f*exp(y)<sup>2</sup> + g*exp(x)<sup>3</sup> + h*exp(y)<sup>3</sup> + i*exp(x)*exp(y) + j*exp(x)<sup>2</sup>*exp(y) + k*exp(x)*exp(y)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k']
    _canLinearSolverBeUsedForSSQABS = True
    
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX_PowExpY(NameOrValueFlag=1, args=[2.0, 1.0]), [2.0, 1.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX_PowExpY(NameOrValueFlag=1, args=[1.0, 2.0]), [1.0, 2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        PowExpX_2 = inDataCacheDictionary['PowExpX_2.0'] # only need to perform this dictionary look-up once
        PowExpY_2 = inDataCacheDictionary['PowExpY_2.0'] # only need to perform this dictionary look-up once
        PowExpX_3 = inDataCacheDictionary['PowExpX_3.0'] # only need to perform this dictionary look-up once
        PowExpY_3 = inDataCacheDictionary['PowExpY_3.0'] # only need to perform this dictionary look-up once
        ExpX_ExpY = inDataCacheDictionary['ExpX_ExpY'] # only need to perform this dictionary look-up once
        PowExpX_PowExpY_21 = inDataCacheDictionary['PowExpX_PowExpY_2.01.0'] # only need to perform this dictionary look-up once
        PowExpX_PowExpY_12 = inDataCacheDictionary['PowExpX_PowExpY_1.02.0'] # only need to perform this dictionary look-up once
        
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
            temp += b * ExpX
            temp += c * ExpY
            temp += d * PowExpX_2
            temp += f * PowExpY_2
            temp += g * PowExpX_3
            temp += h * PowExpY_3
            temp += i * ExpX_ExpY
            temp += j * PowExpX_PowExpY_21
            temp += k * PowExpX_PowExpY_12
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a;\n"
        s += "\ttemp += b * exp(x_in);\n"
        s += "\ttemp += c * exp(y_in);\n"
        s += "\ttemp += d * pow(exp(x_in), 2.0);\n"
        s += "\ttemp += f * pow(exp(y_in), 2.0);\n"
        s += "\ttemp += g * pow(exp(x_in), 3.0);\n"
        s += "\ttemp += h * pow(exp(y_in), 3.0);\n"
        s += "\ttemp += i * exp(x_in) * exp(y_in);\n"
        s += "\ttemp += j * pow(exp(x_in), 2.0) * exp(y_in);\n"
        s += "\ttemp += k * exp(x_in) * pow(exp(y_in), 2.0);\n"
        return s



class FullCubicExponentialTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Full Cubic Exponential"
    _HTML = 'z = a + b*exp(m*x+n) + c*exp(o*y+p) + d*exp(m*x+n)<sup>2</sup> + f*exp(o*y+p)<sup>2</sup> + g*exp(m*x+n)<sup>3</sup> + h*exp(o*y+p)<sup>3</sup> + i*exp(m*x+n)*exp(o*y+p) + j*exp(m*x+n)<sup>2</sup>*exp(o*y+p) + k*exp(m*x+n)*exp(o*y+p)<sup>2</sup>'
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
            temp += b * numpy.exp(m * x_in + n)
            temp += c * numpy.exp(o * y_in + p)
            temp += d * numpy.square(numpy.exp(m * x_in + n))
            temp += f * numpy.square(numpy.exp(o * y_in + p))
            temp += g * numpy.power(numpy.exp(m * x_in + n), 3.0)
            temp += h * numpy.power(numpy.exp(o * y_in + p), 3.0)
            temp += i * numpy.exp(m * x_in + n) * numpy.exp(o * y_in + p)
            temp += j * numpy.square(numpy.exp(m * x_in + n)) * numpy.exp(o * y_in + p)
            temp += k * numpy.exp(m * x_in + n) * numpy.square(numpy.exp(o * y_in + p))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(m * x_in + n);\n"
        s += "\ttemp += c * exp(o * y_in + p);\n"
        s += "\ttemp += d * pow(exp(m * x_in + n), 2.0);\n"
        s += "\ttemp += f * pow(exp(o * y_in + p), 2.0);\n"
        s += "\ttemp += g * pow(exp(m * x_in + n), 3.0);\n"
        s += "\ttemp += h * pow(exp(o * y_in + p), 3.0);\n"
        s += "\ttemp += i * exp(m * x_in + n) * exp(o * y_in + p);\n"
        s += "\ttemp += j * pow(exp(m * x_in + n), 2.0) * exp(o * y_in + p);\n"
        s += "\ttemp += k * exp(m * x_in + n) * pow(exp(o * y_in + p), 2.0);\n"
        return s



class FullQuadraticExponential(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Quadratic Exponential"
    _HTML = 'z = a + b*exp(x) + c*exp(y) + d*exp(x)<sup>2</sup> + f*exp(y)<sup>2</sup> + g*exp(x)*exp(y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
    _canLinearSolverBeUsedForSSQABS = True
    
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX_ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        PowExpX2 = inDataCacheDictionary['PowExpX_2.0'] # only need to perform this dictionary look-up once
        PowExpY2 = inDataCacheDictionary['PowExpY_2.0'] # only need to perform this dictionary look-up once
        ExpX_ExpY = inDataCacheDictionary['ExpX_ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a
            temp += b * ExpX
            temp += c * ExpY
            temp += d * PowExpX2
            temp += f * PowExpY2
            temp += g * ExpX_ExpY
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(x_in);\n"
        s += "\ttemp += c * exp(y_in);\n"
        s += "\ttemp += d * pow(exp(x_in), 2.0);\n"
        s += "\ttemp += f * pow(exp(y_in), 2.0);\n"
        s += "\ttemp += g * exp(x_in) * exp(y_in);\n"
        return s



class FullQuadraticExponentialTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Full Quadratic Exponential"
    _HTML = 'z = a + b*exp(h*x+i) + c*exp(j*y+k) + d*exp(h*x+i)<sup>2</sup> + e*exp(j*y+k)<sup>2</sup> + f*exp(h*x+i)*exp(j*y+k)'
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
            temp += b * numpy.exp(h * x_in + i)
            temp += c * numpy.exp(j * y_in + k)
            temp += d * numpy.square(numpy.exp(h * x_in + i))
            temp += f * numpy.square(numpy.exp(j * y_in + k))
            temp += g * numpy.exp(h * x_in + i) * numpy.exp(j * y_in + k)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(h * x_in + i);\n"
        s += "\ttemp += c * exp(j * y_in + k);\n"
        s += "\ttemp += d * pow(exp(h * x_in + i), 2.0);\n"
        s += "\ttemp += f * pow(exp(j * y_in + k), 2.0);\n"
        s += "\ttemp += g * exp(h * x_in + i) * exp(j * y_in + k);\n"
        return s



class LinearExponential(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Linear Exponential"
    _HTML = 'z = a + b*exp(x) + c*exp(y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = True
    
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * ExpX + c * ExpY
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b * exp(x_in) + c * exp(y_in);\n"
        return s



class LinearExponentialTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Linear Exponential"
    _HTML = 'z = a + b*exp(d*x+f) + c*exp(g*y+h)'
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
            temp = a + b * numpy.exp(d * x_in + f) + c * numpy.exp(g * y_in + h)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b * exp(d * x_in + f) + c * exp(g * y_in + h);\n"
        return s



class SimplifiedCubicExponential(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Cubic Exponential"
    _HTML = 'z = a + b*exp(x) + c*exp(y) + d*exp(x)<sup>2</sup> + e*exp(y)<sup>2</sup> + f*exp(x)<sup>3</sup> + g*exp(y)<sup>3</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = True
    
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        PowExpX2 = inDataCacheDictionary['PowExpX_2.0'] # only need to perform this dictionary look-up once
        PowExpY2 = inDataCacheDictionary['PowExpY_2.0'] # only need to perform this dictionary look-up once
        PowExpX3 = inDataCacheDictionary['PowExpX_3.0'] # only need to perform this dictionary look-up once
        PowExpY3 = inDataCacheDictionary['PowExpY_3.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a
            temp += b * ExpX
            temp += c * ExpY
            temp += d * PowExpX2
            temp += f * PowExpY2
            temp += g * PowExpX3
            temp += h * PowExpY3
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a;\n"
        s += "\ttemp += b * exp(x_in);\n"
        s += "\ttemp += c * exp(y_in);\n"
        s += "\ttemp += d * pow(exp(x_in), 2.0);\n"
        s += "\ttemp += f * pow(exp(y_in), 2.0);\n"
        s += "\ttemp += g * pow(exp(x_in), 3.0);\n"
        s += "\ttemp += h * pow(exp(y_in), 3.0);\n"
        return s



class SimplifiedCubicExponentialTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Simplified Cubic Exponential"
    _HTML = 'z = a + b*exp(i*x+j) + c*exp(k*y+m) + d*exp(i*x+j)<sup>2</sup> + f*exp(k*y+m)<sup>2</sup> + g*exp(i*x+j)<sup>3</sup> + h*exp(k*y+m)<sup>3</sup>'
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
            temp += b * numpy.exp(i * x_in + j)
            temp += c * numpy.exp(k * y_in + m)
            temp += d * numpy.square(numpy.exp(i * x_in + j))
            temp += f * numpy.square(numpy.exp(k * y_in + m))
            temp += g * numpy.power(numpy.exp(i * x_in + j), 3.0)
            temp += h * numpy.power(numpy.exp(k * y_in + m), 3.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(i * x_in + j);\n"
        s += "\ttemp += c * exp(k * y_in + m);\n"
        s += "\ttemp += d * pow(exp(i * x_in + j), 2.0);\n"
        s += "\ttemp += f * pow(exp(k * y_in + m), 2.0);\n"
        s += "\ttemp += g * pow(exp(i * x_in + j), 3.0);\n"
        s += "\ttemp += h * pow(exp(k * y_in + m), 3.0);\n"
        return s



class SimplifiedQuadraticExponential(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Quadratic Exponential"
    _HTML = 'z = a + b*exp(x) + c*exp(y) + d*exp(x)<sup>2</sup> + f*exp(y)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = True
    
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowExpY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        ExpX = inDataCacheDictionary['ExpX'] # only need to perform this dictionary look-up once
        ExpY = inDataCacheDictionary['ExpY'] # only need to perform this dictionary look-up once
        PowExpX2 = inDataCacheDictionary['PowExpX_2.0'] # only need to perform this dictionary look-up once
        PowExpY2 = inDataCacheDictionary['PowExpY_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a
            temp += b * ExpX
            temp += c * ExpY
            temp += d * PowExpX2
            temp += f * PowExpY2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(x_in);\n"
        s += "\ttemp += c * exp(y_in);\n"
        s += "\ttemp += d * pow(exp(x_in), 2.0);\n"
        s += "\ttemp += f * pow(exp(y_in), 2.0);\n"
        return s



class SimplifiedQuadraticExponentialTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Simplified Quadratic Exponential"
    _HTML = 'z = a + b*exp(g*x+h) + c*exp(i*y+j) + d*exp(g*x+h)<sup>2</sup> + f*exp(i*y+j)<sup>2</sup>'
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
            temp += b * numpy.exp(g * x_in + h)
            temp += c * numpy.exp(i * y_in + j)
            temp += d * numpy.square(numpy.exp(g * x_in + h))
            temp += f * numpy.square(numpy.exp(i * y_in + j))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * exp(g * x_in + h);\n"
        s += "\ttemp += c * exp(i * y_in + j);\n"
        s += "\ttemp += d * pow(exp(g * x_in + h), 2.0);\n"
        s += "\ttemp += f * pow(exp(i * y_in + j), 2.0);\n"
        return s



