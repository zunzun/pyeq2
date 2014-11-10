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


class Lomolino(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lomolino"
    _HTML = 'y = a / (1.0 + b<sup>ln(c/x)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = True
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
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a / (1.0 + numpy.power(b, numpy.log(c/x_in)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + pow(b, log(c/x_in)));\n"
        return s



class BET_Sigmoidal_A(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "BET Sigmoidal A"
    _HTML = 'y = x / (a + bx - (a+b)x<sup>2</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = False
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = x_in / (a + (b * x_in) - ((a + b) * x_PowX2))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = x_in / (a + (b * x_in) - ((a + b) * x_in * x_in));\n"
        return s



class BET_Sigmoidal_B(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "BET Sigmoidal B"
    _HTML = 'y = abx / (1.0 + (b-2.0)x - (b-1.0)x<sup>2</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = False
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a * b * x_in / (1.0 + ((b - 2.0) * x_in) - ((b - 1.0) * x_PowX2))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * b * x_in / (1.0 + ((b - 2.0) * x_in) - ((b - 1.0) * x_in * x_in));\n"
        return s



class BoltzmannSigmoidA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Boltzmann Sigmoid A"
    _HTML = 'y = (a - b) / (1.0 + exp((x-c)/d)) + b'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = (a - b) / (1.0 + numpy.exp((x_in - c) / d)) + b
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a - b) / (1.0 + exp((x_in - c) / d)) + b;\n"
        return s



class BoltzmannSigmoidB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Boltzmann Sigmoid B"
    _HTML = 'y = (a - b) / (1.0 + exp((x-c)/(dx))) + b'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = (a - b) / (1.0 + numpy.exp((x_in - c) / (d*x_in))) + b
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a - b) / (1.0 + exp((x_in - c) / (d * x_in))) + b;\n"
        return s



class Chapman(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Chapman"
    _HTML = 'y = a * (1.0 - exp(-bx))<sup>c</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.power(1.0 - numpy.exp(-1.0 * b * x_in), c)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * pow(1.0 - exp(-1.0 * b * x_in), c);\n"
        return s



class DonLevinSigmoid(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Don Levin Sigmoid"
    _HTML = 'y = a1 / (1.0 + exp(-(x-b1)/c1)) + a2 / (1.0 + exp(-(x-b2)/c2)) + a3 / (1.0 + exp(-(x-b3)/c3))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a1 = inCoeffs[0]
        b1 = inCoeffs[1]
        c1 = inCoeffs[2]
        a2 = inCoeffs[3]
        b2 = inCoeffs[4]
        c2 = inCoeffs[5]
        a3 = inCoeffs[6]
        b3 = inCoeffs[7]
        c3 = inCoeffs[8]

        try:
            temp = a1 / (1.0 + numpy.exp(-1.0 * (x_in - b1) / c1)) + a2 / (1.0 + numpy.exp(-1.0 * (x_in - b2) / c2)) + a3 / (1.0 + numpy.exp(-1.0 * (x_in - b3) / c3))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a1 / (1.0 + exp(-1.0 * (x_in - b1) / c1)) + a2 / (1.0 + exp(-1.0 * (x_in - b2) / c2)) + a3 / (1.0 + exp(-1.0 * (x_in - b3) / c3));\n"
        return s



class FiveParameterLogistic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Five-Parameter Logistic"
    _HTML = 'y = d + (a-d) / (1.0 + (x/c)<sup>b</sup>)<sup>f</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = d + (a - d) / numpy.power(1.0 + numpy.power(x_in / c, b), f)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = d + (a - d) / pow(1.0 + pow(x_in / c, b), f);\n"
        return s



class FourParameterLogistic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Four-Parameter Logistic"
    _HTML = 'y = d + (a-d) / (1.0 + (x/c)<sup>b</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = d + (a - d) / (1.0 + numpy.power(x_in / c, b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = d + (a - d) / (1.0 + pow(x_in / c, b));\n"
        return s



class GeneralisedLogistic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Generalised Logistic"
    _HTML = 'y = A + C / (1 + T * exp(-B * (x - M)))<sup>1/T</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['A', 'C', 'M', 'B', 'T']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.knowledgerush.com/kr/encyclopedia/Generalised_logistic_curve/'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        C = inCoeffs[1]
        M = inCoeffs[2]
        B = inCoeffs[3]
        T = inCoeffs[4]

        try:
            temp = A + C / numpy.power(1.0 + T * numpy.exp(-1.0 * B * (x_in - M)), 1.0 / T)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + C / pow(1.0 + T * exp(-1.0 * B * (x_in - M)), 1.0 / T);\n"
        return s



class GompertzA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gompertz A"
    _HTML = 'y = a * exp(-exp(b - cx))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.exp(-1.0 * numpy.exp(b - c*x_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * exp(b - c*x_in));\n"
        return s



class GompertzB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gompertz B"
    _HTML = 'y = a * exp(-exp((x-b)/c))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.exp(-1.0 * numpy.exp((x_in - b)/c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * exp((x_in - b)/c));\n"
        return s



class GompertzC(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gompertz C"
    _HTML = 'y = a * exp(b * exp(c * x))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.exp(b * numpy.exp(c*x_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(b * exp(c*x_in));\n"
        return s



class Hill(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Hill"
    _HTML = 'y = ax<sup>b</sup> / (c<sup>b</sup> + x<sup>b</sup>)'
    _leftSideHTML = 'y'
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
    independentData2CannotContainNegativeFlag = False
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)
        
        
    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.power(x_in, b) / (numpy.power(c, b) + numpy.power(x_in, b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * pow(x_in, b) / (pow(c, b) + pow(x_in, b));\n"
        return s



class Janoschek(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Janoschek Growth"
    _HTML = 'w = a - (1.0 - exp(-b * t<sup>c</sup>))'
    _leftSideHTML = 'w'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.uni-leipzig.de/~vetana/growthe.htm'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a - (1.0 - numpy.exp(-1.0 * b * numpy.power(x_in, c)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a - (1.0 - exp(-1.0 * b * pow(x_in, c)));\n"
        return s



class Janoschek_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Janoschek Growth Modified"
    _HTML = 'w = a - (a - w0) * (1.0 - exp(-b * t<sup>c</sup>))'
    _leftSideHTML = 'w'
    _coefficientDesignators = ['a', 'b', 'c', 'w0']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.uni-leipzig.de/~vetana/growthe.htm'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        w0 = inCoeffs[3]

        try:
            temp = a - (1.0 - (a - w0) * numpy.exp(-1.0 * b * numpy.power(x_in, c)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a - (1.0 - (a - w0) * exp(-1.0 * b * pow(x_in, c)));\n"
        return s



class LogisticA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic A"
    _HTML = 'y = a / (1.0 + b*exp(-cx))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.NegX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_NegX = inDataCacheDictionary['NegX'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a / (1.0 + b*numpy.exp(c * x_NegX))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + b*exp(-1.0 * c * x_in));\n"
        return s



class LogisticB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic B"
    _HTML = 'y = a / (1.0 + (x/b)<sup>c</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a / (1.0 + numpy.power(x_in/b, c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + pow(x_in/b, c));\n"
        return s



class MagneticSaturation(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Magnetic Saturation"
    _HTML = 'y = ax * (1.0 + b*exp(cx))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = False
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
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a*x_in * (1.0 + b*numpy.exp(c*x_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a*x_in * (1.0 + b*exp(c*x_in));\n"
        return s



class MorganMercerFlodin(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Morgan-Mercer-Flodin (MMF)"
    _HTML = 'y = (a * b + c * x<sup>d</sup>) / (b + x<sup>d</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = (a * b + c * numpy.power(x_in, d)) / (b + numpy.power(x_in, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * b + c * pow(x_in, d)) / (b + pow(x_in, d));\n"
        return s



class PetersBaskin_YIII(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yIII (6)"
    _HTML = 'K = ln( exp(b2*c1*d1) + exp(b2*d1*x) )<br>yII = b1*x + K/d1<br>L = ln( exp(b2*c1*d1) + exp(b2*c2*d1) )<br>yIII = yII - ln( exp(d2*(b1*c1 + L/d1)) + exp(d2*yII) ) / d2'
    _leftSideHTML = 'yIII'
    _coefficientDesignators = ['b2', 'c1', 'd1', 'b1', 'c2', 'd2']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]
        b1 = inCoeffs[3]
        c2 = inCoeffs[4]
        d2 = inCoeffs[5]

        try:
            K = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*d1*x_in) )
            yII = b1*x_in + K/d1
            L = numpy.log(numpy.exp(b2*c1*d1) + numpy.exp(b2*c2*d1))
            temp = yII - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII)) / d2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        s += '\tdouble K = log( exp(b2*c1*d1) + exp(b2*d1*x_in) );\n'
        s += '\tdouble yII = b1*x_in + K/d1;\n'
        s += '\tdouble L = log( exp(b2*c1*d1) + exp(b2*c2*d1) );\n'
        s += '\ttemp = yII - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2;\n'
        return s



class PetersBaskin_YII(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yII (3)"
    _HTML = 'K = ln( exp(b2*c1*d1) + exp(b2*d1*x) )<br>yII = b1*x + K/d1'
    _leftSideHTML = 'yII'
    _coefficientDesignators = ['b2', 'c1', 'd1', 'b1']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]
        b1 = inCoeffs[3]

        try:
            temp = b1 * x_in + numpy.log(numpy.exp(b2 * c1 * d1) + numpy.exp(b2 * d1 * x_in)) / d1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = b1 * x_in + log(exp(b2 * c1 * d1) + exp(b2 * d1 * x_in)) / d1;\n"
        return s



class PetersBaskin_YIV(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yIV (9)"
    _HTML = 'K = ln( exp(b2*c1*d1) + exp(b2*d1*x) )<br>yII = b1*x + K/d1<br>L = ln( exp(b2*c1*d1) + exp(b2*c2*d1) )<br>yIII = yII - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2<br>yII,0 = ln(exp(b2*c1*d1) + 1.0 ) / d1<br>yIII,0 = yII,0 - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII,0) ) / d2<br>yIV = yIII - yIII,0'
    _leftSideHTML = 'yIV'
    _coefficientDesignators = ['b2', 'c1', 'd1', 'b1', 'c2', 'd2']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]
        b1 = inCoeffs[3]
        c2 = inCoeffs[4]
        d2 = inCoeffs[5]

        try:
            K = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*d1*x_in) )
            yII = b1*x_in + K/d1
            L = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*c2*d1) )
            yIII = yII - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII) ) / d2
            yII_0 = numpy.log( numpy.exp(b2*c1*d1) + 1.0) / d1
            yIII_0 = yII_0 - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII_0) ) / d2
            temp = yIII - yIII_0
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        s += '\tdouble K = log( exp(b2*c1*d1) + exp(b2*d1*x_in) );\n'
        s += '\tdouble yII = b1*x_in + K/d1;\n'
        s += '\tdouble L = log( exp(b2*c1*d1) + exp(b2*c2*d1) );\n'
        s += '\tdouble yIII = yII - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2;\n'
        s += '\tdouble yII_0 = log( exp(b2*c1*d1) + 1.0) / d1;\n'
        s += '\tdouble yIII_0 = yII_0 - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII_0) ) / d2;\n'
        s += '\ttemp = yIII - yIII_0;\n'
        return s



class PetersBaskin_YI(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yI (2)"
    _HTML = 'yI = ln(exp(b2*c1*d1) + exp(b2*d1*x)) / d1'
    _leftSideHTML = 'yI'
    _coefficientDesignators = ['b2', 'c1', 'd1']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]

        try:
            temp = numpy.log(numpy.exp(b2 * c1 * d1) + numpy.exp(b2 * d1 * x_in)) / d1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = log(exp(b2 * c1 * d1) + exp(b2 * d1 * x_in)) / d1;\n"
        return s



class PetersBaskin_YV(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yV (10)"
    _HTML = 'K = ln( exp(b2*c1*d1) + exp(b2*d1*x) )<br>yII = b1*x + K/d1<br>L = ln( exp(b2*c1*d1) + exp(b2*c2*d1) )<br>yIII = yII - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2<br>yII,0 = ln(exp(b2*c1*d1) + 1.0 ) / d1<br>yIII,0 = yII,0 - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII,0) ) / d2<br>yIV = yIII - yIII,0 + q'
    _leftSideHTML = 'yIV'
    _coefficientDesignators = ['b2', 'c1', 'd1', 'b1', 'c2', 'd2', 'q']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]
        b1 = inCoeffs[3]
        c2 = inCoeffs[4]
        d2 = inCoeffs[5]
        q = inCoeffs[6]

        try:
            K = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*d1*x_in) )
            yII = b1*x_in + K/d1
            L = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*c2*d1) )
            yIII = yII - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII) ) / d2
            yII_0 = numpy.log( numpy.exp(b2*c1*d1) + 1.0) / d1
            yIII_0 = yII_0 - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII_0) ) / d2
            temp = yIII - yIII_0 + q
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        s += '\tdouble K = log( exp(b2*c1*d1) + exp(b2*d1*x_in) );\n'
        s += '\tdouble yII = b1*x_in + K/d1;\n'
        s += '\tdouble L = log( exp(b2*c1*d1) + exp(b2*c2*d1) );\n'
        s += '\tdouble yIII = yII - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2;\n'
        s += '\tdouble yII_0 = log( exp(b2*c1*d1) + 1.0) / d1;\n'
        s += '\tdouble yIII_0 = yII_0 - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII_0) ) / d2;\n'
        s += '\ttemp = yIII - yIII_0 + q;\n'
        return s



