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



class SineX_Plus_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Plus Sine Y [radians]"
    _HTML = 'z = amplitude_x * sin(pi * (x - center_x) / width_x) + amplitude_y * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.sin(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * sin(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class SineX_Times_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Times Sine Y [radians]"
    _HTML = 'z = amplitude * sin(pi * (x - center_x) / width_x) * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.sin(numpy.pi * (x_in - center_x) / width_x) * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * sin(3.14159265358979323846 * (x_in - center_x) / width_x) * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class SineXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine XY [radians]"
    _HTML = 'z = amplitude * sin(pi * (xy - center) / width)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center', 'width']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        xy = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center = inCoeffs[1]
        width = inCoeffs[2]

        try:
            temp = amplitude * numpy.sin(numpy.pi * (xy - center) / width)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * sin(3.14159265358979323846 * ((x_in * y_in) - center) / width);\n"
        return s



class TangentX_Plus_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Plus Tangent Y [radians]"
    _HTML = 'z = amplitude_x * tan(pi * (x - center_x) / width_x) + amplitude_y * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.tan(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * tan(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentX_Times_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Times Tangent Y [radians]"
    _HTML = 'z = amplitude * tan(pi * (x - center_x) / width_x) * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.tan(numpy.pi * (x_in - center_x) / width_x) * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * tan(3.14159265358979323846 * (x_in - center_x) / width_x) * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent XY [radians]"
    _HTML = 'z = amplitude * tan(pi * (xy - center) / width)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center', 'width']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        xy = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center = inCoeffs[1]
        width = inCoeffs[2]

        try:
            temp = amplitude * numpy.tan(numpy.pi * (xy - center) / width)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * tan(3.14159265358979323846 * ((x_in * y_in) - center) / width);\n"
        return s



class CoshX_Plus_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Plus Cosh Y [radians]"
    _HTML = 'z = amplitude_x * cosh(pi * (x - center_x) / width_x) + amplitude_y * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshX_Times_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Times Cosh Y[radians]"
    _HTML = 'z = amplitude * cosh(pi * (x - center_x) / width_x) * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshXY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh XY [radians]"
    _HTML = 'z = amplitude * cosh(pi * (xy - center) / width)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center', 'width']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        xy = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center = inCoeffs[1]
        width = inCoeffs[2]

        try:
            temp = amplitude * numpy.cosh(numpy.pi * (xy - center) / width)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * cosh(3.14159265358979323846 * ((x_in * y_in) - center) / width);\n"
        return s



