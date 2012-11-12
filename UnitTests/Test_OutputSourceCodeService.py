from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest, inspect

# the pyeq2 directory is located up one level from here
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
    
import pyeq2
import DataForUnitTests



class TestGenerationOfOutputSourceCodeForAllEquations(unittest.TestCase):
    
    def test_GenerationOf_CPP_ForAllEquations(self): # ensure no coding errors in source code generation for any equation
        for submodule in inspect.getmembers(pyeq2.Models_2D) + inspect.getmembers(pyeq2.Models_3D):
            if inspect.ismodule(submodule[1]):
                for equationClass in inspect.getmembers(submodule[1]):
                    if inspect.isclass(equationClass[1]):
                        try: # not all equation classes have a fixed number of coefficient designators
                            equation = equationClass[1]()
                            coeffCount = len(equation.GetCoefficientDesignators())
                            equation.solvedCoefficients = [1.0] * len(equation.GetCoefficientDesignators())
                        except:
                            continue
                        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(equation)
                        self.assertIs(type(generated), type('')) # must be a striong
                        self.assertTrue(len(generated) > 0) # must have a length > 0



class TestConversionsFromCPP(unittest.TestCase):
    
    cppStringForTestingLanguageConversions = '''
\t// comment
\tdouble doubleVariable;
\ttemp = a * abs(1.1);
\ttemp = a / abs(1.1);
\ttemp += pow(temp);
\ttemp -= log(temp);
\ttemp = log10(temp);
\ttemp = exp(temp);
\ttemp = sin(temp);
\ttemp = cos(temp);
\ttemp = tan(temp);
\ttemp = tanh(temp);
\ttemp = cosh(temp);
'''


    def test_ConversionFromCppToCSHARP(self):
        convertedShouldBe = '''
\t\t// comment
\t\tdouble doubleVariable;
\t\ttemp = a * Math.Abs(1.1);
\t\ttemp = a / Math.Abs(1.1);
\t\ttemp += Math.Pow(temp);
\t\ttemp -= Math.Log(temp);
\t\ttemp = Math.Log10(temp);
\t\ttemp = Math.Exp(temp);
\t\ttemp = Math.Sin(temp);
\t\ttemp = Math.Cos(temp);
\t\ttemp = Math.Tan(temp);
\t\ttemp = Math.Tanh(temp);
\t\ttemp = Math.Cosh(temp);
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToCSHARP(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)


    def test_ConversionFromCppToJAVA(self):
        convertedShouldBe = '''
\t\t// comment
\t\tdouble doubleVariable;
\t\ttemp = a * Math.abs(1.1);
\t\ttemp = a / Math.abs(1.1);
\t\ttemp += Math.pow(temp);
\t\ttemp -= Math.log(temp);
\t\ttemp = Math.log10(temp);
\t\ttemp = Math.exp(temp);
\t\ttemp = Math.sin(temp);
\t\ttemp = Math.cos(temp);
\t\ttemp = Math.tan(temp);
\t\ttemp = Math.tanh(temp);
\t\ttemp = Math.cosh(temp);
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToJAVA(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)


    def test_ConversionFromCppToVBA(self):
        convertedShouldBe = '''
\t' comment
\tvar doubleVariable
\ttemp = a * Abs(1.1)
\ttemp = a / Abs(1.1)
\ttemp = temp + Application.WorksheetFunction.power(temp)
\ttemp = temp - Application.WorksheetFunction.ln(temp)
\ttemp = Application.WorksheetFunction.log(temp)
\ttemp = Exp(temp)
\ttemp = sin(temp)
\ttemp = cos(temp)
\ttemp = tan(temp)
\ttemp = Application.WorksheetFunction.tanh(temp)
\ttemp = Application.WorksheetFunction.cosh(temp)
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToVBA(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)
        
        
    def test_ConversionFromCppToPYTHON(self):
        convertedShouldBe = '''
    # comment
    # double doubleVariable
    temp = a * math.fabs(1.1)
    temp = a / math.fabs(1.1)
    temp += math.pow(temp)
    temp -= math.log(temp)
    temp = math.log10(temp)
    temp = math.exp(temp)
    temp = math.sin(temp)
    temp = math.cos(temp)
    temp = math.tan(temp)
    temp = math.tanh(temp)
    temp = math.cosh(temp)
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToPYTHON(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)


    def test_ConversionFromCppToSCILAB(self):
        convertedShouldBe = '''
\t// comment
\tdoubleVariable;
\ttemp = a * abs(1.1);
\ttemp = a / abs(1.1);
\ttemp = temp + power(temp);
\ttemp = temp - log(temp);
\ttemp = log10(temp);
\ttemp = exp(temp);
\ttemp = sin(temp);
\ttemp = cos(temp);
\ttemp = tan(temp);
\ttemp = tanh(temp);
\ttemp = cosh(temp);
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToSCILAB(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)


    def test_ConversionFromCppToMATLAB(self):
        convertedShouldBe = '''