class PetersBaskin_YV_Scaled(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: yV (10) Scaled"
    _HTML = 'K = ln( exp(b2*c1*d1) + exp(b2*d1*x) )<br>yII = b1*x + K/d1<br>L = ln( exp(b2*c1*d1) + exp(b2*c2*d1) )<br>yIII = yII - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2<br>yII,0 = ln(exp(b2*c1*d1) + 1.0 ) / d1<br>yIII,0 = yII,0 - ln( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII,0) ) / d2<br>yIV = scale * (yIII - yIII,0 )+ q'
    _leftSideHTML = 'yIV'
    _coefficientDesignators = ['b2', 'c1', 'd1', 'b1', 'c2', 'd2', 'q', 'scale']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b2 = inCoeffs[0]
        c1 = inCoeffs[1]
        d1 = inCoeffs[2]
        b1 = inCoeffs[3]
        c2 = inCoeffs[4]
        d2 = inCoeffs[5]
        q = inCoeffs[6]
        scale = inCoeffs[7]

        try:
            K = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*d1*x_in) )
            yII = b1*x_in + K/d1
            L = numpy.log( numpy.exp(b2*c1*d1) + numpy.exp(b2*c2*d1) )
            yIII = yII - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII) ) / d2
            yII_0 = numpy.log( numpy.exp(b2*c1*d1) + 1.0) / d1
            yIII_0 = yII_0 - numpy.log( numpy.exp(d2*(b1*c2 + L/d1)) + numpy.exp(d2*yII_0) ) / d2
            temp = scale * (yIII - yIII_0) + q
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        s += '\tdouble K = log( exp(b2*c1*d1) + exp(b2*d1*x_in) );\n'
        s += '\tdouble yII = b1*x_in + K/d1;\n'
        s += '\tdouble L = log( exp(b2*c1*d1) + exp(b2*c2*d1) );\n'
        s += '\tdouble yIII = yII - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII) ) / d2;\n'
        s += '\tdouble yII_0 = log( exp(b2*c1*d1) + 1.0) / d1;\n'
        s += '\tdouble yIII_0 = yII_0 - log( exp(d2*(b1*c2 + L/d1)) + exp(d2*yII_0) ) / d2;\n'
        s += '\ttemp = scale * (yIII - yIII_0) + q;\n'
        return s



