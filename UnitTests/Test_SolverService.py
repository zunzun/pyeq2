from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, types, unittest

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2
import DataForUnitTests

import numpy, scipy.interpolate
numpy.seterr(all= 'ignore')




class TestSolverService(unittest.TestCase):


    def test_SolveUsingODR_3D(self):
        coefficientsShouldBe = numpy.array([-0.04925, -0.90509, 1.28076])
        model = pyeq2.Models_3D.Polynomial.Linear('ODR')
        model.estimatedCoefficients = numpy.array([0.2, -1.0, 1.0]) # starting values for the ODR solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D, model, False)
        coefficients = pyeq2.solverService().SolveUsingODR(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-03, atol=1.0E-300))


    def test_SolveUsingODR_2D(self):
        coefficientsShouldBe = numpy.array([-8.04624, 1.53032])
        model = pyeq2.Models_2D.Polynomial.Linear('ODR')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        coefficients = pyeq2.solverService().SolveUsingODR(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-03, atol=1.0E-300))


    def test_SolveUsingLevenbergMarquardt_3D(self):
        coefficientsShouldBe = numpy.array([0.28658387, -0.90215776, 1.15483863])
        model = pyeq2.Models_3D.Polynomial.Linear('SSQABS')
        model.estimatedCoefficients = numpy.array([0.2, -1.0, 1.0]) # starting values for the simplex solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D, model, False)
        coefficients = pyeq2.solverService().SolveUsingSelectedAlgorithm(model, inAlgorithmName="Levenberg-Marquardt")
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))


    def test_SolveUsingLevenbergMarquardt_2D(self):
        coefficientsShouldBe = numpy.array([-8.01913565, 1.5264473])
        model = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        model.estimatedCoefficients = numpy.array([-4.0, 2.0]) # starting values for the simplex solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        coefficients = pyeq2.solverService().SolveUsingSelectedAlgorithm(model, inAlgorithmName="Levenberg-Marquardt")
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_SolveUsingSimplex_3D(self):
        coefficientsShouldBe = numpy.array([0.28658383, -0.90215775, 1.15483864])
        model = pyeq2.Models_3D.Polynomial.Linear('SSQABS')
        model.estimatedCoefficients = numpy.array([1.0, 1.0, 1.0]) # starting values for the simplex solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D, model, False)
        coefficients = pyeq2.solverService().SolveUsingSimplex(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_SolveUsingSimplex_SSQABS_2D(self):
        coefficientsShouldBe = numpy.array([-8.01913562, 1.52644729])
        model = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        model.estimatedCoefficients = numpy.array([1.0, 1.0]) # starting values for the simplex solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        coefficients = pyeq2.solverService().SolveUsingSimplex(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_SolveUsingSimplex_SSQREL_2D(self):
        coefficientsShouldBe = numpy.array([-6.74510573, 1.32459622])
        model = pyeq2.Models_2D.Polynomial.Linear('SSQREL')
        model.estimatedCoefficients = numpy.array([1.0, 1.0]) # starting values for the simplex solver
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        coefficients = pyeq2.solverService().SolveUsingSimplex(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_SolveUsingDE_3D(self):
        coefficientsShouldBe = numpy.array([-2.05105972, -0.49194959,  1.77817475])
        model = pyeq2.Models_3D.UserDefinedFunction.UserDefinedFunction('SSQABS', 'Default', 'a + b*X + c*Y')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D_small, model, False)
        coefficients = pyeq2.solverService().SolveUsingDE(model)
        fittingTarget = model.CalculateAllDataFittingTarget(coefficients)
        self.assertTrue(fittingTarget <= 0.1)
        
        
    def test_SolveUsingDE_2D(self):
        coefficientsShouldBe = numpy.array([-7.92223965, 1.51863709])
        model = pyeq2.Models_2D.UserDefinedFunction.UserDefinedFunction('SSQABS', 'Default', 'm*X + b')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D_small, model, False)
        coefficients = pyeq2.solverService().SolveUsingDE(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))
        
        
    def test_SolveUsingSpline_3D(self):
        xKnotPointsShouldBe = numpy.array([0.607, 0.607, 0.607, 3.017, 3.017, 3.017])
        yKnotPointsShouldBe = numpy.array([1.984, 1.984, 1.984, 3.153, 3.153, 3.153])
        coefficientsShouldBe = numpy.array([2.33418963, 1.80079612, 5.07902936, 0.54445029, 1.04110843, 2.14180324, 0.26992805, 0.39148852, 0.8177307])
        testEvaluationShouldBe = numpy.array([0.76020577997])
        model = pyeq2.Models_3D.Spline.Spline(inSmoothingFactor = 1.0, inXOrder = 2, inYOrder = 2)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D, model, False)
        fittedParameters = pyeq2.solverService().SolveUsingSpline(model)

        # example of later using the saved spline knot points and coefficients
        unFittedSpline = scipy.interpolate.fitpack2.SmoothBivariateSpline(model.dataCache.allDataCacheDictionary['X'], model.dataCache.allDataCacheDictionary['Y'], model.dataCache.allDataCacheDictionary['DependentData'], s=model.smoothingFactor, kx=model.xOrder, ky=model.yOrder)
        unFittedSpline.tck = fittedParameters
        testEvaluation = unFittedSpline.ev(2.5, 2.5)
        
        self.assertTrue(numpy.allclose(testEvaluation, testEvaluationShouldBe, rtol=1.0E-10, atol=1.0E-300))
        self.assertTrue(numpy.equal(fittedParameters[0], xKnotPointsShouldBe).all())
        self.assertTrue(numpy.equal(fittedParameters[1], yKnotPointsShouldBe).all())
        self.assertTrue(numpy.allclose(fittedParameters[2], coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))
    

    def test_SolveUsingSpline_2D(self):
        knotPointsShouldBe = numpy.array([5.357,  5.357,  5.357,  5.357,  9.861,  9.861,  9.861,  9.861])
        coefficientsShouldBe = numpy.array([ 0.38297001,  1.95535226,  4.59605664, 7.16162379, 0.0, 0.0, 0.0, 0.0])
        testEvaluationShouldBe = numpy.array([4.02361487093])
        model = pyeq2.Models_2D.Spline.Spline(inSmoothingFactor = 1.0, inXOrder = 3)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        fittedParameters = pyeq2.solverService().SolveUsingSpline(model)

        # example of later using the saved spline knot points and coefficients
        unFittedSpline = scipy.interpolate.fitpack2.UnivariateSpline(model.dataCache.allDataCacheDictionary['X'], model.dataCache.allDataCacheDictionary['DependentData'], s=model.smoothingFactor, k=model.xOrder)
        unFittedSpline._eval_args = fittedParameters
        testEvaluation = unFittedSpline(numpy.array([8.0]))
        
        self.assertTrue(numpy.allclose(testEvaluation, testEvaluationShouldBe, rtol=1.0E-10, atol=1.0E-300))
        self.assertTrue(numpy.equal(fittedParameters[0], knotPointsShouldBe).all())
        self.assertTrue(numpy.allclose(fittedParameters[1], coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))
    
    
    def test_SolveUsingLinear_2D(self):
        coefficientsShouldBe = numpy.array([-8.0191356407516956E+00, 1.5264472941853220E+00])
        model = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        coefficients = pyeq2.solverService().SolveUsingLinear(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-10, atol=1.0E-300))


    def test_SolveUsingLinear_3D(self):
        coefficientsShouldBe = numpy.array([2.8658381589774945E-01, -9.0215775175410395E-01, 1.1548386445491325E+00])
        model = pyeq2.Models_3D.Polynomial.Linear('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_3D, model, False)
        coefficients = pyeq2.solverService().SolveUsingLinear(model)
        self.assertTrue(numpy.allclose(coefficients, coefficientsShouldBe, rtol=1.0E-10, atol=1.0E-300))


    def test_ExponentialSensitivity_2D(self):
        coefficientsShouldBe = numpy.array([2.0, 0.1, -3000.0])
        model = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Offset')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataForExponentialSensitivityTest, model, False)
        model.Solve()
        self.assertTrue(numpy.allclose(model.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-10, atol=1.0E-300))



if __name__ == '__main__':
    unittest.main()
