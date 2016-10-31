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

import numpy
numpy.seterr(all= 'ignore')

import pyeq2, pyeq2.PolyFunctions, pyeq2.Model_2D_BaseClass


class UserSelectablePolyfunctional(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    userSelectablePolyfunctionalFlag = True
    _baseName = "User-Selectable Polyfunctional"
    _leftSideHTML = 'y'
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inFittingTarget = None, inExtendedVersionName = 'Default', inPolyfunctional2DFlags = [], inPolyfunctionalEquationList_X = []):
        if not inPolyfunctionalEquationList_X:
            self.polyfunctionalEquationList = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_2D()
        else:
            self.polyfunctionalEquationList = inPolyfunctionalEquationList_X
        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
    
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass      
    
        self.polyfunctional2DFlags = inPolyfunctional2DFlags
                
        
    def GetDisplayHTML(self):                
        if not self.polyfunctional2DFlags:
            self._HTML = "y = user-selectable function"
        else:
            self._HTML = 'y = '
            coefficientDesignatorIndex = 0
            cd = self.GetCoefficientDesignators()
            for index in range(len(self.polyfunctional2DFlags)):
                
                if self.polyfunctional2DFlags[index] == 0: # move "offset" to end of HTML
                    continue
                
                self._HTML += '<b>' + cd[coefficientDesignatorIndex] + '(</b> ' + self.polyfunctionalEquationList[self.polyfunctional2DFlags[index]].HTML + ' <b>)</b>'
                coefficientDesignatorIndex += 1
                if (self.polyfunctional2DFlags[index] != self.polyfunctional2DFlags[len(self.polyfunctional2DFlags)-1]) or (0 in self.polyfunctional2DFlags): # not the last one
                    self._HTML += " + "
            if 0 in self.polyfunctional2DFlags:
                self._HTML += "<b>Offset</b>"
            
        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetCoefficientDesignators(self):
        if 0 in self.polyfunctional2DFlags:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctional2DFlags)-1])
            self._coefficientDesignators.append('Offset')
        else:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctional2DFlags)])
        return self._coefficientDesignators
        
    
    def GetDataCacheFunctions(self):
        functionList = []
        for i in self.polyfunctional2DFlags:
            if i == 0:
                continue
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Polyfunctional2D(NameOrValueFlag=1, args=i), i])
        if 0 in self.polyfunctional2DFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Polyfunctional2D(NameOrValueFlag=1, args=0), 0])
        return functionList

    
    def ShouldDataBeRejected(self, unused):
        for i in self.polyfunctional2DFlags:
            self.independentData1CannotContainZeroFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.polyfunctionalEquationList[i].cannotAcceptDataWith_Negative
        return pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.ShouldDataBeRejected(self, unused)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in self.polyfunctional2DFlags:
                if i == 0:
                    continue
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polyfunctional2D_" + str(i) + "']")
                coeffCount += 1
            if 0 in self.polyfunctional2DFlags:
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polyfunctional2D_0']")                
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        count = 0
        cd = self.GetCoefficientDesignators()
        for i in self.polyfunctional2DFlags:
            if i != 0:
                s += "\ttemp += " + cd[count] + " * " + self.polyfunctionalEquationList[i].CPP + ";\n"
                count += 1
        if 0 in self.polyfunctional2DFlags:
            s += "\ttemp += " + cd[count] + ";\n"
                
        return s
