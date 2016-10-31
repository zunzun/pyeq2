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

import pyeq2, pyeq2.Model_3D_BaseClass, pyeq2.PolyFunctions


class UserSelectablePolyfunctional(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    userSelectablePolyfunctionalFlag = True    
    _baseName = "User-Selectable Polyfunctional"
    _leftSideHTML = 'z'
    _canLinearSolverBeUsedForSSQABS = True
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inFittingTarget = None, inExtendedVersionName = 'Default', inPolyfunctional3DFlags = [], inPolyfunctionalEquationList_X = [], inPolyfunctionalEquationList_Y = []):
        if not inPolyfunctionalEquationList_X:
            self.polyfunctionalEquationList_X = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_3D_X()
            self.polyfunctionalEquationList_Y = pyeq2.PolyFunctions.GenerateListForPolyfunctionals_3D_Y()
        else:
            self.polyfunctionalEquationList_X = inPolyfunctionalEquationList_X
            self.polyfunctionalEquationList_Y = inPolyfunctionalEquationList_Y
        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
    
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass      
    
        self.polyfunctional3DFlags = inPolyfunctional3DFlags
        
        
    def GetDisplayHTML(self):                
        if not self.polyfunctional3DFlags:
            self._HTML = "z = user-selectable function"
        else:
            self._HTML = 'z = '
            coefficientDesignatorIndex = 0
            cd = self.GetCoefficientDesignators()
            for index in range(len(self.polyfunctional3DFlags)):
                
                if self.polyfunctional3DFlags[index] == [0,0]: # move "offset" to end of HTML
                    continue

                if self.polyfunctional3DFlags[index][0] == 0: # no 'X'
                    self._HTML += '<b>' + cd[coefficientDesignatorIndex] + '(</b> ' + self.polyfunctionalEquationList_Y[self.polyfunctional3DFlags[index][1]].HTML + ' <b>)</b>'
                elif self.polyfunctional3DFlags[index][1] == 0: # no 'Y'
                    self._HTML += '<b>' + cd[coefficientDesignatorIndex] + '(</b> ' + self.polyfunctionalEquationList_X[self.polyfunctional3DFlags[index][0]].HTML + ' <b>)</b>'
                else:
                    self._HTML += '<b>' + cd[coefficientDesignatorIndex] + '(</b> ' + self.polyfunctionalEquationList_X[self.polyfunctional3DFlags[index][0]].HTML + ' * ' + self.polyfunctionalEquationList_Y[self.polyfunctional3DFlags[index][1]].HTML + ' <b>)</b>'

                if (self.polyfunctional3DFlags[index] != self.polyfunctional3DFlags[len(self.polyfunctional3DFlags)-1]) or ([0,0] in self.polyfunctional3DFlags): # not the last one
                    self._HTML += " + "
                coefficientDesignatorIndex += 1
                
            if [0,0] in self.polyfunctional3DFlags:
                self._HTML += "<b>Offset</b>"
            
        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetCoefficientDesignators(self):
        # put "offset" last
        if [0, 0] in self.polyfunctional3DFlags:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctional3DFlags)-1])
            self._coefficientDesignators.append('Offset')
        else:
            self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.polyfunctional3DFlags)])
        return self._coefficientDesignators
        
    
    def GetDataCacheFunctions(self):
        functionList = []
        for i in self.polyfunctional3DFlags:
            if i[0] > 0 or i[1] > 0:
                functionList.append([pyeq2.DataCache.DataCacheFunctions.Polyfunctional3D(NameOrValueFlag=1, args=[i[0], i[1]]), [i[0], i[1]]])
        if [0,0] in self.polyfunctional3DFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Polyfunctional3D(NameOrValueFlag=1, args=[0,0]), [0,0]])
        return functionList

    
    def ShouldDataBeRejected(self, unused):
        for i in self.polyfunctional3DFlags:
            self.independentData1CannotContainZeroFlag |= self.polyfunctionalEquationList_X[i[0]].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.polyfunctionalEquationList_X[i[0]].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.polyfunctionalEquationList_X[i[0]].cannotAcceptDataWith_Negative
            self.independentData2CannotContainZeroFlag |= self.polyfunctionalEquationList_Y[i[1]].cannotAcceptDataWith_Zero
            self.independentData2CannotContainPositiveFlag |= self.polyfunctionalEquationList_Y[i[1]].cannotAcceptDataWith_Positive
            self.independentData2CannotContainNegativeFlag |= self.polyfunctionalEquationList_Y[i[1]].cannotAcceptDataWith_Negative
        return pyeq2.IModel.IModel.ShouldDataBeRejected(self, unused)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        temp = 0.0
        coeffCount = 0
        try:
            for i in self.polyfunctional3DFlags:
                if i == [0,0]:
                    continue
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polyfunctional3D_[" + str(i[0]) + ", " + str(i[1]) + "]']")
                coeffCount += 1
                
            if [0,0] in self.polyfunctional3DFlags:
                temp += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Polyfunctional3D_[0, 0]']")
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        s = ""
        count = 0
        cd = self.GetCoefficientDesignators()
        for i in self.polyfunctional3DFlags:
            if i != [0,0]:
                if i[0] > 0 and i[1] == 0:
                    s += "\ttemp += " + cd[count] + " * " + self.polyfunctionalEquationList_X[i[0]].CPP + ";\n"
                elif i[0] == 0 and i[1] > 0:
                    s += "\ttemp += " + cd[count] + " * " + self.polyfunctionalEquationList_Y[i[1]].CPP + ";\n"
                else:
                    s += "\ttemp += " + cd[count] + " * " + self.polyfunctionalEquationList_X[i[0]].CPP + " * " + self.polyfunctionalEquationList_Y[i[1]].CPP + ";\n"
                count += 1
        if [0,0] in self.polyfunctional3DFlags:
            s += "\ttemp += " + self._coefficientDesignators[count] + ";\n"
                
        return s
