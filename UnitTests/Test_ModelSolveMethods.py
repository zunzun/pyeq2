from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import numpy, scipy.interpolate
numpy.seterr(all= 'ignore')

import pyeq2
import DataForUnitTests



class TestModelSolveMethods(unittest.TestCase):
    
    def test_UserDefinedFunctionSolve_3D(self):
        resultShouldBe = numpy.array([-2.46874698, -0.43649152, 1.88125938])
        model = pyeq2.Models_3D.UserDefinedFunction.UserDefinedFunction('SSQABS', 'Default', 'a + b*X + c*Y')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D_small, model, False)
        result = model.Solve()
        self.assertTrue(numpy.allclose(result, resultShouldBe, rtol=1.0E-06, atol=1.0E-300))

        
    def test_UserDefinedFunctionSolve_SSQREL_2D(self):
        resultShouldBe = numpy.array([-6.93576507, 1.36423107])
        model = pyeq2.Models_2D.UserDefinedFunction.UserDefinedFunction('SSQREL', 'Default', 'm*X + b')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D_small, model, False)
        result = model.Solve()
        self.assertTrue(numpy.allclose(result, resultShouldBe, rtol=1.0E-06, atol=1.0E-300))

        
    def test_UserDefinedFunctionSolve_SSQABS_2D(self):
        resultShouldBe = numpy.array([-7.88180304, 1.51245438])
        model = pyeq2.Models_2D.UserDefinedFunction.UserDefinedFunction('SSQABS', 'Default', 'm*X + b')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D_small, model, False)
        result = model.Solve()
        self.assertTrue(numpy.allclose(result, resultShouldBe, rtol=1.0E-06, atol=1.0E-300))

        
    def test_SplineSolve_3D(self):
        resultShouldBe = (numpy.array([0.607, 0.607, 0.607, 3.017, 3.017, 3.017]),
                          numpy.array([1.984, 1.984, 1.984, 3.153, 3.153, 3.153]),
                          numpy.array([2.33418963, 1.80079612, 5.07902936, 0.54445029, 1.04110843, 2.14180324, 0.26992805, 0.39148852, 0.8177307])
                         )
        model = pyeq2.Models_3D.Spline.Spline(inSmoothingFactor = 1.0, inXOrder = 2, inYOrder = 2)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(model.exampleData, model, False)
        result = model.Solve()
        self.assertTrue(numpy.allclose(result[0], resultShouldBe[0], rtol=1.0E-06, atol=1.0E-300))
        self.assertTrue(numpy.allclose(result[1], resultShouldBe[1], rtol=1.0E-06, atol=1.0E-300))
        self.assertTrue(numpy.allclose(result[2], resultShouldBe[2], rtol=1.0E-06, atol=1.0E-300))


    def test_SplineSolve_2D(self):
        resultShouldBe = (numpy.array([5.357, 5.357, 5.357, 5.357, 9.861, 9.861, 9.861, 9.861]),
                          numpy.array([0.38297001, 1.95535226, 4.59605664, 7.16162379, 0.0, 0.0, 0.0, 0.0]),
                          3
                         )
        model = pyeq2.Models_2D.Spline.Spline(inSmoothingFactor = 1.0, inXOrder = 3)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(model.exampleData, model, False)
        result = model.Solve()
        self.assertTrue(numpy.allclose(result[0], resultShouldBe[0], rtol=1.0E-06, atol=1.0E-300))
        self.assertTrue(numpy.allclose(result[1], resultShouldBe[1], rtol=1.0E-06, atol=1.0E-300))
        self.assertEqual(result[2], resultShouldBe[2])

        
if __name__ == '__main__':
    unittest.main()
