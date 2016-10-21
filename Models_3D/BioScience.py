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


class ChenClayton(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Chen-Clayton"
    _HTML = 'r.h.(T<sub>k</sub>,M) = exp(-(C1/T<sup>C2</sup>) * exp(-C3*T<sup>C4</sup>*M))'
    _leftSideHTML = 'r.h.(T<sub>k</sub>,M)'
    _coefficientDesignators = ['C1', 'C2', 'C3', 'C4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]
        C4 = inCoeffs[3]

        try:
            temp = numpy.exp(-1.0 * (C1/numpy.power(x_in,C2)) * numpy.exp(-1.0 * C3 * numpy.power(x_in, C4) * y_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * (C1/pow(x_in,C2)) * exp(-1.0 * C3 * pow(x_in, C4) * y_in));\n"
        return s



class ChenClayton_scaled(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Chen-Clayton Scaled"
    _HTML = 'z = Scale * exp(-(C1/T<sup>C2</sup>) * exp(-C3*T<sup>C4</sup>*M))'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['C1', 'C2', 'C3', 'C4', 'Scale']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]
        C4 = inCoeffs[3]
        scale = inCoeffs[4]

        try:
            temp = scale * numpy.exp(-1.0 * (C1/numpy.power(x_in,C2)) * numpy.exp(-1.0 * C3 * numpy.power(x_in, C4) * y_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * exp(-1.0 * (C1/pow(x_in,C2)) * exp(-1.0 * C3 * pow(x_in, C4) * y_in));\n"
        return s



class HighLowAffinityDoubleIsotopeDisplacement(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "High-Low Affinity Double Isotope Displacement (y = [Hot])"
    _HTML = 'z = aby / (1+b(x+y)) + cdy / (1+d(x+y))'
    _leftSideHTML = 'z'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XPLUSY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        x_plus_y = inDataCacheDictionary['XPLUSY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = (a * b * y_in) / (1.0 + b * x_plus_y) + (c * d * y_in) / (1.0 + d * x_plus_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * b * y_in) / (1.0 + b * (x_in + y_in)) + (c * d * y_in) / (1.0 + d * (x_in + y_in));\n"
        return s



class HighLowAffinityIsotopeDisplacement(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "High-Low Affinity Isotope Displacement (y = [Hot])"
    _HTML = 'z = aby / (1+b(x+y))'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XPLUSY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        x_plus_y = inDataCacheDictionary['XPLUSY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (a * b * y_in) / (1.0 + b * x_plus_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * b * y_in) / (1.0 + b * (x_in + y_in));\n"
        return s



class LogisticGrowth(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Logistic Growth"
    _HTML = 'z = a / (1 + exp(-(b + cx + dy + fxy))) + g'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['a', 'b', 'c', 'd', 'f', 'g']
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        xtimesy = inDataCacheDictionary['XY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]
        f = inCoeffs[4]
        g = inCoeffs[5]

        try:
            temp = a / (1.0 + numpy.exp(-1.0 * (b + c * x_in + d * y_in + f * xtimesy))) + g
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a / (1.0 + exp(-1.0 * (b + c * x_in + d * y_in + f * x_in * y_in))) + g;\n"
        return s



class MichaelisMentenDoubleIsotopeDisplacement(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Michaelis-Menten Double Isotope Displacement (y = [Hot])"
    _HTML = 'z = ay / (b + x + y) + cy / (d + x + y)'
    _leftSideHTML = 'z'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XPLUSY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        x_plus_y = inDataCacheDictionary['XPLUSY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]
        c = inCoeffs[2]
        d = inCoeffs[3]

        try:
            temp = (a * y_in) / (b + x_plus_y) + (c * y_in) / (d + x_plus_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * y_in) / (b + x_in + y_in) + (c * y_in) / (d + x_in + y_in);\n"
        return s



class MichaelisMentenIsotopeDisplacement(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Michaelis-Menten Isotope Displacement (y = [Hot])"
    _HTML = 'z = ay / (b + x + y)'
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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XPLUSY(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        x_plus_y = inDataCacheDictionary['XPLUSY'] # only need to perform this dictionary look-up once
        
        a = inCoeffs[0]
        b = inCoeffs[1]

        try:
            temp = (a * y_in) / (b + x_plus_y)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = (a * y_in) / (b + x_in + y_in);\n"
        return s



class ModifiedChungPfost(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Modified Chung-Pfost"
    _HTML = 'r.h.(T,M) = exp(-(C1/(T+C2)) * exp(-C3*M))'
    _leftSideHTML = 'r.h.(T,M)'
    _coefficientDesignators = ['C1', 'C2', 'C3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]

        try:
            temp = numpy.exp(-1.0 * (C1/(x_in+C2)) * numpy.exp(-1.0 * C3 * y_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * (C1/(x_in+C2)) * exp(-1.0 * C3 * y_in));\n"
        return s



class ModifiedHalsey(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Modified Halsey"
    _HTML = 'r.h.(T,M) = exp(-exp(C1 + C2*T) * M<sup>-C3</sup>)'
    _leftSideHTML = 'r.h.(T,M)'
    _coefficientDesignators = ['C1', 'C2', 'C3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]

        try:
            temp = numpy.exp(-1.0 * numpy.exp(C1 + C2*x_in) * numpy.power(y_in, -1.0 * C3))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(-1.0 * exp(C1 + C2*x_in) * pow(y_in, -1.0 * C3));\n"
        return s



class ModifiedHalsey_scaled(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Modified Halsey Scaled"
    _HTML = 'z = Scale * exp(-exp(C1 + C2*T) * M<sup>-C3</sup>)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['C1', 'C2', 'C3', 'Scale']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]
        scale = inCoeffs[3]

        try:
            temp = scale * numpy.exp(-1.0 * numpy.exp(C1 + C2*x_in) * numpy.power(y_in, -1.0 * C3))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = Scale * exp(-1.0 * exp(C1 + C2*x_in) * pow(y_in, -1.0 * C3));\n"
        return s



class ModifiedHenderson(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Modified Henderson"
    _HTML = 'r.h.(T,M) = 1 - exp(-C1 * (T + C2) * M<sup>C3</sup>)'
    _leftSideHTML = 'r.h.(T,M)'
    _coefficientDesignators = ['C1', 'C2', 'C3']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
    independentData2CannotContainNegativeFlag = True
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]

        try:
            temp = 1.0 - numpy.exp(-1.0 * C1 * (x_in + C2) * numpy.power(y_in, C3))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = 1.0 - exp(-1.0 * C1 * (x_in + C2) * pow(y_in, C3));\n"
        return s



class StrohmanYoerger(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Strohman-Yoerger"
    _HTML = 'r.h.(P<sub>s</sub>,M) = exp(C1*exp(-C2*M)*ln(P<sub>s</sub>) - C3*exp(-C4*M))'
    _leftSideHTML = 'r.h.(P<sub>s</sub>,M)'
    _coefficientDesignators = ['C1', 'C2', 'C3', 'C4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.cigrjournal.org/index.php/Ejounral/article/download/1039/1032'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.LogX(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_LogX = inDataCacheDictionary['LogX'] # only need to perform this dictionary look-up once
        y_in = inDataCacheDictionary['Y'] # only need to perform this dictionary look-up once
        
        C1 = inCoeffs[0]
        C2 = inCoeffs[1]
        C3 = inCoeffs[2]
        C4 = inCoeffs[3]

        try:
            temp = numpy.exp(C1*numpy.exp(-C2*y_in)*x_LogX - C3*numpy.exp(-C4*y_in))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = exp(C1*exp(-C2*y_in)*log(x_in) - C3*exp(-C4*y_in));\n"
        return s



