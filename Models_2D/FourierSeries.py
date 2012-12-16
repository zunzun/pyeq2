from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

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


import pyeq2.Model_2D_BaseClass


class Term1(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    
    _baseName = "1 Term"
    _HTML = 'y = a0 + a1*sin(c1*x)+b1*cos(c1*x)'
    _leftSideHTML = 'y'
    _coefficientDesignators = ['a0', '1a', 'b1', 'c1']
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = 'http://mathworld.wolfram.com/FourierSeries.html'

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
    

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return self.extendedVersionHandler.GetAdditionalDataCacheFunctions(self, functionList)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        x_in = inDataCacheDictionary['X'] # only need to perform this dictionary look-up once
        
        a0 = inCoeffs[0]
        a1 = inCoeffs[1]
        b1 = inCoeffs[2]
        c1 = inCoeffs[3]

        try:
            temp = a0
            temp += a1 *numpy.sin(c1 * x_in) + b1 *numpy.cos(c1 * x_in)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = "\ttemp = a0;\n"
        s += "\ttemp +=  a1 *sin(c1 * x_in) + b1 *cos(c1 * x_in);\n"
        return s
