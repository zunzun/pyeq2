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

ln_2 = numpy.log(2.0)
sqr_root_two = numpy.sqrt(2.0)
neg_sqr_root_two = -1.0 * sqr_root_two
sqr_root_two_pi = numpy.sqrt(2.0 * numpy.pi)


class LaplacePeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Laplace Peak"
    _HTML = 'y = a * exp((-1.0 * pow(2.0, 0.5) * abs(x-b))/c)'
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
            temp = a * numpy.exp(neg_sqr_root_two * numpy.abs(x_in-b) / c)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp((-1.0 * pow(2.0, 0.5) * abs(x_in-b)) / c);\n"
        return s



class LaplaceArea(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Laplace Area"
    _HTML = 'y = (a / (pow(2.0, 0.5) * c)) * exp((-1.0 * pow(2.0, 0.5) * abs(x-b))/c)'
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
            temp = (a / (sqr_root_two * c)) * numpy.exp(neg_sqr_root_two * numpy.abs(x_in-b) / c)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (pow(2.0, 0.5) * c)) * exp((-1.0 * pow(2.0, 0.5) * abs(x_in-b)) / c);\n"
        return s



class Hamilton(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Hamilton"
    _HTML = "Vb = Gb * (I/mu)<sup>ln(mu/I)/(B*B)</sup> + (Vb<sub>max</sub> * I)/(I + sigma_b)"
    _leftSideHTML = 'Vb'
    _coefficientDesignators = ['Gb', 'mu', 'B', 'Vbmax', 'sigma_b']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)
    
    
    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once

        Gb = inCoeffs[0]
        mu = inCoeffs[1]
        B = inCoeffs[2]
        Vbmax = inCoeffs[3]
        sigma_b = inCoeffs[4]

        try:
            temp = Gb * numpy.power(x_in / mu, numpy.log(mu/x_in)/(B*B)) + (Vbmax * x_in) / (x_in + sigma_b)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Gb * pow(x_in / mu, log(mu/x_in)/(B*B)) + (Vbmax * x_in) / (x_in + sigma_b);\n"
        return s



class ArnoldCohenLogNormalShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Arnold Cohen Log-Normal Peak Shifted"
    _HTML = 'y = a * (exp(-0.5 * ((ln(x-f)-b)/c)<sup>2</sup>)) / (d * (x-g))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
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
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = (a * numpy.exp(-0.5 * numpy.square((numpy.log(x_in-f)-b) / c))) / (d * (x_in-g))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * exp(-0.5 * pow((log(x_in-f)-b) / c, 2.0))) / (d * (x_in-g));\n"
        return s



class ArnoldCohenTwoParameterLogNormalShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Arnold Cohen Two-Parameter Log-Normal Peak Shifted"
    _HTML = 'y = exp(-0.5 * ((ln(x-d)-b)/c)<sup>2</sup>) / (sqrt(2*pi) * c * (x-f))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['b', 'c', 'd', 'f']
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

    sqrt2pi = numpy.sqrt(2.0 * numpy.pi)
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        b = inCoeffs[0]
        c = inCoeffs[1]
        d = inCoeffs[2]
        f = inCoeffs[3]

        try:
            temp = numpy.exp(-0.5 * numpy.square((numpy.log(x_in-d)-b) / c)) / (self.sqrt2pi * c * (x_in-f))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-0.5 * pow((log(x_in-d)-b) / c, 2.0)) / (2.506628274631000502415765284811  * c * (x_in-f));\n"
        return s



