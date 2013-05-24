from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
    
import pyeq2

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them



class TestPolyFunctions(unittest.TestCase):
    
    def test_Offset_Term(self):
        term = pyeq2.PolyFunctions.Offset_Term('varName', 'codeName')
        
        htmlShouldBe = 'Offset'
        self.assertEqual(term.HTML, htmlShouldBe)

        cppShouldBe = 'Offset'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.0])
        valueShouldBe = numpy.array([1.0])
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_ArcTangent_Term(self):
        term = pyeq2.PolyFunctions.ArcTangent_Term('varName', 'codeName')
        
        htmlShouldBe = 'atan(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'atan(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.0])
        valueShouldBe = numpy.arctan(1.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_NegativeOne_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='-1.0', logFlag=False)
        
        htmlShouldBe = 'varName<sup>-1.0</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, -1.0)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, -1.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_HyperbolicCosine_Term(self):
        term = pyeq2.PolyFunctions.HyperbolicCosine_Term('varName', 'codeName')
        
        htmlShouldBe = 'cosh(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'cosh(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.cosh(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_OnePointFive_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='1.5', logFlag=False)
        
        htmlShouldBe = 'varName<sup>1.5</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, 1.5)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, 1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_ZeroPointFive_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='0.5', logFlag=False)
        
        htmlShouldBe = 'varName<sup>0.5</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, 0.5)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, 0.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_VariableUnchanged_Term(self):
        term = pyeq2.PolyFunctions.VariableUnchanged_Term('varName', 'codeName')
        
        htmlShouldBe = 'varName'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'codeName'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.array([1.5])
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_Two_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='2.0', logFlag=False)
        
        htmlShouldBe = 'varName<sup>2.0</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, 2.0)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, 2.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_HyperbolicSine_Term(self):
        term = pyeq2.PolyFunctions.HyperbolicSine_Term('varName', 'codeName')
        
        htmlShouldBe = 'sinh(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'sinh(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.sinh(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Exponential_VariableUnchanged_Term(self):
        term = pyeq2.PolyFunctions.Exponential_VariableUnchanged_Term('varName', 'codeName')
        
        htmlShouldBe = 'exp(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'exp(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.exp(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Exponential_VariableTimesNegativeOne_Term(self):
        term = pyeq2.PolyFunctions.Exponential_VariableTimesNegativeOne_Term('varName', 'codeName')
        
        htmlShouldBe = 'exp(-varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'exp(-1.0 * codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.exp(-1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Sine_Term(self):
        term = pyeq2.PolyFunctions.Sine_Term('varName', 'codeName')
        
        htmlShouldBe = 'sin(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'sin(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.sin(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Cosine_Term(self):
        term = pyeq2.PolyFunctions.Cosine_Term('varName', 'codeName')
        
        htmlShouldBe = 'cos(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'cos(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.cos(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Tangent_Term(self):
        term = pyeq2.PolyFunctions.Tangent_Term('varName', 'codeName')
        
        htmlShouldBe = 'tan(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'tan(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.tan(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_HyperbolicTangent_Term(self):
        term = pyeq2.PolyFunctions.HyperbolicTangent_Term('varName', 'codeName')
        
        htmlShouldBe = 'tanh(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'tanh(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.tanh(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_NegativeZeroPointFive_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='-0.5', logFlag=False)
        
        htmlShouldBe = 'varName<sup>-0.5</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, -0.5)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, -0.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_NegativeTwo_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='-2', logFlag=False)
        
        htmlShouldBe = 'varName<sup>-2</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(codeName, -2)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(1.5, -2.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Log_Term(self):
        term = pyeq2.PolyFunctions.Log_Term('varName', 'codeName')
        
        htmlShouldBe = 'ln(varName)'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'log(codeName)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.log(1.5)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_NegativeOne_OfLog_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='-1.0', logFlag=True)
        
        htmlShouldBe = 'ln(varName)<sup>-1.0</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(log(codeName), -1.0)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(numpy.log(1.5), -1.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_Two_OfLog_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='2.0', logFlag=True)
        
        htmlShouldBe = 'ln(varName)<sup>2.0</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(log(codeName), 2.0)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(numpy.log(1.5), 2.0)
        self.assertEqual(term.value(testArray), valueShouldBe)


    def test_Power_NegativeTwo_OfLog_Term(self):
        term = pyeq2.PolyFunctions.PowerTerm('varName', 'codeName', powerString='-2.0', logFlag=True)
        
        htmlShouldBe = 'ln(varName)<sup>-2.0</sup>'
        self.assertEqual(term.HTML, htmlShouldBe)
        
        cppShouldBe = 'pow(log(codeName), -2.0)'
        self.assertEqual(term.CPP, cppShouldBe)
        
        testArray = numpy.array([1.5])
        valueShouldBe = numpy.power(numpy.log(1.5), -2.0)
        self.assertEqual(term.value(testArray), valueShouldBe)



if __name__ == '__main__':
    unittest.main()
