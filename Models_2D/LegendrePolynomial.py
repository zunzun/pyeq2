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


def cppCodeGeneratorForLegendrePolynomials(n, cosineFlag):
    # see http://mathworld.wolfram.com/LegendrePolynomial.html
    if cosineFlag:
        x = 'cos(x_in)'
    else:
        x = 'x_in'

    if n == 0:
        return "1.0"
    elif n == 1:
        return "x_in"
    elif n == 2:
        return "(1.0 / 2.0) * (3.0*pow(" + x + ", 2.0) - 1.0)"
    elif n == 3:
        return "(1.0 / 2.0) * (5.0*pow(" + x + ", 3.0) - 3.0*" + x + ")"
    elif n == 4:
        return "(1.0 / 8.0) * (35.0*pow(" + x + ", 4.0) - 30.0*pow(" + x + ", 2.0) + 3)"
    elif n == 5:
        return "(1.0 / 8.0) * (63.0*pow(" + x + ", 5.0) - 70.0*pow(" + x + ", 3.0) + 15.0*" + x + ")"
    elif n == 6:
        return "(1.0 / 16.0) * (231.0*pow(" + x + ", 6.0) - 315.0*pow(" + x + ", 4.0) + 105.0*pow(" + x + ", 2.0) - 5)"
    elif n == 7:
        return "(1.0 / 16.0) * (429.0*pow(" + x + ", 7.0) - 693.0*pow(" + x + ", 5.0) + 315.0*pow(" + x + ", 3.0) - 35.0*" + x + ")"
    elif n == 8:
        return "(1.0 / 128.0) * (6435.0*pow(" + x + ", 8.0) - 12012.0*pow(" + x + ", 6.0) + 6930.0*pow(" + x + ", 4.0) - 1260.0*pow(" + x + ", 2.0) + 35.0)"
    elif n == 9:
        return "(1.0 / 128.0) * (12155.0*pow(" + x + ", 9.0) - 25740.0*pow(" + x + ", 7.0) + 18018.0*pow(" + x + ", 5.0) - 4620.0*pow(" + x + ", 3.0) + 315.0*" + x + ")"
    elif n == 10:
        return "(1.0 / 256.0) * (46189.0*pow(" + x + ", 10.0) - 109395.0*pow(" + x + ", 8.0) + 90090.0*pow(" + x + ", 6.0) - 30030.0*pow(" + x + ", 4.0) + 3465.0*pow(" + x + ", 2.0) - 63.0)"
    else:
        raise Exception("Legendre Polynomial Degree of " + str(n) + " is too high, please use a degree of 10 or less.")


class EighthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial G - Eighth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub> + hP<sub>6</sub> + iP<sub>7</sub> + jP<sub>8</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[6, 0]), [6, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[7, 0]), [7, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[8, 0]), [8, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        LegendreX_6 = inDataCacheDictionary['LegendreX_6'] # only need to perform this dictionary look-up once
        LegendreX_7 = inDataCacheDictionary['LegendreX_7'] # only need to perform this dictionary look-up once
        LegendreX_8 = inDataCacheDictionary['LegendreX_8'] # only need to perform this dictionary look-up once
        
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
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            temp += h * LegendreX_6
            temp += i * LegendreX_7
            temp += j * LegendreX_8
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        s += "\ttemp += h * (" + cppCodeGeneratorForLegendrePolynomials(6, 0) + ");\n"
        s += "\ttemp += i * (" + cppCodeGeneratorForLegendrePolynomials(7, 0) + ");\n"
        s += "\ttemp += j * (" + cppCodeGeneratorForLegendrePolynomials(8, 0) + ");\n"
        return s



class FifthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial D - Fifth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        return s



class FourthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial C - Fourth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        return s



class GammaRayAngularDistributionDegreesA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gamma Ray Angular Distribution (degrees) A"
    _HTML = 'y = A0 + A2 * P<sub>2</sub>(cos(theta))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['A0', 'A2']
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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineDegreesX(NameOrValueFlag=1, args=[2, 2]), [2, 2]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LegendreCosineDegreesX_2 = inDataCacheDictionary['LegendreCosineDegreesX_2'] # only need to perform this dictionary look-up once
        
        A0 = inCoeffs[0]
        A2 = inCoeffs[1]

        try:
            temp = A0 + A2 * LegendreCosineDegreesX_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += A0 + A2 * (" + cppCodeGeneratorForLegendrePolynomials(2, 2) + ");\n"
        return s



class GammaRayAngularDistributionDegreesB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gamma Ray Angular Distribution (degrees) B"
    _HTML = 'y = A0 + A2 * P<sub>2</sub>(cos(theta)) + A4 * P<sub>4</sub>(cos(theta))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['A0', 'A2', 'A4']
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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineDegreesX(NameOrValueFlag=1, args=[2, 2]), [2, 2]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineDegreesX(NameOrValueFlag=1, args=[4, 2]), [4, 2]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LegendreCosineDegreesX_2 = inDataCacheDictionary['LegendreCosineDegreesX_2'] # only need to perform this dictionary look-up once
        LegendreCosineDegreesX_4 = inDataCacheDictionary['LegendreCosineDegreesX_4'] # only need to perform this dictionary look-up once
        
        A0 = inCoeffs[0]
        A2 = inCoeffs[1]
        A4 = inCoeffs[2]

        try:
            temp = A0 + A2 * LegendreCosineDegreesX_2 + A4 * LegendreCosineDegreesX_4
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += A0 + A2 * (" + cppCodeGeneratorForLegendrePolynomials(2, 2) + ") + A4 * (" + cppCodeGeneratorForLegendrePolynomials(4, 2) + ");\n"
        return s



class GammaRayAngularDistributionRadiansA(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gamma Ray Angular Distribution (radians) A"
    _HTML = 'y = A0 + A2 * P<sub>2</sub>(cos(theta))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['A0', 'A2']
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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineRadiansX(NameOrValueFlag=1, args=[2, 1]), [2, 1]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LegendreCosineRadiansX_2 = inDataCacheDictionary['LegendreCosineRadiansX_2'] # only need to perform this dictionary look-up once
        
        A0 = inCoeffs[0]
        A2 = inCoeffs[1]

        try:
            temp = A0 + A2 * LegendreCosineRadiansX_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += A0 + A2 * (" + cppCodeGeneratorForLegendrePolynomials(2, 1) + ");\n"
        return s



class GammaRayAngularDistributionRadiansB(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Gamma Ray Angular Distribution (radians) B"
    _HTML = 'y = A0 + A2 * P<sub>2</sub>(cos(theta)) + A4 * P<sub>4</sub>(cos(theta))'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['A0', 'A2', 'A4']
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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineRadiansX(NameOrValueFlag=1, args=[2, 1]), [2, 1]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreCosineRadiansX(NameOrValueFlag=1, args=[4, 1]), [4, 1]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        LegendreCosineRadiansX_2 = inDataCacheDictionary['LegendreCosineRadiansX_2'] # only need to perform this dictionary look-up once
        LegendreCosineRadiansX_4 = inDataCacheDictionary['LegendreCosineRadiansX_4'] # only need to perform this dictionary look-up once
        
        A0 = inCoeffs[0]
        A2 = inCoeffs[1]
        A4 = inCoeffs[2]

        try:
            temp = A0 + A2 * LegendreCosineRadiansX_2 + A4 * LegendreCosineRadiansX_4
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += A0 + A2 * (" + cppCodeGeneratorForLegendrePolynomials(2, 1) + ") + A4 * (" + cppCodeGeneratorForLegendrePolynomials(4, 1) + ");\n"
        return s



class NinthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial H - Ninth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub> + hP<sub>6</sub> + iP<sub>7</sub> + jP<sub>8</sub> + kP<sub>9</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[6, 0]), [6, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[7, 0]), [7, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[8, 0]), [8, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[9, 0]), [9, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        LegendreX_6 = inDataCacheDictionary['LegendreX_6'] # only need to perform this dictionary look-up once
        LegendreX_7 = inDataCacheDictionary['LegendreX_7'] # only need to perform this dictionary look-up once
        LegendreX_8 = inDataCacheDictionary['LegendreX_8'] # only need to perform this dictionary look-up once
        LegendreX_9 = inDataCacheDictionary['LegendreX_9'] # only need to perform this dictionary look-up once
        
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
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            temp += h * LegendreX_6
            temp += i * LegendreX_7
            temp += j * LegendreX_8
            temp += k * LegendreX_9
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        s += "\ttemp += h * (" + cppCodeGeneratorForLegendrePolynomials(6, 0) + ");\n"
        s += "\ttemp += i * (" + cppCodeGeneratorForLegendrePolynomials(7, 0) + ");\n"
        s += "\ttemp += j * (" + cppCodeGeneratorForLegendrePolynomials(8, 0) + ");\n"
        s += "\ttemp += k * (" + cppCodeGeneratorForLegendrePolynomials(9, 0) + ");\n"
        return s



class SecondDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial A - Second Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        return s



class SeventhDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial F - Seventh Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub> + hP<sub>6</sub> + iP<sub>7</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[6, 0]), [6, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[7, 0]), [7, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        LegendreX_6 = inDataCacheDictionary['LegendreX_6'] # only need to perform this dictionary look-up once
        LegendreX_7 = inDataCacheDictionary['LegendreX_7'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]
        i = inCoeffs[7]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            temp += h * LegendreX_6
            temp += i * LegendreX_7
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        s += "\ttemp += h * (" + cppCodeGeneratorForLegendrePolynomials(6, 0) + ");\n"
        s += "\ttemp += i * (" + cppCodeGeneratorForLegendrePolynomials(7, 0) + ");\n"
        return s



class SixthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial E - Sixth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub> + hP<sub>6</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[6, 0]), [6, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        LegendreX_6 = inDataCacheDictionary['LegendreX_6'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]
        h = inCoeffs[6]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            temp += h * LegendreX_6
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        s += "\ttemp += h * (" + cppCodeGeneratorForLegendrePolynomials(6, 0) + ");\n"
        return s



class TenthDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial I - Tenth Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub> + fP<sub>4</sub> + gP<sub>5</sub> + hP<sub>6</sub> + iP<sub>7</sub> + jP<sub>8</sub> + kP<sub>9</sub> + mP<sub>10</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'm']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[4, 0]), [4, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[5, 0]), [5, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[6, 0]), [6, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[7, 0]), [7, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[8, 0]), [8, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[9, 0]), [9, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[10, 0]), [10, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        LegendreX_4 = inDataCacheDictionary['LegendreX_4'] # only need to perform this dictionary look-up once
        LegendreX_5 = inDataCacheDictionary['LegendreX_5'] # only need to perform this dictionary look-up once
        LegendreX_6 = inDataCacheDictionary['LegendreX_6'] # only need to perform this dictionary look-up once
        LegendreX_7 = inDataCacheDictionary['LegendreX_7'] # only need to perform this dictionary look-up once
        LegendreX_8 = inDataCacheDictionary['LegendreX_8'] # only need to perform this dictionary look-up once
        LegendreX_9 = inDataCacheDictionary['LegendreX_9'] # only need to perform this dictionary look-up once
        LegendreX_10 = inDataCacheDictionary['LegendreX_10'] # only need to perform this dictionary look-up once
        
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
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            temp += f * LegendreX_4
            temp += g * LegendreX_5
            temp += h * LegendreX_6
            temp += i * LegendreX_7
            temp += j * LegendreX_8
            temp += k * LegendreX_9
            temp += m * LegendreX_10
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        s += "\ttemp += f * (" + cppCodeGeneratorForLegendrePolynomials(4, 0) + ");\n"
        s += "\ttemp += g * (" + cppCodeGeneratorForLegendrePolynomials(5, 0) + ");\n"
        s += "\ttemp += h * (" + cppCodeGeneratorForLegendrePolynomials(6, 0) + ");\n"
        s += "\ttemp += i * (" + cppCodeGeneratorForLegendrePolynomials(7, 0) + ");\n"
        s += "\ttemp += j * (" + cppCodeGeneratorForLegendrePolynomials(8, 0) + ");\n"
        s += "\ttemp += k * (" + cppCodeGeneratorForLegendrePolynomials(9, 0) + ");\n"
        s += "\ttemp += m * (" + cppCodeGeneratorForLegendrePolynomials(10, 0) + ");\n"
        return s



class ThirdDegreeLegendrePolynomial(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "Legendre Polynomial B - Third Degree"
    _HTML = 'y = a + bx + cP<sub>2</sub> + dP<sub>3</sub>'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = 'http://mathworld.wolfram.com/LegendrePolynomial.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[2, 0]), [2, 0]])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LegendreX(NameOrValueFlag=1, args=[3, 0]), [3, 0]])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        LegendreX_2 = inDataCacheDictionary['LegendreX_2'] # only need to perform this dictionary look-up once
        LegendreX_3 = inDataCacheDictionary['LegendreX_3'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = a + b * x_in
            temp += c * LegendreX_2
            temp += d * LegendreX_3
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s  = "\t// see http://mathworld.wolfram.com/LegendrePolynomial.html\n"
        s += "\ttemp += a + b * x_in;\n"
        s += "\ttemp += c * (" + cppCodeGeneratorForLegendrePolynomials(2, 0) + ");\n"
        s += "\ttemp += d * (" + cppCodeGeneratorForLegendrePolynomials(3, 0) + ");\n"
        return s