class RezaCustomOne(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Reza's Custom Equation One [radians]"
    _HTML = 'z = (cos(a*x - b*y) + sin(c*x - d*y))<sup>n</sup> - (cos(f*x - g*y) + sin(h*x- i*y))<sup>n</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'n']
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
        h = inCoeffs[6]
        i = inCoeffs[7]
        n = inCoeffs[8]

        try:
            temp = numpy.power(numpy.cos(a*x_in - b*y_in) + numpy.sin(c*x_in - d*y_in), n)
            temp -= numpy.power(numpy.cos(f*x_in - g*y_in) + numpy.sin(h*x_in - i*y_in), n)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = pow(cos(a*x_in - b*y_in) + sin(c*x_in - d*y_in), n);\n"
        s += "\ttemp -= pow(cos(f*x_in - g*y_in) + sin(h*x_in - i*y_in), n);\n"
        return s



class RezaCustomTwo(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Reza's Custom Equation Two [radians]"
    _HTML = 'z = abs(cos((A*(x+B)) + C*(y+D))) + abs(cos((A*(x+B)) - C*(y+D))) - (sin(E*x+F))<sup>2</sup> - (sin(E*y+G))<sup>2</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
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
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = abs(numpy.cos((A*(x_in+B)) + C*(y_in+D))) + abs(numpy.cos((A*(x_in+B)) - C*(y_in+D))) - numpy.power(numpy.sin(E*x_in+F), 2.0) - numpy.power(numpy.sin(E*y_in+G), 2.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = abs(cos((A*(x_in+B)) + C*(y_in+D))) + abs(cos((A*(x_in+B)) - C*(y_in+D))) - pow(sin(E*x_in+F), 2.0) - pow(sin(E*y_in+G), 2.0);\n"
        return s



class SineX_Plus_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Plus Tangent Y [radians]"
    _HTML = 'z = amplitude_x * sin(pi * (x - center_x) / width_x) + amplitude_y * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.sin(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * sin(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class SineX_Times_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Times Tangent Y [radians]"
    _HTML = 'z = amplitude * sin(pi * (x - center_x) / width_x) * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.sin(numpy.pi * (x_in - center_x) / width_x) * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * sin(3.14159265358979323846 * (x_in - center_x) / width_x) * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentX_Plus_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Plus Sine Y [radians]"
    _HTML = 'z = amplitude_x * tan(pi * (x - center_x) / width_x) + amplitude_y * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.tan(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * tan(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentX_Times_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Times Sine Y [radians]"
    _HTML = 'z = amplitude * tan(pi * (x - center_x) / width_x) * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.tan(numpy.pi * (x_in - center_x) / width_x) * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * tan(3.14159265358979323846 * (x_in - center_x) / width_x) * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshX_Plus_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Plus Sine Y [radians]"
    _HTML = 'z = amplitude_x * cosh(pi * (x - center_x) / width_x) + amplitude_y * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshX_Times_SineY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Times Sine Y [radians]"
    _HTML = 'z = amplitude * cosh(pi * (x - center_x) / width_x) * sin(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) * numpy.sin(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) * sin(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class SineX_Plus_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Plus Cosh Y [radians]"
    _HTML = 'z = amplitude_x * sin(pi * (x - center_x) / width_x) + amplitude_y * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.sin(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * sin(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class SineX_Times_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sine X Times Cosh Y [radians]"
    _HTML = 'z = amplitude * sine(pi * (x - center_x) / width_x) * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.sin(numpy.pi * (x_in - center_x) / width_x) * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * sin(3.14159265358979323846 * (x_in - center_x) / width_x) * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshX_Plus_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Plus Tangent Y [radians]"
    _HTML = 'z = amplitude_x * cosh(pi * (x - center_x) / width_x) + amplitude_y * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class CoshX_Times_TangentY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Cosh X Times Tangent Y [radians]"
    _HTML = 'z = amplitude * cosh(pi * (x - center_x) / width_x) * tan(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.cosh(numpy.pi * (x_in - center_x) / width_x) * numpy.tan(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * cosh(3.14159265358979323846 * (x_in - center_x) / width_x) * tan(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentX_Plus_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Plus Cosh Y [radians]"
    _HTML = 'z = amplitude_x * tan(pi * (x - center_x) / width_x) + amplitude_y * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude_x', 'center_x', 'width_x', 'amplitude_y', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude_x = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        amplitude_y = inCoeffs[3]
        center_y = inCoeffs[4]
        width_y = inCoeffs[5]

        try:
            temp = amplitude_x * numpy.tan(numpy.pi * (x_in - center_x) / width_x) + amplitude_y * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude_x * tan(3.14159265358979323846 * (x_in - center_x) / width_x) + amplitude_y * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



class TangentX_Times_CoshY(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Tangent X Times Cosh Y [radians]"
    _HTML = 'z = amplitude * tan(pi * (x - center_x) / width_x) * cosh(pi * (y - center_y) / width_y)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['amplitude', 'center_x', 'width_x', 'center_y', 'width_y']
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
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName)
        self.lowerCoefficientBounds = [None, None, 0.0, None, 0.0]
        self.extendedVersionHandler.AppendAdditionalCoefficientBounds(self)


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        amplitude = inCoeffs[0]
        center_x = inCoeffs[1]
        width_x = inCoeffs[2]
        center_y = inCoeffs[3]
        width_y = inCoeffs[4]

        try:
            temp = amplitude * numpy.tan(numpy.pi * (x_in - center_x) / width_x) * numpy.cosh(numpy.pi * (y_in - center_y) / width_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = amplitude * tan(3.14159265358979323846 * (x_in - center_x) / width_x) * cosh(3.14159265358979323846 * (y_in - center_y) / width_y);\n"
        return s



