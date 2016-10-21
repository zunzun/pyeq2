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


class Cauchy(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "CAUCHY"
    _HTML = 'n = A + B/x<sup>2</sup> + C/x<sup>4</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / x_PowX2 + C / x_PowX4
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / pow(x_in, 2.0) + C / pow(x_in, 4.0);\n"
        return s



class Conrady1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "CONRADY1"
    _HTML = 'n = A + B/x + C/x<sup>3.5</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.5]), [3.5]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX3_5 = inDataCacheDictionary['PowX_3.5'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / x_in + C / x_PowX3_5
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / x_in + C / pow(x_in, 3.5);\n"
        return s



class Conrady2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "CONRADY2"
    _HTML = 'n = A + B/x<sup>2</sup> + C/x<sup>3.5</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.5]), [3.5]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX3_5 = inDataCacheDictionary['PowX_3.5'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / x_PowX2 + C / x_PowX3_5
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / pow(x_in, 2.0) + C / pow(x_in, 3.5);\n"
        return s



class Hartmann1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HARTMANN1"
    _HTML = 'n = A + B/(C - x)'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / (C - x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / (C - x_in);\n"
        return s



class Hartmann2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HARTMANN2"
    _HTML = 'n = A + B/(C - x)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / numpy.square(C - x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / pow(C - x_in, 2.0);\n"
        return s



class Hartmann3a(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HARTMANN3a"
    _HTML = 'n = A + B/(C - x)<sup>1.2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B / numpy.power(C - x_in, 1.2)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / pow(C - x_in, 1.2);\n"
        return s



class Hartmann3b(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HARTMANN3b"
    _HTML = 'n = A/(x - B)<sup>1.2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        
        A = inCoeffs[0]
        B = inCoeffs[1]

        try:
            temp = A / numpy.power(x_in - B, 1.2)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A / pow(x_in - B, 1.2);\n"
        return s



class Hartmann4(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HARTMANN4"
    _HTML = 'n = A + B/(C - x) + D/(E - x)'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B / (C - x_in) + D / (E - x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B / (C - x_in) + D / (E - x_in);\n"
        return s



class Herzberger2X2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGR2X2"
    _HTML = 'n = A + Bx<sup>2</sup> + C / (x<sup>2</sup> - 0.028) + D / (x<sup>2</sup> - 0.028)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B * x_PowX2 + C / (x_PowX2 - 0.028) + D / numpy.square(x_PowX2 - 0.028)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C / (pow(x_in, 2.0) - 0.028) + D / pow(pow(x_in, 2.0) - 0.028, 2.0);\n"
        return s



class Herzberger3X2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGR3X2"
    _HTML = 'n = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D / (x<sup>2</sup> - 0.028) + E / (x<sup>2</sup> - 0.028)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D / (x_PowX2 - 0.028) + E / numpy.square(x_PowX2 - 0.028)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D / (pow(x_in, 2.0) - 0.028) + E / pow(pow(x_in, 2.0) - 0.028, 2.0);\n"
        return s



class Herzberger3X3(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGR3X3"
    _HTML = 'n = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D / (x<sup>2</sup> - 0.028) + E / (x<sup>2</sup> - 0.028)<sup>2</sup> + F / (x<sup>2</sup> - 0.028)<sup>4</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D / (x_PowX2 - 0.028) + E / numpy.square(x_PowX2 - 0.028) + F / numpy.power(x_PowX2 - 0.028, 4.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D / (pow(x_in, 2.0) - 0.028) + E / pow(pow(x_in, 2.0) - 0.028, 2.0) + F / pow(pow(x_in, 2.0) - 0.028, 4.0);\n"
        return s



class Herzberger4X2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGR4X2"
    _HTML = 'n = A + Bx<sup>2</sup> + Cx<sup>4</sup> + Dx<sup>6</sup> + E / (x<sup>2</sup> - 0.028) + F / (x<sup>2</sup> - 0.028)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D * x_PowX6 + E / (x_PowX2- 0.028) + F / numpy.square(x_PowX2 - 0.028)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D * pow(x_in, 6.0) + E / (pow(x_in, 2.0) - 0.028) + F / pow(pow(x_in, 2.0) - 0.028, 2.0);\n"
        return s



class Herzberger5X2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGR5X2"
    _HTML = 'n = A + Bx<sup>2</sup> + Cx<sup>4</sup> + Dx<sup>6</sup> + Ex<sup>8</sup> + F / (x<sup>2</sup> - 0.028) + G / (x<sup>2</sup> - 0.028)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D * x_PowX6 +  + E * x_PowX8 + F / (x_PowX2 - 0.028) + G / numpy.square(x_PowX2 - 0.028)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D * pow(x_in, 6.0) +  + E * pow(x_in, 8.0) + F / (pow(x_in, 2.0) - 0.028) + G / pow(pow(x_in, 2.0) - 0.028, 2.0);\n"
        return s



class HerzbergerJK(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HERZBRGRJK"
    _HTML = 'n = A + Bx<sup>2</sup> + Cx<sup>4</sup> + Dx<sup>6</sup> + E / (x<sup>2</sup> - J) + F / (x<sup>2</sup> - K)<sup>2</sup>'
    _leftSideHTML = 'n'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'K']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        J = inCoeffs[6]
        K = inCoeffs[7]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D * x_PowX6 + E / (x_PowX2 - J) + F / numpy.square(x_PowX2 - K)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D * pow(x_in, 6.0) + E / (pow(x_in, 2.0) - J) + F / pow(pow(x_in, 2.0) - K, 2.0);\n"
        return s



class HoO1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HoO1"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C / (x<sup>2</sup> - D<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B*x_PowX2 + C / (x_PowX2-D*D)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C / (x_in*x_in-D*D);\n"
        return s



class HoO2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "HoO2"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>2</sup> / (x<sup>2</sup> - D<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B*x_PowX2 + C*x_PowX2/(x_PowX2-D*D)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*x_in*x_in/(x_in*x_in-D*D);\n"
        return s



class Kingslake1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "KINGSLAKE1"
    _HTML = 'n<sup>2</sup> = A + B/(x<sup>2</sup>-C<sup>2</sup>) + D/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B/(x_PowX2-C*C) + D/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B/(x_in*x_in-C*C) + D/(x_in*x_in-E*E);\n"
        return s



class Kingslake2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "KINGSLAKE2"
    _HTML = 'n<sup>2</sup> = A + B/(x<sup>2</sup>-C<sup>2</sup>) + D/(x<sup>2</sup>-E<sup>2</sup>) + F/(x<sup>2</sup>-G<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B/(x_PowX2-C*C) + D/(x_PowX2-E*E) + F/(x_PowX2-G*G)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B/(x_in*x_in-C*C) + D/(x_in*x_in-E*E) + F/(x_in*x_in-G*G);\n"
        return s



class Misc01(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "MISC01"
    _HTML = 'n<sup>2</sup> = A + B/(x<sup>2</sup>-C<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B/(x_PowX2-C*C)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B/(x_in*x_in-C*C);\n"
        return s



class Misc02(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "MISC02"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/(x<sup>2</sup>-D<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B*x_PowX2 + C/(x_PowX2-D*D)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C/(x_in*x_in-D*D);\n"
        return s



class Misc03(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "MISC03"
    _HTML = 'n<sup>2</sup> = A + B/x<sup>2</sup> + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = A + B/x_PowX2 + C*x_PowX2/(x_PowX2-D*D)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B/(x_in*x_in) + C*x_in*x_in/(x_in*x_in-D*D);\n"
        return s



class Misc04(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "MISC04"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>2</sup> + Ex<sup>2</sup>/(x<sup>2</sup>-F+(Gx<sup>2</sup>/(x<sup>2</sup>-F)))'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D/x_PowX2 + E*x_PowX2/(x_PowX2-F+(G*x_PowX2/(x_PowX2-F)))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*x_in*x_in*x_in*x_in + D/(x_in*x_in) + E*x_in*x_in/(x_in*x_in-F+(G*x_in*x_in/(x_in*x_in-F)));\n"
        return s



class Schott2X3(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT2X3"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + D/x<sup>4</sup> + E/x<sup>6</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B * x_PowX2 + C / x_PowX2 + D / x_PowX4 + E / x_PowX6
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C / pow(x_in, 2.0) + D / pow(x_in, 4.0) + E / pow(x_in, 6.0);\n"
        return s



class Schott2X4(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT2X4"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + D/x<sup>4</sup> + E/x<sup>6</sup> + F/x<sup>8</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B * x_PowX2 + C / x_PowX2 + D / x_PowX4 + E / x_PowX6 + F / x_PowX8
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C / pow(x_in, 2.0) + D / pow(x_in, 4.0) + E / pow(x_in, 6.0) + F / pow(x_in, 8.0);\n"
        return s



class Schott2X5(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT2X5"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + D/x<sup>4</sup> + E/x<sup>6</sup> + F/x<sup>8</sup> + G/x<sup>10</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[10.0]), [10.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        x_PowX10 = inDataCacheDictionary['PowX_10.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B * x_PowX2 + C / x_PowX2 + D / x_PowX4 + E / x_PowX6 + F / x_PowX8 + G / x_PowX10
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C / pow(x_in, 2.0) + D / pow(x_in, 4.0) + E / pow(x_in, 6.0) + F / pow(x_in, 8.0) + G / pow(x_in, 10.0);\n"
        return s



class Schott2X6(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT2X6"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + D/x<sup>4</sup> + E/x<sup>6</sup> + F/x<sup>8</sup> + G/x<sup>10</sup> + H/x<sup>12</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[10.0]), [10.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[12.0]), [12.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        x_PowX10 = inDataCacheDictionary['PowX_10.0'] # only need to perform this dictionary look-up once
        x_PowX12 = inDataCacheDictionary['PowX_12.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]

        try:
            temp = A + B * x_PowX2 + C / x_PowX2 + D / x_PowX4 + E / x_PowX6 + F / x_PowX8 + G / x_PowX10 + H / x_PowX12
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C / pow(x_in, 2.0) + D / pow(x_in, 4.0) + E / pow(x_in, 6.0) + F / pow(x_in, 8.0) + G / pow(x_in, 10.0) + H / pow(x_in, 12.0);\n"
        return s



class Schott3X3(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT3X3"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>2</sup> + E/x<sup>4</sup> + F/x<sup>6</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D / x_PowX2 + E / x_PowX4 + F / x_PowX6
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D / pow(x_in, 2.0) + E / pow(x_in, 4.0) + F / pow(x_in, 6.0);\n"
        return s



class Schott3X4(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT3X4"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>2</sup> + E/x<sup>4</sup> + F/x<sup>6</sup> + G/x<sup>8</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D / x_PowX2 + E / x_PowX4 + F / x_PowX6 + G / x_PowX8
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D / pow(x_in, 2.0) + E / pow(x_in, 4.0) + F / pow(x_in, 6.0) + G / pow(x_in, 8.0);\n"
        return s



class Schott3X5(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT3X5"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>2</sup> + E/x<sup>4</sup> + F/x<sup>6</sup> + G/x<sup>8</sup> + H/x<sup>10</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[10.0]), [10.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        x_PowX10 = inDataCacheDictionary['PowX_10.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D / x_PowX2 + E / x_PowX4 + F / x_PowX6 + G / x_PowX8 + H / x_PowX10
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D / pow(x_in, 2.0) + E / pow(x_in, 4.0) + F / pow(x_in, 6.0) + G / pow(x_in, 8.0) + H / pow(x_in, 10.0);\n"
        return s



class Schott4X4(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT4X4"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + Dx<sup>6</sup> + E/x<sup>2</sup> + F/x<sup>4</sup> + G/x<sup>6</sup> + H/x<sup>8</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D * x_PowX6 + E / x_PowX2 + F / x_PowX4 + G / x_PowX6 + H / x_PowX8
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D * pow(x_in, 6.0) + E / pow(x_in, 2.0) + F / pow(x_in, 4.0) + G / pow(x_in, 6.0) + H / pow(x_in, 8.0);\n"
        return s



class Schott5X5(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SCHOTT5X5"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + Dx<sup>6</sup> + Ex<sup>8</sup> + F/x<sup>2</sup> + G/x<sup>4</sup> + H/x<sup>6</sup> + J/x<sup>8</sup> + K/x<sup>10</sup>'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[8.0]), [8.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[10.0]), [10.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        x_PowX8 = inDataCacheDictionary['PowX_8.0'] # only need to perform this dictionary look-up once
        x_PowX10 = inDataCacheDictionary['PowX_10.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]
        K = inCoeffs[9]

        try:
            temp = A + B * x_PowX2 + C * x_PowX4 + D * x_PowX6 + E * x_PowX8 + F / x_PowX2 + G / x_PowX4 + H / x_PowX6 + J / x_PowX8 + K / x_PowX10
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B * pow(x_in, 2.0) + C * pow(x_in, 4.0) + D * pow(x_in, 6.0) + E * pow(x_in, 8.0) + F / pow(x_in, 2.0) + G / pow(x_in, 4.0) + H / pow(x_in, 6.0) + J / pow(x_in, 8.0) + K / pow(x_in, 10.0);\n"
        return s



class Sell1TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL1TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> / (x<sup>2</sup> - C<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C);\n"
        return s



class Sell1T(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL1T"
    _HTML = 'n<sup>2</sup> = 1 + Ax<sup>2</sup> / (x<sup>2</sup> - B<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]

        try:
            temp = 1.0 + A*x_PowX2/(x_PowX2-B*B)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + A*x_in*x_in/(x_in*x_in-B*B);\n"
        return s



class Sell2TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL2TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E);\n"
        return s



class Sell2T(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL2T"
    _HTML = 'n<sup>2</sup> = 1 + Ax<sup>2</sup>/(x<sup>2</sup>-B<sup>2</sup>) + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]

        try:
            temp = 1.0 + A*x_PowX2/(x_PowX2-B*B) + C*x_PowX2/(x_PowX2-D*D)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + A*x_in*x_in/(x_in*x_in-B*B) + C*x_in*x_in/(x_in*x_in-D*D);\n"
        return s



class Sell3TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL3TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G);\n"
        return s



class Sell3T(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL3T"
    _HTML = 'n<sup>2</sup> = 1 + Ax<sup>2</sup>/(x<sup>2</sup>-B<sup>2</sup>) + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>) + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = 1.0 + A*x_PowX2/(x_PowX2-B*B) + C*x_PowX2/(x_PowX2-D*D) + E*x_PowX2/(x_PowX2-F*F)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + A*x_in*x_in/(x_in*x_in-B*B) + C*x_in*x_in/(x_in*x_in-D*D) + E*x_in*x_in/(x_in*x_in-F*F);\n"
        return s



class Sell4TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL4TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>) + Hx<sup>2</sup>/(x<sup>2</sup>-J<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G) + H*x_PowX2/(x_PowX2-J*J)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G) + H*x_in*x_in/(x_in*x_in-J*J);\n"
        return s



class Sell4T(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL4T"
    _HTML = 'n<sup>2</sup> = 1 + Ax<sup>2</sup>/(x<sup>2</sup>-B<sup>2</sup>) + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>) + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>) + Gx<sup>2</sup>/(x<sup>2</sup>-H<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]

        try:
            temp = 1.0 + A*x_PowX2/(x_PowX2-B*B) + C*x_PowX2/(x_PowX2-D*D) + E*x_PowX2/(x_PowX2-F*F) + G*x_PowX2/(x_PowX2-H*H)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + A*x_in*x_in/(x_in*x_in-B*B) + C*x_in*x_in/(x_in*x_in-D*D) + E*x_in*x_in/(x_in*x_in-F*F) + G*x_in*x_in/(x_in*x_in-H*H);\n"
        return s



class Sell5TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL5TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>) + Hx<sup>2</sup>/(x<sup>2</sup>-J<sup>2</sup>) + Kx<sup>2</sup>/(x<sup>2</sup>-M<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]
        K = inCoeffs[9]
        M = inCoeffs[10]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G) + H*x_PowX2/(x_PowX2-J*J) + K*x_PowX2/(x_PowX2-M*M)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G) + H*x_in*x_in/(x_in*x_in-J*J) + K*x_in*x_in/(x_in*x_in-M*M);\n"
        return s



class Sell5T(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL5T"
    _HTML = 'n<sup>2</sup> = 1 + Ax<sup>2</sup>/(x<sup>2</sup>-B<sup>2</sup>) + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>) + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>) + Gx<sup>2</sup>/(x<sup>2</sup>-H<sup>2</sup>) + Jx<sup>2</sup>/(x<sup>2</sup>-K<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]
        K = inCoeffs[9]

        try:
            temp = 1.0 + A*x_PowX2/(x_PowX2-B*B) + C*x_PowX2/(x_PowX2-D*D) + E*x_PowX2/(x_PowX2-F*F) + G*x_PowX2/(x_PowX2-H*H) + J*x_PowX2/(x_PowX2-K*K)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 + A*x_in*x_in/(x_in*x_in-B*B) + C*x_in*x_in/(x_in*x_in-D*D) + E*x_in*x_in/(x_in*x_in-F*F) + G*x_in*x_in/(x_in*x_in-H*H) + J*x_in*x_in/(x_in*x_in-K*K);\n"
        return s



class Sell6TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL6TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>) + Hx<sup>2</sup>/(x<sup>2</sup>-J<sup>2</sup>) + Kx<sup>2</sup>/(x<sup>2</sup>-M<sup>2</sup>) + Nx<sup>2</sup>/(x<sup>2</sup>-P<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]
        K = inCoeffs[9]
        M = inCoeffs[10]
        N = inCoeffs[11]
        P = inCoeffs[12]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G) + H*x_PowX2/(x_PowX2-J*J) + K*x_PowX2/(x_PowX2-M*M) + N*x_PowX2/(x_PowX2-P*P)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G) + H*x_in*x_in/(x_in*x_in-J*J) + K*x_in*x_in/(x_in*x_in-M*M) + N*x_in*x_in/(x_in*x_in-P*P);\n"
        return s



class Sell7TA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELL7TA"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>) + Hx<sup>2</sup>/(x<sup>2</sup>-J<sup>2</sup>) + Kx<sup>2</sup>/(x<sup>2</sup>-M<sup>2</sup>) + Nx<sup>2</sup>/(x<sup>2</sup>-P<sup>2</sup>) + Qx<sup>2</sup>/(x<sup>2</sup>-R<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]
        H = inCoeffs[7]
        J = inCoeffs[8]
        K = inCoeffs[9]
        M = inCoeffs[10]
        N = inCoeffs[11]
        P = inCoeffs[12]
        Q = inCoeffs[13]
        R = inCoeffs[14]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G) + H*x_PowX2/(x_PowX2-J*J) + K*x_PowX2/(x_PowX2-M*M) + N*x_PowX2/(x_PowX2-P*P) + Q*x_PowX2/(x_PowX2-R*R)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G) + H*x_in*x_in/(x_in*x_in-J*J) + K*x_in*x_in/(x_in*x_in-M*M) + N*x_in*x_in/(x_in*x_in-P*P) + Q*x_in*x_in/(x_in*x_in-R*R);\n"
        return s



class Sellmod1A(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD1A"
    _HTML = 'n<sup>2</sup> = A + Bx + Cx<sup>2</sup> + D/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_in + C*x_PowX2 + D/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in + C*x_in*x_in + D/(x_in*x_in-E*E);\n"
        return s



class Sellmod1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD1"
    _HTML = 'n<sup>2</sup> = A + Bx + Cx<sup>2</sup> + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_in + C*x_PowX2 + D*x_PowX2/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in + C*x_in*x_in + D*x_in*x_in/(x_in*x_in-E*E);\n"
        return s



class Sellmod2A(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD2A"
    _HTML = 'n<sup>2</sup> = A + Bx + Cx<sup>4</sup> + D/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*x_in*x_in*x_in*x_in + D/(x_in*x_in-E*E);\n"
        return s



class Sellmod2(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD2"
    _HTML = 'n<sup>2</sup> = A + Bx + Cx<sup>4</sup> + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D*x_PowX2/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*x_in*x_in*x_in*x_in + D*x_in*x_in/(x_in*x_in-E*E);\n"
        return s



class Sellmod3(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD3"
    _HTML = 'n<sup>2</sup> = (Ax<sup>2</sup>+B)/(x<sup>2</sup>-C<sup>2</sup>) + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = (A*x_PowX2+B)/(x_PowX2-C*C) + D*x_PowX2/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (A*x_in*x_in+B)/(x_in*x_in-C*C) + D*x_in*x_in/(x_in*x_in-E*E);\n"
        return s



class Sellmod4A(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD4A"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + D/(x<sup>2</sup>-E<sup>2</sup>) + F/(x<sup>2</sup>-G<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B*x_PowX2 + C/(x_PowX2) + D/(x_PowX2-E*E) + F/(x_PowX2-G*G)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C/(x_in*x_in) + D/(x_in*x_in-E*E) + F/(x_in*x_in-G*G);\n"
        return s



class Sellmod4(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD4"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + C/x<sup>2</sup> + Dx<sup>2</sup>/(x<sup>2</sup>-E<sup>2</sup>) + Fx<sup>2</sup>/(x<sup>2</sup>-G<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B*x_PowX2 + C/(x_PowX2) + D*x_PowX2/(x_PowX2-E*E) + F*x_PowX2/(x_PowX2-G*G)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C/(x_in*x_in) + D*x_in*x_in/(x_in*x_in-E*E) + F*x_in*x_in/(x_in*x_in-G*G);\n"
        return s



class Sellmod5(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD5"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>2</sup>/(x<sup>2</sup>-D<sup>2</sup>) + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B*x_PowX2 + C*x_PowX2/(x_PowX2-D*D) + E*x_PowX2/(x_PowX2-F*F)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*x_in*x_in/(x_in*x_in-D*D) + E*x_in*x_in/(x_in*x_in-F*F);\n"
        return s



class Sellmod6(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD6"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup>/(x<sup>2</sup>-C<sup>2</sup>) + D/(x<sup>2</sup>-E<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]

        try:
            temp = A + B*x_PowX2/(x_PowX2-C*C) + D/(x_PowX2-E*E)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in/(x_in*x_in-C*C) + D/(x_in*x_in-E*E);\n"
        return s



class Sellmod7A(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD7A"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>6</sup> + E/(x<sup>2</sup>-F<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D/x_PowX6 + E/(x_PowX2-F*F)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*pow(x_in, 4.0) + D/pow(x_in, 6.0) + E/(x_in*x_in-F*F);\n"
        return s



class Sellmod7(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD7"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/x<sup>6</sup> + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D/x_PowX6 + E*x_PowX2/(x_PowX2-F*F)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*pow(x_in, 4.0) + D/pow(x_in, 6.0) + E*x_in*x_in/(x_in*x_in-F*F);\n"
        return s



class Sellmod8(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD8"
    _HTML = 'n<sup>2</sup> = A + Bx<sup>2</sup> + Cx<sup>4</sup> + D/(x<sup>2</sup>-E<sup>2</sup>) + F/(x<sup>2</sup>-G<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]
        G = inCoeffs[6]

        try:
            temp = A + B*x_PowX2 + C*x_PowX4 + D/(x_PowX2-E*E) + F/(x_PowX2-G*G)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B*x_in*x_in + C*pow(x_in, 4.0) + D/(x_in*x_in-E*E) + F/(x_in*x_in-G*G);\n"
        return s



class Sellmod9(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "SELLMOD9"
    _HTML = 'n<sup>2</sup> = A + B/x<sup>2</sup> + C/x<sup>4</sup> + D/x<sup>6</sup> + Ex<sup>2</sup>/(x<sup>2</sup>-F<sup>2</sup>)'
    _leftSideHTML = 'n<sup>2</sup>'
    _coefficientDesignators = ['A', 'B', 'C', 'D', 'E', 'F']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://home.comcast.net/~mbiegert/Blog/DispersionCoefficient/dispeqns.pdf'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[6.0]), [6.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX6 = inDataCacheDictionary['PowX_6.0'] # only need to perform this dictionary look-up once
        
        A = inCoeffs[0]
        B = inCoeffs[1]
        C = inCoeffs[2]
        D = inCoeffs[3]
        E = inCoeffs[4]
        F = inCoeffs[5]

        try:
            temp = A + B/x_PowX2 + C/x_PowX4 + D/x_PowX6 + E*x_PowX2/(x_PowX2-F*F)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = A + B/(x_in*x_in) + C/pow(x_in, 4.0) + D/pow(x_in, 6.0) + E*x_in*x_in/(x_in*x_in-F*F);\n"
        return s



