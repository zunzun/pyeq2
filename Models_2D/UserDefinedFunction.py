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

import numpy # implicitly required by compiling the userFunctionCodeObject in the method EvaluateCachedData() below
numpy.seterr(all= 'ignore')

import StringIO, parser

import pyeq2.Model_2D_BaseClass



class UserDefinedFunction(pyeq2.Model_2D_BaseClass.Model_2D_BaseClass):
    userDefinedFunctionFlag = True

    # based on http://lybniz2.sourceforge.net/safeeval.html
    functionDictionary = {'Arithmetic Operations':    ['power', 'mod'],
                          'Exponents And Logarithms': ['exp', 'log', 'log10', 'log2'],
                          'Trigonometric Functions':  ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'hypot', 'arctan2', 'deg2rad', 'rad2deg'],
                          'Hyperbolic Trig Functions':['arcsinh', 'arccosh', 'arctanh', 'sinh', 'cosh', 'tanh'],
                          'Other Special Functions':  ['sinc'],
                          'Miscellaneous':            ['sqrt', 'square', 'fabs', 'sign']
                         }
                   
    constantsDictionary = {'Constants':['pi', 'e']}
    _baseName = "User Defined Function"

    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False


    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default', inUserFunctionString = ''):
        if inUserFunctionString:
            self.ParseAndCompileUserFunctionString(inUserFunctionString)
        pyeq2.Model_2D_BaseClass.Model_2D_BaseClass.__init__(self, inFittingTarget, inExtendedVersionName) # call superclass        


    def GetDisplayHTML(self):
        return 'y = User Defined Function'


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        return functionList


    def GetTokensFromTupleParsingHelper(self, tup, inList=None):
        if inList is None:
            inList = []
        if type(tup) is type(()):
            tupleLength = len(tup)
            if tupleLength > 1 and type(tup[0]) is not type(()):
                if tup[0] == 1:
                    inList.append(tup[1])
            if tupleLength == 2: # so a caret character can be trapped later
                if tup[0] == 33:
                    if tup[1] == '^':
                        inList.append('^')
            for i in tup:
                inList = self.GetTokensFromTupleParsingHelper(i, inList)
        return inList


    def ParseAndCompileUserFunctionString(self, inString):
       
        # shift user functions into numpy namespace at run time, do not import time
        numpySafeTokenList = []
        for key in list(self.functionDictionary.keys()):
            numpySafeTokenList += self.functionDictionary[key]
        for key in list(self.constantsDictionary.keys()):
            numpySafeTokenList += self.constantsDictionary[key]
           
        # to shift user functions such as "power" into the numpy namespace "numpy.power" for evaluation
        for token in numpySafeTokenList:
            exec(token + ' = numpy.' + token)
       
        # no blank lines of text, StringIO() allows using file methods on text
        stringToConvert = ''
        rawData = StringIO.StringIO(inString).readlines()
       
        for line in rawData:
            stripped = line.strip()
            if len(stripped) > 0: # no empty strings
                if stripped[0] != '#': # no comment-only lines
                    stringToConvert += stripped + '\n'

        # convert brackets to parentheses
        stringToConvert = stringToConvert.replace('[', '(').replace(']', ')')
       
        if stringToConvert == '':
            raise Exception('You must enter some function text for the software to use.')

        if -1 != stringToConvert.find('='):
            raise Exception('Please do not use an equals sign "=" in your text.')

        st = parser.expr(stringToConvert)
        tup = st.totuple()
        tokens = self.GetTokensFromTupleParsingHelper(tup)

        if '^' in tokens:
            raise Exception('The caret symbol "^" is not recognized by the parser, please substitute double asterisks "**" for "^".')
           
        if 'ln' in tokens:
            raise Exception("The parser uses log() for the natural log function, not ln(). Please use log() in your text.")

        if 'abs' in tokens:
            raise Exception("The parser uses fabs() for the absolute value, not abs(). Please use fabs() in your text.")

        if 'EXP' in tokens:
            raise Exception("The parser uses lower case exp(), not upper case EXP(). Please use lower case exp() in your text.")

        if 'LOG' in tokens:
            raise Exception("The parser uses lower case log(), not upper case LOG(). Please use lower case log() in your text.")

        # test for required reserved tokens
        tokenNames = list(set(tokens) - set(numpySafeTokenList))
        if 'X' not in tokenNames:
            raise Exception('You must use a separate upper case "X" in your function to enter a valid function of X.')

        self._coefficientDesignators = sorted(list(set(tokenNames) - set(['X'])))
               
        if len(self._coefficientDesignators) == 0:
            raise Exception('I could not find any equation parameter or coefficient names, please check the function text')

        # now compile code object using safe tokens with integer conversion
        self.safe_dict = dict([ (k, locals().get(k, None)) for k in numpySafeTokenList ])
           
        # convert integer use such as (3/2) into floats such as (3.0/2.0)
        st = parser.expr(stringToConvert)
        stList = parser.st2list(st)
        stList = self.RecursivelyConvertIntStringsToFloatStrings(stList)
        st = parser.sequence2st(stList)

        # later evals re-use this compiled code for improved performance in EvaluateCachedData() methods
        self.userFunctionCodeObject  = parser.compilest(st)

        
    def ShouldDataBeRejected(self, inModel):
        return False

    
    def AreCoefficientsWithinBounds(self, inCoeffs):
        return True # User Defined Functions do not have coefficient bounds
        

    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        self.safe_dict['X'] = inDataCacheDictionary['X']
        if self.GetDimensionality() == 3:
            self.safe_dict['Y'] = inDataCacheDictionary['Y']
            
        # define coefficient values before calling eval
        for i in range(len(self._coefficientDesignators)):
            self.safe_dict[self._coefficientDesignators[i]] = inCoeffs[i]
        
        # eval uses previously compiled code for improved performance
        # based on http://lybniz2.sourceforge.net/safeeval._HTML
        try:
            temp = eval(self.userFunctionCodeObject, {"__builtins__":None, 'numpy':numpy}, self.safe_dict)
            return self.extendedVersionHandler.GetAdditionalModelPredictions(temp, inCoeffs, inDataCacheDictionary, self)
        except:
            return numpy.ones(len(inDataCacheDictionary['X'])) * 1.0E300
    

    def Solve(self, inUserFunctionString = None, inAlgorithmName="Levenberg-Marquardt"):
        if inUserFunctionString:
            self.ParseAndCompileUserFunctionString(inUserFunctionString)

        # starting point
        if len(self.estimatedCoefficients) == 0:
            self.estimatedCoefficients = pyeq2.solverService().SolveUsingDE(self)
            
        if self.fittingTarget == 'ODR':
            return pyeq2.solverService().SolveUsingODR(self)
        
        self.estimatedCoefficients = pyeq2.solverService().SolveUsingSelectedAlgorithm(self, inAlgorithmName=inAlgorithmName)
        return pyeq2.solverService().SolveUsingSimplex(self)
