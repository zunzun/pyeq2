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



class UserSelectableRational(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    userSelectableRationalFlag = True
    _baseName = "User-Selectable Rational"
    _canLinearSolverBeUsedForSSQABS = False
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = True
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default', inRationalNumeratorFlags = [], inRationalDenominatorFlags = [], inRationalEquationList = []):
        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
    
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass

        self.rationalNumeratorFlags = inRationalNumeratorFlags
        self.rationalDenominatorFlags = inRationalDenominatorFlags
        
        if inRationalEquationList:
            self.rationalEquationList = inRationalEquationList
        else:
            self.rationalEquationList = pyeq2.PolyFunctions.GenerateListForRationals_2D()
        
        self._HTML = "y = user-selectable rational"
        self._leftSideHTML = 'y'
    
    
    def GetDisplayHTML(self):                
        if 0 == (len(self.rationalNumeratorFlags) + len(self.rationalDenominatorFlags)):
            self._HTML = "y = user-selectable rational"
        else:
            self._HTML = "</B><B>y = (" # turn off any preceding bolding
            count = 0
            for xindex in range(len(self.rationalEquationList)):
                if xindex in self.rationalNumeratorFlags: # numerator
                    if xindex == 0:
                        self._HTML += self.listOfAdditionalCoefficientDesignators[count] + " "
                    else:
                        self._HTML += self.listOfAdditionalCoefficientDesignators[count] + "(</B>&nbsp;" + self.rationalEquationList[xindex].HTML + "&nbsp;<B>) "
                    count += 1
                    if len(self.rationalNumeratorFlags) > count:
                        self._HTML += "+ "
            self._HTML += ") / (1.0 + "
            count = 0
            for xindex in range(len(self.rationalEquationList)):
                if xindex in self.rationalDenominatorFlags: # denominator
                    if xindex == 0:
                        self._HTML += self.listOfAdditionalCoefficientDesignators[count + len(self.rationalNumeratorFlags)] + " "
                    else:
                        self._HTML += self.listOfAdditionalCoefficientDesignators[count + len(self.rationalNumeratorFlags)] + "(</B>&nbsp;" + self.rationalEquationList[xindex].HTML + "&nbsp;<B>) "
                    count += 1
                    if len(self.rationalDenominatorFlags) > count:
                        self._HTML += "+ "
            self._HTML += ')</B>'
            
        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetCoefficientDesignators(self):
        self._coefficientDesignators = list(self.listOfAdditionalCoefficientDesignators[:len(self.rationalNumeratorFlags) + len(self.rationalDenominatorFlags)])
        return self.extendedVersionHandler.AssembleCoefficientDesignators(self)


    def GetDataCacheFunctions(self):
        functionList = []
        for i in self.rationalNumeratorFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Rational2D(NameOrValueFlag=1, args=i), i])
        for i in self.rationalDenominatorFlags:
            functionList.append([pyeq2.DataCache.DataCacheFunctions.Rational2D(NameOrValueFlag=1, args=i), i])
        return functionList

    
    def ShouldDataBeRejected(self, unused):                
        for i in range(len(self.rationalNumeratorFlags)):
            self.independentData1CannotContainZeroFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Negative
        for i in range(len(self.rationalDenominatorFlags)):
            self.independentData1CannotContainZeroFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Zero
            self.independentData1CannotContainPositiveFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Positive
            self.independentData1CannotContainNegativeFlag |= self.rationalEquationList[i].cannotAcceptDataWith_Negative
        return pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.ShouldDataBeRejected(self, unused)


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        numerator = 0.0
        denominator = 0.0
        coeffCount = 0
        try:
            for i in self.rationalNumeratorFlags:
                numerator += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Rational2D_" + str(i) + "']")
                coeffCount += 1
            for i in self.rationalDenominatorFlags:
                denominator += inCoeffs[coeffCount] * eval("inDataCacheDictionary['Rational2D_" + str(i) + "']")
                coeffCount += 1
            temp = numerator / (1.0 + denominator)
            
            # handle an old design error regarding offsets
            if len(inCoeffs) > coeffCount and -1 == self.extendedVersionHandler.__class__.__name__.find('_Offset'):
                temp += inCoeffs[-1]
                
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['DependentData'])) * 1.0E300


    def SpecificCodeCPP(self):
        numeratorString = ""
        denominatorString = ""
        coeffCount = 0
        EquationListForRationals = pyeq2.PolyFunctions.GenerateListForRationals_2D()
        
        for i in self.rationalNumeratorFlags:
            if coeffCount < (len(self.rationalNumeratorFlags) - 1):
                if i == 0:
                    numeratorString += self._coefficientDesignators[coeffCount] + " + "
                else:
                    numeratorString += self._coefficientDesignators[coeffCount] + " * " + EquationListForRationals[i].CPP + " + "
            else:
                numeratorString += self._coefficientDesignators[coeffCount] + " * " + EquationListForRationals[i].CPP
            coeffCount += 1
            
        for i in self.rationalDenominatorFlags:
            if coeffCount < (len(self.rationalNumeratorFlags) + len(self.rationalDenominatorFlags) - 1):
                if i == 0:
                    denominatorString += self._coefficientDesignators[coeffCount] + " + "
                else:
                    denominatorString += self._coefficientDesignators[coeffCount] + " * " + EquationListForRationals[i].CPP + " + "
            else:
                denominatorString += self._coefficientDesignators[coeffCount] + " * " + EquationListForRationals[i].CPP
            coeffCount += 1
            
        s = "\ttemp = (" + numeratorString + ")\n;"
        s += "\ttemp /= (1.0 + " + denominatorString + ")\n;"

        # handle an old design error regarding offsets
        if len(self._coefficientDesignators) > coeffCount  and -1 == self.extendedVersionHandler.__class__.__name__.find('_Offset'):
            s += "\ttemp += Offset\n;"
        return s
