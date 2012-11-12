from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest, string

# the pyeq2 directory is located up one level from here
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2
import DataForUnitTests

import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them



class TestExtendedVersionHandlers(unittest.TestCase):
    
    def test_ExtendedVersion_Exponential_WithOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_Offset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx) + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Exponential With Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([6.6644703, 0.10305385, -11.2292899])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))


    def test_ExtendedVersion_Reciprocal_Exponential_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Reciprocal')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_Reciprocal')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = 1.0 / y')
        self.assertEqual(equation.GetDisplayName(), 'Reciprocal Exponential')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([1.0869969588803379E+01, -4.4497258666306111E-01])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Reciprocal_Exponential_WithOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Reciprocal With Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_ReciprocalWithOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = 1.0 / y + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Reciprocal Exponential With Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.15004943, -0.10305384, -11.22929034])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Inverse_Exponential_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Inverse')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_Inverse')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = x / y')
        self.assertEqual(equation.GetDisplayName(), 'Inverse Exponential')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([30.67342834, -0.31776877])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Inverse_Exponential_WithOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Inverse With Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_InverseWithOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = x / y + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Inverse Exponential With Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([1.55291718, -0.06133912, -4.44443162])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Exponential_WithLinearDecay_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Linear Decay')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_LinearDecay')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = y / x')
        self.assertEqual(equation.GetDisplayName(), 'Exponential With Linear Decay')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.25868186, 0.57252871])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))
        
        
    def test_ExtendedVersion_Exponential_WithLinearDecayAndOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Linear Decay And Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_LinearDecayAndOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = y / x + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Exponential With Linear Decay And Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([9.94308512, 0.27132282, -7.28329138])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Exponential_WithLinearGrowth_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Linear Growth')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_LinearGrowth')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = y * x')
        self.assertEqual(equation.GetDisplayName(), 'Exponential With Linear Growth')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.03260151, 0.31776877])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))
        
        
    def test_ExtendedVersion_Exponential_WithLinearGrowthAndOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.Exponential('SSQABS', 'Linear Growth And Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_LinearGrowthAndOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = a * exp(bx)<br>y = y * x + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Exponential With Linear Growth And Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 1)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.643949371878, 0.0613391161993, -4.44443175952])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))


    def test_ExtendedVersion_Asymptotic_Exponential_A_WithExponentialGrowth_2D(self):
        equation = pyeq2.Models_2D.Exponential.AsymptoticExponentialA('SSQABS', 'Exponential Growth')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_ExponentialGrowth')
        self.assertEqual(equation.GetDisplayHTML(), 'y = 1.0 - a<sup>x</sup><br>y = y * (c * exp(x))')
        self.assertEqual(equation.GetDisplayName(), 'Asymptotic Exponential A With Exponential Growth')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 2)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.lowerCoefficientBounds = []
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.001, 0.00041378])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0, atol=1.0E-300))
        
        
    def test_ExtendedVersion_Asymptotic_Exponential_A_WithExponentialGrowthAndOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.AsymptoticExponentialA('SSQABS', 'Exponential Growth And Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_ExponentialGrowthAndOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = 1.0 - a<sup>x</sup><br>y = y * (d * exp(x)) + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Asymptotic Exponential A With Exponential Growth And Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 2)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([0.314768543035, 0.000328683484927, 1.30596153831])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))


    def test_ExtendedVersion_Asymptotic_Exponential_A_WithExponentialDecay_2D(self):
        equation = pyeq2.Models_2D.Exponential.AsymptoticExponentialA('SSQABS', 'Exponential Decay')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_ExponentialDecay')
        self.assertEqual(equation.GetDisplayHTML(), 'y = 1.0 - a<sup>x</sup><br>y = y / (c * exp(x))')
        self.assertEqual(equation.GetDisplayName(), 'Asymptotic Exponential A With Exponential Decay')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 2)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([4.24147585367, -10.8635807983])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-05, atol=1.0E-300))
        
        
    def test_ExtendedVersion_Asymptotic_Exponential_A_WithExponentialDecayAndOffset_2D(self):
        equation = pyeq2.Models_2D.Exponential.AsymptoticExponentialA('SSQABS', 'Exponential Decay And Offset')
        self.assertEqual(equation.extendedVersionHandler.__class__.__name__, 'ExtendedVersionHandler_ExponentialDecayAndOffset')
        self.assertEqual(equation.GetDisplayHTML(), 'y = 1.0 - a<sup>x</sup><br>y = y / (d * exp(x)) + Offset')
        self.assertEqual(equation.GetDisplayName(), 'Asymptotic Exponential A With Exponential Decay And Offset')
        self.assertEqual(equation.GetCoefficientDesignators(), ['a', 'b', 'Offset'])
        self.assertEqual(len(equation.GetDataCacheFunctions()), 2)
        self.assertFalse(equation.CanLinearSolverBeUsedForSSQABS())

        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, equation, False)
        
        equation.Solve()
        coefficientsShouldBe = numpy.array([2.69273579217, 0.00518863941, 182.725486049])
        self.assertTrue(numpy.allclose(equation.solvedCoefficients, coefficientsShouldBe, rtol=1.0E-06, atol=1.0E-300))



if __name__ == '__main__':
    unittest.main()
