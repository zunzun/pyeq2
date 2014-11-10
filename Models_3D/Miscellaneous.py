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


class RexKelfkens(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rex Kelfkens' Custom Equation"
    _HTML = 'z =  exp(A+B*ln(x)+C*ln(y))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['A', 'B', 'C']
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
        logX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        logY = inDataCacheDictionary['LogY'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = numpy.exp(A+B*logX+C*logY)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(A+B*log(x_in)+C*log(y_in));\n"
        return s



class RexKelfkensTransform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Rex Kelfkens' Custom Equation Transform"
    _HTML = 'z =  exp(A+B*ln(x * xscale + xoffset)+C*ln(y * yscale + yoffset))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['A', 'B', 'C', 'xscale', 'xoffset', 'yscale', 'yoffset']
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
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        xscale = inCoeffs[3]
        xoffset = inCoeffs[4]
        yscale = inCoeffs[5]
        yoffset = inCoeffs[6]

        try:
            temp = numpy.exp(A+B*numpy.log(x_in * xscale + xoffset)+C*numpy.log(y_in * yscale + yoffset))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(A+B*log(x_in * xscale + xoffset)+C*log(y_in * yscale + yoffset));\n"
        return s



class GaryCler_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gary Cler's Custom Equation Transform"
    _HTML = 'z = a * (dx + f)<sup>b</sup> * (gy + h)<sup>c</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a * numpy.power(d * x_in + f, b) * numpy.power(g * y_in + h, c)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * pow(d * x_in + f, b) * pow(g * y_in + h, c);\n"
        return s



class GaussianCurvatureOfParaboloid(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gaussian Curvature Of Paraboloid"
    _HTML = 'z = 4a<sup>2</sup> / (1 + 4a<sup>2</sup> * (x<sup>2</sup> + y<sup>2</sup>))<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = 4.0 * a * a / numpy.square(1.0 + 4.0 * a * a * XSQPLUSYSQ)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 4.0 * a * a / pow(1.0 + 4.0 * a * a * (x_in * x_in + y_in * y_in), 2.0);\n"
        return s



class GaussianCurvatureOfParaboloid_scaled(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gaussian Curvature Of Paraboloid Scaled"
    _HTML = 'z = Scale * 4a<sup>2</sup> / (1 + 4a<sup>2</sup> * (x<sup>2</sup> + y<sup>2</sup>))<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'Scale']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        scale = inCoeffs[1]

        try:
            temp = scale * 4.0 * a * a / numpy.square(1.0 + 4.0 * a * a * XSQPLUSYSQ)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * 4.0 * a * a / pow(1.0 + 4.0 * a * a * (x_in * x_in + y_in * y_in), 2.0);\n"
        return s



class GaussianCurvatureOfRichmondsMinimalSurface(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gaussian Curvature Of Richmond's Minimal Surface"
    _HTML = 'z = -1.0 * a * (x<sup>2</sup> + y<sup>2</sup>)<sup>3</sup> / (b + (x<sup>2</sup> + y<sup>2</sup>)<sup>2</sup>)<sup>4</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = -1.0 * a * numpy.power(XSQPLUSYSQ, 3.0) / numpy.power(b + numpy.square(XSQPLUSYSQ), 4.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = -1.0 * a * pow(x_in * x_in + y_in * y_in, 3.0) / pow(b + pow(x_in * x_in + y_in * y_in, 2.0), 4.0);\n"
        return s



class GaussianCurvatureOfWhitneysUmbrellaA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gaussian Curvature Of Whitney's Umbrella A"
    _HTML = 'z = -1.0 * a * y<sup>2</sup> / (x<sup>2</sup> + a * (y<sup>2</sup> + y<sup>4</sup>))<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowY4 = inDataCacheDictionary['PowY_4.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = -1.0 * a * PowY2 / numpy.square(PowX2 + a * (PowY2 + PowY4))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = -1.0 * a * y_in * y_in / pow(x_in * x_in + a * (y_in * y_in + pow(y_in, 4.0)), 2.0);\n"
        return s



class GaussianCurvatureOfWhitneysUmbrellaB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Gaussian Curvature Of Whitney's Umbrella B"
    _HTML = 'z = -1.0 * a * x<sup>2</sup> / (y<sup>2</sup> + a * (x<sup>2</sup> + x<sup>4</sup>))<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        PowY2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = -1.0 * a * PowX2 / numpy.square(PowY2 + a * (PowX2 + PowX4))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = -1.0 * a * x_in * x_in / pow(y_in * y_in + a * (x_in * x_in + pow(x_in, 4.0)), 2.0);\n"
        return s



class LipingZheng(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Liping Zheng's core loss coefficients"
    _HTML = 'z = ax<sup>2</sup>y + bx<sup>2</sup>y<sup>2</sup> + cx<sup>1.5</sup>y<sup>1.5</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[2.0, 1.0]), [2.0, 1.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[2.0, 2.0]), [2.0, 2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[1.5, 1.5]), [1.5, 1.5]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        PowX_PowY21 = inDataCacheDictionary['PowX_PowY_2.01.0'] # only need to perform this dictionary look-up once
        PowX_PowY22 = inDataCacheDictionary['PowX_PowY_2.02.0'] # only need to perform this dictionary look-up once
        PowX_PowY15_15 = inDataCacheDictionary['PowX_PowY_1.51.5'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * PowX_PowY21 + b * PowX_PowY22 + c * PowX_PowY15_15
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * x_in * x_in * y_in + b * x_in * x_in * y_in * y_in + c * pow(x_in, 1.5) * pow(y_in, 1.5);\n"
        return s



class MeanCurvatureOfParaboloid(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Mean Curvature Of Paraboloid"
    _HTML = 'z = 2 * (a + 2a<sup>3</sup> * (x<sup>2</sup> + y<sup>2</sup>)) / (1 + 4a<sup>2</sup> * (x<sup>2</sup> + y<sup>2</sup>))<sup>1.5</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = 2.0 * (a + 2.0 * numpy.power(a, 3.0) * XSQPLUSYSQ) / numpy.power(1.0 + 4.0 * a * a * XSQPLUSYSQ, 1.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 2.0 * (a + 2.0 * pow(a, 3.0) * (x_in * x_in + y_in * y_in)) / pow(1.0 + 4.0 * a * a * (x_in * x_in + y_in * y_in), 1.5);\n"
        return s



class MeanCurvatureOfParaboloid_scaled(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Mean Curvature Of Paraboloid Scaled"
    _HTML = 'z = Scale * (a + 2a<sup>3</sup> * (x<sup>2</sup> + y<sup>2</sup>)) / (1 + 4a<sup>2</sup> * (x<sup>2</sup> + y<sup>2</sup>))<sup>1.5</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'Scale']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        scale = inCoeffs[1]

        try:
            temp = scale * (a + 2.0 * numpy.power(a, 3.0) * XSQPLUSYSQ) / numpy.power(1.0 + 4.0 * a * a * XSQPLUSYSQ, 1.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * (a + 2.0 * pow(a, 3.0) * (x_in * x_in + y_in * y_in)) / pow(1.0 + 4.0 * a * a * (x_in * x_in + y_in * y_in), 1.5);\n"
        return s



class MeanCurvatureOfWhitneysUmbrellaA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Mean Curvature Of Whitney's Umbrella A"
    _HTML = 'z = -1.0 * x * (a + b * y<sup>2</sup>) / (x<sup>2</sup> + a * (y<sup>2</sup> + y<sup>4</sup>))<sup>1.5</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowY4 = inDataCacheDictionary['PowY_4.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = -1.0 * x_in * (a + b * PowY2) / numpy.power(PowX2 + a * (PowY2 + PowY4), 1.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = -1.0 * x_in * (a + b * y_in * y_in) / pow(x_in * x_in + a * (y_in * y_in + pow(y_in, 4.0)), 1.5);\n"
        return s



class MeanCurvatureOfWhitneysUmbrellaB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Mean Curvature Of Whitney's Umbrella B"
    _HTML = 'z = -1.0 * y * (a + b * x<sup>2</sup>) / (y<sup>2</sup> + a * (x<sup>2</sup> + x<sup>4</sup>))<sup>1.5</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowY2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = -1.0 * y_in * (a + b * PowX2) / pow(PowY2 + a * (PowX2 + PowX4), 1.5)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = -1.0 * y_in * (a + b * x_in * x_in) / pow(y_in * y_in + a * (x_in * x_in + pow(x_in, 4.0)), 1.5);\n"
        return s



class MennSurfaceA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Menn's Surface A"
    _HTML = 'z = ax<sup>4</sup> + bx<sup>2</sup>y - cy<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowX_4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * PowX_4 + b * PowX_2 * y_in - c * PowY_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * x_in * x_in * x_in * x_in + b * x_in * x_in * y_in - c * y_in * y_in;\n"
        return s



class MennSurfaceB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Menn's Surface B"
    _HTML = 'z = ay<sup>4</sup> + by<sup>2</sup>x - cx<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowY_4 = inDataCacheDictionary['PowY_4.0'] # only need to perform this dictionary look-up once
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * PowY_4 + b * PowY_2 * x_in - c * PowX_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * y_in * y_in * y_in * y_in + b * y_in * y_in * x_in - c * x_in * x_in;\n"
        return s



class MonkeySaddleA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Monkey Saddle A"
    _HTML = 'z = ax<sup>3</sup> - bxy<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        PowX_3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a * PowX_3 - b * x_in * PowY_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * x_in * x_in * x_in - b * x_in * y_in * y_in;\n"
        return s



class MonkeySaddleB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Monkey Saddle B"
    _HTML = 'z = ay<sup>3</sup> - byx<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowY_3 = inDataCacheDictionary['PowY_3.0'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a * PowY_3 - b * y_in * PowX_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * y_in * y_in * y_in - b * y_in * x_in * x_in;\n"
        return s



class MonkeySaddle_TransformA(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Monkey Saddle Transform A"
    _HTML = 'z = a(cx + d)<sup>3</sup> - b(cx + d)(fy + g)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
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
        g = inCoeffs[5]

        try:
            temp = a * numpy.power(c * x_in + d, 3.0) - b * (c * x_in + d) * numpy.square(f * y_in + g)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * pow(c * x_in + d, 3.0) - b * (c * x_in + d) * pow(f * y_in + g, 2.0);\n"
        return s



class MonkeySaddle_TransformB(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Monkey Saddle Transform B"
    _HTML = 'z = a(cy + d)<sup>3</sup> - b(cy + d)(fx + g)<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
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

        try:
            temp = a * numpy.power(c * y_in + d, 3.0) - b * (c * y_in + d) * numpy.square(f * x_in + g)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * pow(c * y_in + d, 3.0) - b * (c * y_in + d) * pow(f * x_in + g, 2.0);\n"
        return s



class Paraboloid(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Paraboloid"
    _HTML = 'z = a * (x<sup>2</sup> + y<sup>2</sup>)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = a * XSQPLUSYSQ
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (x_in * x_in + y_in * y_in);\n"
        return s



class Paraboloid_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Paraboloid Transform"
    _HTML = 'z = a * ((bx + c)<sup>2</sup> + (dy + f)<sup>2</sup>)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
            temp = a * (numpy.square(b * x_in + c) + numpy.square(d * y_in + f))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (pow(b * x_in + c, 2.0) + pow(d * y_in + f, 2.0));\n"
        return s



class PaschensBreakdownFieldStrengthLaw(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Paschen's Law for Breakdown Field Strength"
    _HTML = 'Ebreakdown = pressure * (a / (ln(pressure * distance) + b))'
    _leftSideHTML = 'Ebreakdown'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogXY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LogXY = inDataCacheDictionary['LogXY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = x_in * (a / (LogXY + b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = x_in * (a / (log(x_in * y_in) + b));\n"
        return s



class PaschensBreakdownVoltageLaw(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Paschen's Law for Breakdown Voltage"
    _HTML = 'Vbreakdown = a(pressure * distance) / (ln(pressure * distance) + b)'
    _leftSideHTML = 'Vbreakdown'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogXY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        LogXY = inDataCacheDictionary['LogXY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (a * XY) / (LogXY + b)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * x_in * y_in) / (log(x_in * y_in) + b);\n"
        return s



