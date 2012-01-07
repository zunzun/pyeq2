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
#    Version info: $Id$

import sys, os
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2, pyeq2.PolyFunctions

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them


import pyeq2.Model_2D_BaseClass, pyeq2, pyeq2.PolyFunctions


class UserSelectablePolyfunctional(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    UserSelectablePolyfunctionalFlag = True
    _baseName = "User-Selectable Polyfunctional"
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inFittingTarget = None, inExtendedVersionName = 'Default', inPolyfunctionalFlags = [], inPolyfunctionalEquationList = []):
        if not inPolyfunctionalEquationList:
            self.polyfunctionalEquationList = pyeq2.PolyFunctions.GenerateListForPolyfunctionals('unused', 'unused')
        else:
            self.polyfunctionalEquationList = inPolyfunctionalEquationList
        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
    
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass      
    
        self.polyfunctionalFlags = inPolyfunctionalFlags

        self._HTML = "y = user-selectable function"
        self._leftSideHTML = 'y'
        
        
        
    def GetCoefficientDesignators(self):
        if 0 in self.polyfunctionalFlags:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctionalFlags)-1])
            self._coefficientDesignators.append('Offset')
        else:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctionalFlags)])
        return self._coefficientDesignators
        
    
    def GetDataCacheFunctions(self):
        functionList = []
        for i in self.polyfunctionalFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Polyfunctional2D(NameOrValueFlag=1, args=i), i])
        return functionList

    
    def ShouldDataBeRejected(self, unused):
        for i in self.polyfunctionalFlags:
            self.independentData1CannotContainZeroFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Negative
        return pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.ShouldDataBeRejected(self, unused)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in self.polyfunctionalFlags:
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polyfunctional2D_" + str(i) + "']")
                coeffCount += 1
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        count = 0
        EquationListForPolyfunctional = pyeq2.PolyFunctions.GenerateListForPolyfunctionals('x', 'x_in')
        for i in self.polyfunctionalFlags:
            if i != 0:
                s += "\ttemp += " + self._coefficientDesignators[count] + " * " + EquationListForPolyfunctional[i].CPP + ";\n"
                count += 1
        if 0 in self.polyfunctionalFlags:
            s += "\ttemp += " + self._coefficientDesignators[count] + ";\n"
                
        return s
