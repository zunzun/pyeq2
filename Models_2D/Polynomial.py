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

import pyeq2, pyeq2.PolyFunctions

import numpy
numpy.seterr(all= 'ignore')


import pyeq2.Model_2D_BaseClass


class Quintic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "5th Order (Quintic)"
    _HTML = 'y = a + bx + cx<sup>2</sup> + dx<sup>3</sup> + fx<sup>4</sup> + gx<sup>5</sup>'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[5.0]), [5.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        x_PowX5 = inDataCacheDictionary['PowX_5.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a + b * x_in + c * x_PowX2 + d * x_PowX3 + f * x_PowX4 + g * x_PowX5
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a + b * x_in + c * pow(x_in, 2.0) + d * pow(x_in, 3.0) + f * pow(x_in, 4.0) + g * pow(x_in, 5.0);\n"
        return s



class Quartic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "4th Order (Quartic)"
    _HTML = 'y = a + bx + cx<sup>2</sup> + dx<sup>3</sup> + fx<sup>4</sup>'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[4.0]), [4.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        x_PowX4 = inDataCacheDictionary['PowX_4.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a + b * x_in + c * x_PowX2 + d * x_PowX3 + f * x_PowX4
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a + b * x_in + c * pow(x_in, 2.0) + d * pow(x_in, 3.0) + f * pow(x_in, 4.0);\n"
        return s



class Cubic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "3rd Order (Cubic)"
    _HTML = 'y = a + bx + cx<sup>2</sup> + dx<sup>3</sup>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        x_PowX3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = a + b * x_in + c * x_PowX2 + d * x_PowX3
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a + b * x_in + c * pow(x_in, 2.0) + d * pow(x_in, 3.0);\n"
        return s



class Linear(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "1st Order (Linear)"
    _HTML = 'y = a + bx'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = a + b * x_in
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a + b * x_in;\n"
        return s



class MarcPlanteQuadratic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Marc Plante's Custom Quadratic"
    _HTML = 'y = (-b + (b<sup>2</sup> - 4 a (c - x))<sup>0.5</sup>) / 2 / a '
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
            temp = ((-1.0 * b) + numpy.sqrt((b * b) - 4.0 * a * (c - x_in))) / 2.0 / a
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += ((-1.0 * b) + pow((b * b) - 4.0 * a * (c - x_in), 0.5)) / 2.0 / a;\n"
        return s



class Quadratic(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "2nd Order (Quadratic)"
    _HTML = 'y = a + bx + cx<sup>2</sup>'
    _leftSideHTML = 'y'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        x_PowX2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * x_in + c * x_PowX2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp += a + b * x_in + c * pow(x_in, 2.0);\n"
        return s



class UserSelectablePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    userSelectablePolynomialFlag = True
    _baseName = "User-Selectable Polynomial"
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    
    
    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default', inXorder = None):
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass
        self.xPolynomialOrder = inXorder
        self._leftSideHTML = 'y'
    
    
    def GetCoefficientDesignators(self):
        self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:self.xPolynomialOrder+1])
        return self.extendedVersionHandler.AssembleCoefficientDesignators(self)
    
    
    def GetDisplayHTML(self):
        if self.xPolynomialOrder == None:
            self._HTML = "y = user-selectable polynomial"
        else:
            self._HTML = "y = "
            cd = self.GetCoefficientDesignators()
            for i in range(self.xPolynomialOrder+1): # 0 - xOrder
                if i == 0:
                    self._HTML += cd[i]
                else:
                    self._HTML += cd[i] + 'x<SUP>' + str(i) + '</SUP>'
                if i != self.xPolynomialOrder:
                    self._HTML += ' + '

        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetDataCacheFunctions(self):
        functionList = []
        for i in range(self.xPolynomialOrder+1): # 0 to xPolynomialOrder
            functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[float(i)]), [float(i)]])
        return functionList

    
    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in range(self.xPolynomialOrder+1): # 0 to xPolynomialOrder
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['PowX_" + str(i) + ".0']")
                coeffCount += 1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        coeffDesignators = self.GetCoefficientDesignators()
        s = ""
        
        length = len(self.solvedCoefficients)
        for i in range(length-1, -1, -1):
            if i == length-1:
                s += "\ttemp = " + coeffDesignators[i] + ";\n"
            else:
                s += "\ttemp = temp * x_in + " + coeffDesignators[i] + ";\n"
        return s



class UserCustomizablePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    userCustomizablePolynomialFlag = True
    _baseName = "User-Customizable Polynomial"
    _leftSideHTML = 'y'
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inFittingTarget = None, inExtendedVersionName = 'Default', inPolynomial2DFlags = [], inPolynomialEquationList_X = []):
        if not inPolynomialEquationList_X:
            self.polynomialEquationList = pyeq2.PolyFunctions.GenerateListForCustomPolynomials_2D()
        else:
            self.polynomialEquationList = inPolynomialEquationList_X
        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
    
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass      
    
        self.polynomial2DFlags = inPolynomial2DFlags
                
        
    def GetDisplayHTML(self):                
        if not self.polynomial2DFlags:
            self._HTML = "y = user-customizable polynomial"
        else:
            self._HTML = 'y = '
            cd = self.GetCoefficientDesignators()
            for index in range(len(self.polynomial2DFlags)):
                self._HTML += '<b>' + cd[index] + '(</b> ' + self.polynomialEquationList[self.polynomial2DFlags[index]].HTML + ' <b>)</b>'
                if (self.polynomial2DFlags[index] != self.polynomial2DFlags[len(self.polynomial2DFlags)-1]) or (0 in self.polynomial2DFlags): # not the last one
                    self._HTML += " + "
            
        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetCoefficientDesignators(self):
        self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polynomial2DFlags)])
        return self._coefficientDesignators
        
    
    def GetDataCacheFunctions(self):
        functionList = []
        for i in self.polynomial2DFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Polynomial2D(NameOrValueFlag=1, args=i), i])
        return functionList

    
    def ShouldDataBeRejected(self, unused):
        for i in self.polynomial2DFlags:
            self.independentData1CannotContainZeroFlag |= self.polynomialEquationList[i].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.polynomialEquationList[i].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.polynomialEquationList[i].cannotAcceptDataWith_Negative
        return pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.ShouldDataBeRejected(self, unused)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in self.polynomial2DFlags:
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polynomial2D_" + str(i) + "']")
                coeffCount += 1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        EquationListForPolynomial = pyeq2.PolyFunctions.GenerateListForCustomPolynomials_2D()
        coeffCount = 0
        for i in self.polynomial2DFlags:
            s += "\ttemp += " + self._coefficientDesignators[coeffCount] + " * " + EquationListForPolynomial[i].CPP + ";\n"
            coeffCount += 1
                
        return s
