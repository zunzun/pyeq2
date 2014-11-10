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


class FullCubic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Cubic"
    _HTML = 'z = a + bx + cy + dx<sup>2</sup> + fy<sup>2</sup> + gx<sup>3</sup> + hy<sup>3</sup> + ixy + jx<sup>2</sup>y + kxy<sup>2</sup>'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[2.0, 1.0]), [2.0, 1.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[1.0, 2.0]), [1.0, 2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowX_3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        Powy_3 = inDataCacheDictionary['PowY_3.0'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        PowX_PowY_21 = inDataCacheDictionary['PowX_PowY_2.01.0'] # only need to perform this dictionary look-up once
        PowX_PowY_12 = inDataCacheDictionary['PowX_PowY_1.02.0'] # only need to perform this dictionary look-up once
        
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
            temp += b * x_in
            temp += c * y_in
            temp += d * PowX_2
            temp += f * PowY_2
            temp += g * PowX_3
            temp += h * Powy_3
            temp += i * XY
            temp += j * PowX_PowY_21
            temp += k * PowX_PowY_12
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * x_in;\n"
        s += "\ttemp += c * y_in;\n"
        s += "\ttemp += d * pow(x_in, 2.0);\n"
        s += "\ttemp += f * pow(y_in, 2.0);\n"
        s += "\ttemp += g * pow(x_in, 3.0);\n"
        s += "\ttemp += h* pow(y_in, 3.0);\n"
        s += "\ttemp += i * x_in * y_in;\n"
        s += "\ttemp += j * pow(x_in, 2.0) * y_in;\n"
        s += "\ttemp += k * x_in * pow(y_in, 2.0);\n"
        return s



class FullQuadratic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Full Quadratic"
    _HTML = 'z = a + bx + cy + dx<sup>2</sup> + fy<sup>2</sup> + gxy'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        XY = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a
            temp += b * x_in
            temp += c * y_in
            temp += d * PowX_2
            temp += f * PowY_2
            temp += g * XY
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * x_in;\n"
        s += "\ttemp += c * y_in;\n"
        s += "\ttemp += d * pow(x_in, 2.0);\n"
        s += "\ttemp += f * pow(y_in, 2.0);\n"
        s += "\ttemp += g * x_in * y_in;\n"
        return s



class Linear(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Linear"
    _HTML = 'z = a + bx + cy'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * x_in + c * y_in
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a + b * x_in + c * y_in;\n"
        return s



class SimplifiedCubic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Cubic"
    _HTML = 'z = a + bx + cy + dx<sup>2</sup> + fy<sup>2</sup> + gx<sup>3</sup> + hy<sup>3</sup>'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[3.0]), [3.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[3.0]), [3.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        PowX_3 = inDataCacheDictionary['PowX_3.0'] # only need to perform this dictionary look-up once
        Powy_3 = inDataCacheDictionary['PowY_3.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a
            temp += b * x_in
            temp += c * y_in
            temp += d * PowX_2
            temp += f * PowY_2
            temp += g * PowX_3
            temp += h * Powy_3
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * x_in;\n"
        s += "\ttemp += c * y_in;\n"
        s += "\ttemp += d * pow(x_in, 2.0);\n"
        s += "\ttemp += f * pow(y_in, 2.0);\n"
        s += "\ttemp += g * pow(x_in, 3.0);\n"
        s += "\ttemp += h * pow(y_in, 3.0);\n"
        return s



class SimplifiedQuadratic(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Simplified Quadratic"
    _HTML = 'z = a + bx + cy + dx<sup>2</sup> + fy<sup>2</sup>'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX(NameOrValueFlag=1, args=[2.0]), [2.0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.PowY(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        PowX_2 = inDataCacheDictionary['PowX_2.0'] # only need to perform this dictionary look-up once
        PowY_2 = inDataCacheDictionary['PowY_2.0'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a
            temp += b * x_in
            temp += c * y_in
            temp += d * PowX_2
            temp += f * PowY_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a;\n"
        s += "\ttemp += b * x_in;\n"
        s += "\ttemp += c * y_in;\n"
        s += "\ttemp += d * pow(x_in, 2.0);\n"
        s += "\ttemp += f * pow(y_in, 2.0);\n"
        return s



class UserSelectablePolynomial(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    userSelectablePolynomialFlag = True
    _baseName = "User-Selectable Polynomial"
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = True
    autoGenerateGrowthAndDecayForms = True

    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    
    
    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default', inXorder = None, inYorder = None):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass
        self.xPolynomialOrder = inXorder
        self.yPolynomialOrder = inYorder
        self._leftSideHTML = 'z'
    
    
    def GetCoefficientDesignators(self):
        self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:(self.xPolynomialOrder+1) * (self.yPolynomialOrder+1)])
        return self.extendedVersionHandler.AssembleCoefficientDesignators(self)
    
    
    def GetDisplayHTML(self):
        if self.xPolynomialOrder == None:
            self._HTML = "z = user-selectable polynomial"
        else:
            self._HTML = "z = "
            cd = self.GetCoefficientDesignators()
            indexmax = (self.xPolynomialOrder+1) * (self.yPolynomialOrder+1)
            for i in range(self.xPolynomialOrder+1): # 0 - xOrder
                for j in range(self.yPolynomialOrder+1): # 0 - yOrder
                    index = (i*(self.yPolynomialOrder+1))+j
                    if index == 0:
                        self._HTML += cd[index]
                    else:
                        self._HTML += cd[index] + 'x<SUP>' + str(i) + '</SUP>y<SUP>' + str(j) + '</SUP>'
                    if (i+1)*(j+1) != indexmax:
                        self._HTML += ' + '
        return self.extendedVersionHandler.AssembleDisplayHTML(self)

    
    def GetDataCacheFunctions(self):
        functionList = []
        for i in range(self.xPolynomialOrder+1): # 0 to xPolynomialOrder
            for j in range(self.yPolynomialOrder+1): # from 0 to yPolynomialOrder
                functionList.append([pyeq2.DataCache.DataCacheFunctions.PowX_PowY(NameOrValueFlag=1, args=[float(i), float(j)]), [float(i), float(j)]])
        return functionList

    
    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in range(self.xPolynomialOrder+1): # 0 to xPolynomialOrder
                for j in range(self.yPolynomialOrder+1): # 0 to xPolynomialOrder
                    temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['PowX_PowY_" + str(i) + ".0" + str(j) + ".0']")
                    coeffCount += 1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        coeffDesignators = self.GetCoefficientDesignators()
        s = ""
        
        for i in range(self.xPolynomialOrder+1): # 0 - xOrder
            for j in range(self.yPolynomialOrder+1): # 0 - yOrder
                index = (i*(self.yPolynomialOrder+1))+j
                if i == 0 and j == 0:
                    s += "\ttemp += " + coeffDesignators[index] + ";\n"
                elif i == 1 and j == 0:
                    s += "\ttemp += " + coeffDesignators[index] + " * x_in;\n"
                elif i > 1 and j == 0:
                    s += "\ttemp += " + coeffDesignators[index] + " * pow(x_in, " + str(i) + ".0);\n"
                elif i > 1 and j == 1:
                    s += "\ttemp += " + coeffDesignators[index] + " * pow(x_in, " + str(i) + ".0) * y_in;\n"
                elif i == 0 and j == 1:
                    s += "\ttemp += " + coeffDesignators[index] + " * y_in;\n"
                elif i == 0 and j > 1:
                    s += "\ttemp += " + coeffDesignators[index] + " * pow(y_in, " + str(j) + ".0);\n"
                elif i == 1 and j > 1:
                    s += "\ttemp += " + coeffDesignators[index] + " * x_in * pow(y_in, " + str(j) + ".0);\n"
                elif i == 1 and j == 1:
                    s += "\ttemp += " + coeffDesignators[index] + " * x_in * y_in;\n"
                else:
                    s += "\ttemp += " + coeffDesignators[index] + " * pow(x_in, " + str(i) + ".0) * pow(y_in, " + str(j) + ".0);\n"
        return s
