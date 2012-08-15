
#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2012 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them


import pyeq2.Model_3D_BaseClass


class SagForAsphere0(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 0"
    _HTML = 's<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        
        k = inCoeffs[0]
        r = inCoeffs[1]

        try:
            s_sq = XSQPLUSYSQ
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = x_in * x_in + y_in * y_in;\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        return s



class SagForAsphere0_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Sag For Asphere 0"
    _HTML = 's<sup>2</sup> = (ax+b)<sup>2</sup> + (cy+d)<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>)'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        a = inCoeffs[2]
        b = inCoeffs[3]
        c = inCoeffs[4]
        d = inCoeffs[5]

        try:
            s_sq = numpy.power(a*x_in+b, 2.0) + numpy.power(c*y_in+d, 2.0)
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5))
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = pow(a*x_in+b, 2.0) + pow(c*y_in+d, 2.0)\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        return s



class SagForAsphere1(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 1"
    _HTML = 's<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW4_3D(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW4_3D = inDataCacheDictionary['XSQPLUSYSQ_POW4_3D'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]

        try:
            s_sq = XSQPLUSYSQ
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * XSQPLUSYSQ_POW4_3D
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = x_in * x_in + y_in * y_in;\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        return s



class SagForAsphere1_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Sag For Asphere 1"
    _HTML = 's<sup>2</sup> = (ax+b)<sup>2</sup> + (cy+d)<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4', 'a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]
        a = inCoeffs[3]
        b = inCoeffs[4]
        c = inCoeffs[5]
        d = inCoeffs[6]

        try:
            s_sq = numpy.power(a*x_in+b, 2.0) + numpy.power(c*y_in+d, 2.0)
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * numpy.power(s_sq, 4.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = pow(a*x_in+b, 2.0) + pow(c*y_in+d, 2.0)\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        return s



class SagForAsphere2(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 2"
    _HTML = 's<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup> + A6*s<sup>6</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4', 'A6']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW4_3D(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW6_3D(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW4_3D = inDataCacheDictionary['XSQPLUSYSQ_POW4_3D'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW6_3D = inDataCacheDictionary['XSQPLUSYSQ_POW6_3D'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]
        A6 = inCoeffs[3]

        try:
            s_sq = XSQPLUSYSQ
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * XSQPLUSYSQ_POW4_3D + A6 * XSQPLUSYSQ_POW6_3D
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = x_in * x_in + y_in * y_in;\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        s += '\ttemp += A6 * pow(s_sq, 6.0);\n'
        return s



class SagForAsphere2_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Sag For Asphere 2"
    _HTML = 's<sup>2</sup> = (ax+b)<sup>2</sup> + (cy+d)<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup> + A6*s<sup>6</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4', 'A6', 'a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]
        A6 = inCoeffs[3]
        a = inCoeffs[4]
        b = inCoeffs[5]
        c = inCoeffs[6]
        d = inCoeffs[7]

        try:
            s_sq = numpy.power(a*x_in+b, 2.0) + numpy.power(c*y_in+d, 2.0)
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * numpy.power(s_sq, 4.0) + A6 * numpy.power(s_sq, 6.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = pow(a*x_in+b, 2.0) + pow(c*y_in+d, 2.0)\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        s += '\ttemp += A6 * pow(s_sq, 6.0);\n'
        return s



class SagForAsphere3(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Sag For Asphere 3"
    _HTML = 's<sup>2</sup> = x<sup>2</sup> + y<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup> + A6*s<sup>6</sup> + A8*s<sup>8</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4', 'A6', 'A8']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW4_3D(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW6_3D(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.XSQPLUSYSQ_POW8_3D(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        XSQPLUSYSQ = inDataCacheDictionary['XSQPLUSYSQ'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW4_3D = inDataCacheDictionary['XSQPLUSYSQ_POW4_3D'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW6_3D = inDataCacheDictionary['XSQPLUSYSQ_POW6_3D'] # only need to perform this dictionary look-up once
        XSQPLUSYSQ_POW8_3D = inDataCacheDictionary['XSQPLUSYSQ_POW8_3D'] # only need to perform this dictionary look-up once
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]
        A6 = inCoeffs[3]
        A8 = inCoeffs[4]

        try:
            s_sq = XSQPLUSYSQ
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * XSQPLUSYSQ_POW4_3D + A6 * XSQPLUSYSQ_POW6_3D + A8 * XSQPLUSYSQ_POW8_3D
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = x_in * x_in + y_in * y_in;\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        s += '\ttemp += A6 * pow(s_sq, 6.0);\n'
        s += '\ttemp += A8 * pow(s_sq, 8.0);\n'
        return s



class SagForAsphere3_Transform(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    
    _baseName = "Transform Sag For Asphere 3"
    _HTML = 's<sup>2</sup> = (ax+b)<sup>2</sup> + (cy+d)<sup>2</sup><br>'
    _HTML += 'z = (s<sup>2</sup>/r) / (1+(1-(k+1)(s/r)<sup>2</sup>)<sup>1/2</sup>) + A4*s<sup>4</sup> + A6*s<sup>6</sup> + A8*s<sup>8</sup>'
    _leftSideHTML = 'z'
    _coefficientDesignators = ['k', 'r', 'A4', 'A6', 'A8', 'a', 'b', 'c', 'd']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://www.scribd.com/doc/69625472/4/Sag-for-Asphere'

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
        
        
        k = inCoeffs[0]
        r = inCoeffs[1]
        A4 = inCoeffs[2]
        A6 = inCoeffs[3]
        A8 = inCoeffs[4]
        a = inCoeffs[4]
        b = inCoeffs[5]
        c = inCoeffs[6]
        d = inCoeffs[7]

        try:
            s_sq = numpy.power(a*x_in+b, 2.0) + numpy.power(c*y_in+d, 2.0)
            s_over_r = pow(s_sq, 0.5) / r
            temp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5)) + A4 * numpy.power(s_sq, 4.0) + A6 * numpy.power(s_sq, 6.0) + A8 * numpy.power(s_sq, 8.0)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = '\tdouble s_sq = pow(a*x_in+b, 2.0) + pow(c*y_in+d, 2.0)\n'
        s += '\tdouble s_over_r = pow(s_sq, 0.5) / r;\n'
        s += '\ttemp = (s_sq / r) / (1.0 + pow(1.0 - (k + 1.0) * s_over_r * s_over_r, 0.5));\n'
        s += '\ttemp += A4 * pow(s_sq, 4.0);\n'
        s += '\ttemp += A6 * pow(s_sq, 6.0);\n'
        s += '\ttemp += A8 * pow(s_sq, 8.0);\n'
        return s