class PetersBaskin_Y(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Peters-Baskin Step-Stool: y (1)"
    _HTML = 'y = ln(c + exp(b*d*x)) / d'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.plantmethods.com/content/2/1/11'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b = inCoeffs[0]
        c = inCoeffs[1]
        d = inCoeffs[2]

        try:
            temp = numpy.log(c + numpy.exp(b * d * x_in)) / d
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = log(c + exp(b * d * x_in)) / d;\n"
        return s



class Richards(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Richards"
    _HTML = 'y = 1.0 / (a + b * e<sup>(c*x)</sup>)<sup>d</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = 1.0 / numpy.power(a + b * numpy.exp(c*x_in), d)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / pow(a + b * exp(c*x_in), d);\n"
        return s



class SigmoidA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sigmoid A"
    _HTML = 'y = 1.0 / (1.0 + exp(-a(x-b)))'
    _leftSideHTML = 'y'
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = 1.0 / (1.0 + numpy.exp(-1.0 * a * (x_in - b)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + exp(-1.0 * a * (x_in - b)));\n"
        return s



class SigmoidA_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sigmoid A Modified"
    _HTML = 'y = 1.0 / (1.0 + exp(-a(x-b)))<sup>c</sup>'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = 1.0 / numpy.power(1.0 + numpy.exp(-1.0 * a * (x_in - b)), c)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / pow(1.0 + exp(-1.0 * a * (x_in - b)), c);\n"
        return s



class SigmoidB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sigmoid B"
    _HTML = 'y = a / (1.0 + exp(-(x-b)/c))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a / (1.0 + numpy.exp(-1.0 * (x_in - b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + exp(-1.0 * (x_in - b) / c));\n"
        return s



class SigmoidB_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Sigmoid B Modified"
    _HTML = 'y = a / (1.0 + exp(-(x-b)/c))<sup>d</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = a / numpy.power(1.0 + numpy.exp(-1.0 * (x_in - b) / c), d)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / pow(1.0 + exp(-1.0 * (x_in - b) / c), d);\n"
        return s



class Weibull(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull"
    _HTML = 'y = a - b*exp(-cx<sup>d</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = True
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = a - b*numpy.exp(-1.0 * c * numpy.power(x_in, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a - b*exp(-1.0 * c * pow(x_in, d));\n"
        return s



class WeibullCDF(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull CDF"
    _HTML = 'y = 1.0 - exp(-(x/b)<sup>a</sup>)'
    _leftSideHTML = 'y'
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = 1.0 - numpy.exp(-1.0 * numpy.power(x_in/b, a))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 - exp(-1.0 * pow(x_in/b, a));\n"
        return s



class WeibullCDF_scaled(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull CDF Scaled"
    _HTML = 'y = Scale * (1.0 - exp(-(x/b)<sup>a</sup>))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'Scale']
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        scale = inCoeffs[2]

        try:
            temp = scale * (1.0 - numpy.exp(-1.0 * numpy.power(x_in/b, a)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * (1.0 - exp(-1.0 * pow(x_in/b, a)));\n"
        return s



class WeibullPDF(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull PDF"
    _HTML = 'y = (a/b) * (x/b)<sup>(a-1.0)</sup> * exp(-(x/b)<sup>a</sup>)'
    _leftSideHTML = 'y'
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

    independentData1CannotContainBothPositiveAndNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (a/b) * numpy.power(x_in/b, a-1.0) * numpy.exp(-1.0 * numpy.power(x_in/b, a))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a/b) * pow(x_in/b, a-1.0) * exp(-1.0 * pow(x_in/b, a));\n"
        return s