class BoxLucasA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas A"
    _HTML = 'y = a * (1.0 - b<sup>x</sup>)'
    _leftSideHTML = 'y'
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)
        
        
    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a * (1.0 - numpy.power(b, x_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - pow(b, x_in));\n"
        return s



class BoxLucasAShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas A Shifted"
    _HTML = 'y = a * (1.0 - b<sup>x-c</sup>)'
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
            temp = a * (1.0 - numpy.power(b, x_in - c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - pow(b, x_in - c));\n"
        return s



class BoxLucasB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas B"
    _HTML = 'y = a * (1.0 - exp(-bx))'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.NegX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_NegX = inDataCacheDictionary['NegX'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a * (1.0 - numpy.exp(b * x_NegX))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - exp(-1.0 * b * x_in));\n"
        return s



class BoxLucasBShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas B Shifted"
    _HTML = 'y = a * (1.0 - exp(-b(x-c)))'
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
            temp = a * (1.0 - numpy.exp(-1.0 * b * (x_in - c)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (1.0 - exp(-1.0 * b * (x_in - c)));\n"
        return s



class BoxLucasC(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas C"
    _HTML = 'y = (a / (a-b)) * (exp(-bx) - exp(-ax))'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (a / (a-b)) * (numpy.exp(-1.0 * b *x_in) - numpy.exp(-1.0 * a * x_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (a-b)) * (exp(-1.0 * b *x_in) - exp(-1.0 * a * x_in));\n"
        return s



class BoxLucasCShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Box Lucas C shifted"
    _HTML = 'y = (a / (a-b)) * (exp(-b(x-c)) - exp(-a(x-c)))'
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
            temp = (a / (a-b)) * (numpy.exp(-1.0 * b * (x_in-c)) - numpy.exp(-1.0 * a * (x_in-c)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (a-b)) * (exp(-1.0 * b * (x_in-c)) - exp(-1.0 * a * (x_in-c)));\n"
        return s



class ExtremeValuePeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extreme Value Peak"
    _HTML = 'y = a * exp(-exp(-((x-b)/c))-((x-b)/c)+1.0)'
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
            temp = a * numpy.exp(-1.0 * numpy.exp(-1.0 * ((x_in-b)/c))-((x_in-b)/c) + 1.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * exp(-1.0 * ((x_in-b)/c))-((x_in-b)/c) + 1.0);\n"
        return s



class ExtremeValueArea(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extreme Value Area"
    _HTML = 'y = (a/c) * exp(-exp(-((x-b)/c))-((x-b)/c))'
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
            temp = (a/c) * numpy.exp(-1.0 * numpy.exp(-1.0 * ((x_in-b)/c))-((x_in-b)/c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a/c) * exp(-1.0 * exp(-1.0 * ((x_in-b)/c))-((x_in-b)/c));\n"
        return s



class GaussianPeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gaussian Peak"
    _HTML = 'y = a * exp(-0.5 * ((x-b)/c)<sup>2</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.square((x_in-b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((x_in-b) / c, 2.0));\n"
        return s



class GaussianPeak_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gaussian Peak Modified"
    _HTML = 'y = a * exp(-0.5 * ((x-b)/c)<sup>d</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.power((x_in-b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((x_in-b) / c, d));\n"
        return s



class GaussianArea(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gaussian Area"
    _HTML = 'y = (a / (pow(2*pi, 0.5) * c)) * exp(-0.5 * ((x-b)/c)<sup>2</sup>)'
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
            temp = (a / (sqr_root_two_pi * c)) * numpy.exp(-0.5 * numpy.square((x_in-b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a / (pow(2.0 * 3.14159265358979323846, 0.5) * c)) * exp(-0.5 * pow((x_in-b) / c, 2.0));\n"
        return s



class LogNormalA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak A"
    _HTML = 'y = a * exp(-0.5 * ((ln(x)-b)/c)<sup>2</sup>)'
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
    independentData1CannotContainNegativeFlag = True
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a * numpy.exp(-0.5 * numpy.square((x_LogX-b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in)-b) / c, 2.0));\n"
        return s



class LogNormalB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak B"
    _HTML = 'y = a * exp(-0.5 * (ln(x/b)/c)<sup>2</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.square(numpy.log(x_in/b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, 2.0));\n"
        return s



class LogNormalAShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak A Shifted"
    _HTML = 'y = a * exp(-0.5 * ((ln(x-d)-b)/c)<sup>2</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.square((numpy.log(x_in-d)-b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in-d)-b) / c, 2.0));\n"
        return s



class LogNormalBShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak B Shifted"
    _HTML = 'y = a * exp(-0.5 * (ln((x-d/b))/c)<sup>2</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.square(numpy.log((x_in-d)/b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-d)/b) / c, 2.0));\n"
        return s



class LogNormalA_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak A Modified"
    _HTML = 'y = a * exp(-0.5 * ((ln(x)-b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = a * numpy.exp(-0.5 * numpy.power((x_LogX-b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in)-b) / c, d));\n"
        return s



class LogNormalB_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak B Modified"
    _HTML = 'y = a * exp(-0.5 * (ln(x/b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
            temp = a * numpy.exp(-0.5 * numpy.power(numpy.log(x_in/b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, d));\n"
        return s



class LogNormalA_ModifiedShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak A Modified Shifted"
    _HTML = 'y = a * exp(-0.5 * ((ln(x-f)-b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a * numpy.exp(-0.5 * numpy.power((numpy.log(x_in-f)-b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow((log(x_in-f)-b) / c, d));\n"
        return s



class LogNormalB_ModifiedShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal Peak B Modified Shifted"
    _HTML = 'y = a * exp(-0.5 * (ln((x-f)/b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a * numpy.exp(-0.5 * numpy.power(numpy.log((x_in-f)/b)-b / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-f)/b)-b / c, d));\n"
        return s



class LogisticPeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic Peak"
    _HTML = 'y = 4a * exp(-1.0 * (x-b) / c) / (1.0 + exp(-1.0 * (x-b) / c))<sup>2</sup>'
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
            temp = 4.0 * a * numpy.exp(-1.0 * (x_in - b) / c) / numpy.square(1.0 + numpy.exp(-1.0 * (x_in - b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 4.0 * a * exp(-1.0 * (x_in - b) / c) / pow(1.0 + exp(-1.0 * (x_in - b) / c), 2.0);\n"
        return s



class LogisticArea(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Logistic Area"
    _HTML = 'y = a * exp(-1.0 * (x-b) / c) / (c * (1.0 + exp(-1.0 * (x-b) / c))<sup>2</sup>)'
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
            temp = a * numpy.exp(-1.0 * (x_in - b) / c) / (c * numpy.square(1.0 + numpy.exp(-1.0 * (x_in - b) / c)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * (x_in - b) / c) / (c * pow(1.0 + exp(-1.0 * (x_in - b) / c), 2.0));\n"
        return s



class LorentzianModifiedPeakA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak A"
    _HTML = 'y = 1.0 / (1.0 + (x-a)<sup>b</sup>)'
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
            temp = 1.0 / (1.0 + numpy.power(x_in-a, b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow(x_in-a, b));\n"
        return s



class LorentzianModifiedPeakB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak B"
    _HTML = 'y = 1.0 / (a + (x-b)<sup>c</sup>)'
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
            temp = 1.0 / (a + numpy.power(x_in-b, c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow(x_in-b, c));\n"
        return s



class LorentzianModifiedPeakC(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak C"
    _HTML = 'y = a / (b + (x-c)<sup>d</sup>)'
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
            temp = a/ (b + numpy.power(x_in-c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow(x_in-c, d));\n"
        return s



class LorentzianModifiedPeakD(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak D"
    _HTML = 'y = 1.0 / (1.0 + ((x-a)/b)<sup>c</sup>)'
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
            temp = 1.0 / (1.0 + numpy.power((x_in-a) / b, c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow((x_in-a) / b, c));\n"
        return s



class LorentzianModifiedPeakE(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak E"
    _HTML = 'y = 1.0 / (a + ((x-b)/c)<sup>d</sup>)'
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
            temp = 1.0 / (a + numpy.power((x_in-b)/c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow((x_in-b)/c, d));\n"
        return s



class LorentzianModifiedPeakF(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak F"
    _HTML = 'y = a / (b + ((x-c)/d)<sup>f</sup>)'
    _leftSideHTML = 'y'
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a / (b + numpy.power((x_in-c)/d, f))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (b + pow((x_in-c)/d, f));\n"
        return s



class LorentzianModifiedPeakG(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Modified Peak G"
    _HTML = 'y = a / (1.0 + ((x-b)/c)<sup>d</sup>)'
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
            temp = a / (1.0 + numpy.power((x_in-b)/c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + pow((x_in-b)/c, d));\n"
        return s



class LorentzianPeakA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak A"
    _HTML = 'y = 1.0 / (1.0 + (x-a)<sup>2</sup>)'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]

        try:
            temp = 1.0 / (1.0 + numpy.square(x_in-a))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow(x_in-a, 2.0));\n"
        return s



class LorentzianPeakB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak B"
    _HTML = 'y = 1.0 / (a + (x-b)<sup>2</sup>)'
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
            temp = 1.0 / (a + numpy.square(x_in-b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow(x_in-b, 2.0));\n"
        return s



class LorentzianPeakC(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak C"
    _HTML = 'y = a / (b + (x-c)<sup>2</sup>)'
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
            temp = a/ (b + numpy.square(x_in-c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow(x_in-c, 2.0));\n"
        return s



class LorentzianPeakD(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak D"
    _HTML = 'y = 1.0 / (1.0 + ((x-a)/b)<sup>2</sup>)'
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
            temp = 1.0 / (1.0 + numpy.square((x_in-a) / b))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (1.0 + pow((x_in-a) / b, 2.0));\n"
        return s



class LorentzianPeakE(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak E"
    _HTML = 'y = 1.0 / (a + ((x-b)/c)<sup>2</sup>)'
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
            temp = 1.0 / (a + numpy.square((x_in-b)/c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 / (a + pow((x_in-b)/c, 2.0));\n"
        return s



class LorentzianPeakF(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak F"
    _HTML = 'y = a / (b + ((x-c)/d)<sup>2</sup>)'
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
            temp = a/ (b + numpy.square((x_in-c)/d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (b + pow((x_in-c)/d, 2.0));\n"
        return s



class LorentzianPeakG(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Lorentzian Peak G"
    _HTML = 'y = a / (1.0 + ((x-b)/c)<sup>2</sup>)'
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
            temp = a/ (1.0 + numpy.square((x_in-b)/c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a/ (1.0 + pow((x_in-b)/c, 2.0));\n"
        return s



class PseudoVoight(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Pseudo-Voight Peak"
    _HTML = 'y = a * (d * (1/(1+((x-b)/c)<sup>2</sup>)) + (1-d) * exp(-0.5 * ((x-b)/c)<sup>2</sup>))'
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
            temp = numpy.square((x_in-b) / c)
            temp = a * (d * (1.0 / (1.0 + temp)) + (1.0-d) * numpy.exp(-0.5 * temp))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = pow((x_in-b) / c, 2.0);\n"
        s += "\ttemp = a * (d * (1.0 / (1.0 + temp)) + (1.0-d) * exp(-0.5 * temp));\n"
        return s



class PseudoVoight_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Pseudo-Voight Peak Modified"
    _HTML = 'y = a * (d * (1/(1+((x-b)/c)<sup>f</sup>)) + (1-d) * exp(-0.5 * ((x-b)/c)<sup>g</sup>))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
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
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a * (d * (1.0 / (1.0 + numpy.power((x_in-b) / c, f))) + (1.0-d) * numpy.exp(-0.5 * numpy.power((x_in-b) / c, g)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * (d * (1.0 / (1.0 + pow((x_in-b) / c, f))) + (1.0-d) * exp(-0.5 * pow((x_in-b) / c, g)));\n"
        return s



class Pulse(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Pulse Peak"
    _HTML = 'y = 4a * exp(-(x-b)/c) * (1.0 - exp(-(x-b)/c))'
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
            temp1 = numpy.exp(-1.0 * (x_in-b) / c)
            temp = 4.0 * a * temp1 * (1.0 - temp1)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 4.0 * a * exp(-1.0 * (x_in-b) / c) * (1.0 - exp(-1.0 * (x_in-b) / c));\n"
        return s



class WeibullPeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull Peak"
    _HTML = 'y = a * exp(-0.5 * (ln(x/b)/c)<sup>2</sup>)'
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
            temp = a * numpy.exp(-0.5 * numpy.square(numpy.log(x_in/b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, 2.0));\n"
        return s



class WeibullPeakShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull Peak Shifted"
    _HTML = 'y = a * exp(-0.5 * (ln((x-d)/b)/c)<sup>2</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        d = inCoeffs[3]

        try:
            temp = a * numpy.exp(-0.5 * numpy.square(numpy.log((x_in-d)/b) / c))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-d)/b) / c, 2.0));\n"
        return s



class WeibullPeak_Modified(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull Peak Modified"
    _HTML = 'y = a * exp(-0.5 * (ln(x/b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
            temp = a * numpy.exp(-0.5 * numpy.power(numpy.log(x_in/b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log(x_in/b) / c, d));\n"
        return s



class WeibullPeak_ModifiedShifted(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Weibull Peak Modified Shifted"
    _HTML = 'y = a * exp(-0.5 * (ln((x-f)/b)/c)<sup>d</sup>)'
    _leftSideHTML = 'y'
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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a * numpy.exp(-0.5 * numpy.power(numpy.log((x_in-f)/b) / c, d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-0.5 * pow(log((x_in-f)/b) / c, d));\n"
        return s



class LogNormal4Parameter(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Log-Normal 4 Parameter"
    _HTML = 'y = a * exp(-1.0 * (ln(2) * ln((((x-b) * (d<sup>2</sup>-1)) / (c*d)) + 1.0)<sup>2</sup>) / ln(d)<sup>2</sup>)'
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
            temp = a * numpy.exp(-1.0 * numpy.square(ln_2 * numpy.log((((x_in-b) * (numpy.square(d)-1.0)) / (c*d)) + 1.0)) / numpy.square(numpy.log(d)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-1.0 * pow(log(2.0) * log((((x_in-b) * (pow(d, 2.0)-1.0)) / (c*d)) + 1.0), 2.0) / pow(log(d), 2.0));\n"
        return s



class ExtremeValue4ParameterPeak(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Extreme Value 4 Parameter Peak"
    _HTML = 'y = a * exp(-x + b + c - c*d*exp(-1.0 * ((x + c*ln(d) - b) / c)) / (c*d))'
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
            temp = a * numpy.exp(-1.0 * x_in + b + c - c*d*numpy.exp(-1.0 * ((x_in + c*numpy.log(d) - b) / c)) / (c*d))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a * exp(-x_in + b + c - c*d*exp(-1.0 * ((x_in + c*log(d) - b) / c)) / (c*d));\n"
        return s



class UVEDFruitGrowthRate(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate"
    _HTML = 'y = ((t/5)<sup>(a-1)</sup>*(1-t/5)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

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
        self.exampleData = '''
   t        y
0.0     0.00
0.3     0.48
0.6     0.86
0.9     0.99
1.2     1.01
1.5     0.91
1.8     0.85
2.1     0.77
2.4     0.77
2.7     0.41
3.0     0.42
3.3     0.22
3.6     0.23
3.9     0.02
4.2     0.04
4.5     0.00
4.8     0.05
'''


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (numpy.power(x_in/5.0,a-1.0)*numpy.power(1.0-x_in/5.0,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (pow(x_in/5.0,a-1.0)*pow(1.0-x_in/5.0,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s





class UVEDFruitGrowthRateB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate B"
    _HTML = 'y = c * ((t/5)<sup>(a-1)</sup>*(1-t/5)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b','c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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

        try:
            temp = c * (numpy.power(x_in/5.0,a-1.0)*numpy.power(1.0-x_in/5.0,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = c * (pow(x_in/5.0,a-1.0)*pow(1.0-x_in/5.0,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s



class UVEDFruitGrowthRateScaled(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate Scaled"
    _HTML = 'y = ((c*t)<sup>(a-1)</sup>*(1-(c*t)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

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

        try:
            temp = (numpy.power(x_in*c,a-1.0)*numpy.power(1.0-x_in*c,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (pow(x_in*c,a-1.0)*pow(1.0-x_in*c,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s






class UVEDFruitGrowthRateScaledB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate Scaled B"
    _HTML = 'y = d * ((c*t)<sup>(a-1)</sup>*(1-(c*t)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c','d']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = True
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
            temp = d * (numpy.power(x_in*c,a-1.0)*numpy.power(1.0-x_in*c,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = d * (pow(x_in*c,a-1.0)*pow(1.0-x_in*c,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s



class UVEDFruitGrowthRateTransform(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate Transform"
    _HTML = 'y = ((c*t+d)<sup>(a-1)</sup>*(1-(c*t+d)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

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
            temp = (numpy.power(x_in*c+d,a-1.0)*numpy.power(1.0-x_in*c+d,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (pow(x_in*c+d,a-1.0)*pow(1.0-x_in*c+d,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s



class UVEDFruitGrowthRateTransformB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "UVED Fruit Growth Rate Transform B"
    _HTML = 'y = f * ((c*t+d)<sup>(a-1)</sup>*(1-(c*t+d)<sup>(b-1)</sup>)/(((a-1)/(a+b-2))<sup>(a-1)</sup>*((b-1)/(a+b-2))<sup>(b-1)</sup>)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd','f']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://greenlab.cirad.fr/GLUVED/html/P1_Prelim/Math/Math_dynsys_202.html'

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
        f = inCoeffs[4]

        try:
            temp = f * (numpy.power(x_in*c+d,a-1.0)*numpy.power(1.0-x_in*c+d,b-1.0)) / (numpy.power((a-1.0)/(a+b-2.0),a-1.0)*numpy.power((b-1.0)/(a+b-2.0),b-1.0))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = f * (pow(x_in*c+d,a-1.0)*pow(1.0-x_in*c+d,b-1.0)) / (pow((a-1.0)/(a+b-2.0),a-1.0)*pow((b-1.0)/(a+b-2.0),b-1.0));\n"
        return s