\t% comment
\tdoubleVariable;
\ttemp = a .* abs(1.1);
\ttemp = a ./ abs(1.1);
\ttemp = temp + power(temp);
\ttemp = temp - log(temp);
\ttemp = log10(temp);
\ttemp = exp(temp);
\ttemp = sin(temp);
\ttemp = cos(temp);
\ttemp = tan(temp);
\ttemp = tanh(temp);
\ttemp = cosh(temp);
'''
        converted = pyeq2.outputSourceCodeService().ConvertCppToMATLAB(self.cppStringForTestingLanguageConversions)
        self.assertEqual(converted, convertedShouldBe)



class TestGenerationOfOutputSourceCode(unittest.TestCase):
    
    def test_GenerationOf_CPP(self):
        generatedShouldBe = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me directly using zunzun@zunzun.com.
//
//      James


#include <math.h>

// Fitting target: lowest sum of squared absolute error
// Fitting target value = 0.223837322455

double Linear_model(double x_in)
{
	double temp;
	temp = 0.0;

	// coefficients
	double a = -8.01913564075E+00;
	double b = 1.52644729419E+00;

	temp += a + b * x_in;
	return temp;
}
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeCPP(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_VBA(self):
        generatedShouldBe = '''' To the best of my knowledge this code is correct.
' If you find any errors or problems please contact
' me directly using zunzun@zunzun.com.
'
'      James

' Fitting target: lowest sum of squared absolute error
' Fitting target value = 0.223837322455

Public Function Linear_model(x_in)
\ttemp = 0.0

\t' coefficients
\tConst a = -8.01913564075E+00
\tConst b = 1.52644729419E+00

\ttemp = temp + a + b * x_in
\tLinear_model = temp
End Function
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeVBA(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_PYTHON(self):
        generatedShouldBe = '''# To the best of my knowledge this code is correct.
# If you find any errors or problems please contact
# me directly using zunzun@zunzun.com.
#
#      James


import math

# Fitting target: lowest sum of squared absolute error
# Fitting target value = 0.223837322455

def Linear_model(x_in):
    temp = 0.0

    # coefficients
    a = -8.01913564075E+00
    b = 1.52644729419E+00

    temp += a + b * x_in
    return temp
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodePYTHON(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_JAVA(self):
        generatedShouldBe = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me directly using zunzun@zunzun.com.
//
//      James


import java.lang.Math;

// Fitting target: lowest sum of squared absolute error
// Fitting target value = 0.223837322455

class Linear
{
\tdouble Linear_model(double x_in)
\t{
\t\tdouble temp;
\t\ttemp = 0.0;

\t\t// coefficients
\t\tdouble a = -8.01913564075E+00;
\t\tdouble b = 1.52644729419E+00;

\t\ttemp += a + b * x_in;
\t\treturn temp;
\t}
}
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeJAVA(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_CSHARP(self):
        generatedShouldBe = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me directly using zunzun@zunzun.com.
//
//      James


using System;

// Fitting target: lowest sum of squared absolute error
// Fitting target value = 0.223837322455

class Linear
{
\tdouble Linear_model(double x_in)
\t{
\t\tdouble temp;
\t\ttemp = 0.0;

\t\t// coefficients
\t\tdouble a = -8.01913564075E+00;
\t\tdouble b = 1.52644729419E+00;

\t\ttemp += a + b * x_in;
\t\treturn temp;
\t}
}
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeCSHARP(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_SCILAB(self):
        generatedShouldBe = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me directly using zunzun@zunzun.com.
//
//      James


// Fitting target: lowest sum of squared absolute error
// Fitting target value = 0.223837322455

function y = Linear_model(x_in)
\ttemp = 0.0;

\t// coefficients
\ta = -8.01913564075E+00;
\tb = 1.52644729419E+00;

\ttemp = temp + a + b * x_in;

\ty = temp;
endfunction
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeSCILAB(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)


    def test_GenerationOf_MATLAB(self):
        generatedShouldBe = '''% To the best of my knowledge this code is correct.
% If you find any errors or problems please contact
% me directly using zunzun@zunzun.com.
%
%      James


% Fitting target: lowest sum of squared absolute error
% Fitting target value = 0.223837322455

function y = Linear_model(x_in)
\ttemp = 0.0;

\t% coefficients
\ta = -8.01913564075E+00;
\tb = 1.52644729419E+00;

\ttemp = temp + a + b .* x_in;

\ty = temp;
'''
        equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        equation.Solve()
        generated = pyeq2.outputSourceCodeService().GetOutputSourceCodeMATLAB(equation, inDigitsOfPrecisionString = '11')
        self.assertEqual(generated, generatedShouldBe)



if __name__ == '__main__':
    unittest.main()
