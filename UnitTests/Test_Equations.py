from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest, inspect

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2



class Test_BioScience2D(unittest.TestCase):

    def test_AphidPopulationGrowth(self):
        equation = pyeq2.Models_2D.BioScience.AphidPopulationGrowth('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.374 >= equation.CalculateAllDataFittingTarget(equation.Solve()))



class Test_Engineering2D(unittest.TestCase):

    def test_DispersionOptical(self):
        equation = pyeq2.Models_2D.Engineering.DispersionOptical('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(1.77E-02 >= equation.CalculateAllDataFittingTarget(equation.Solve()))



class Test_Exponential2D(unittest.TestCase):

    def test_Hocket_Sherby(self):
        equation = pyeq2.Models_2D.Exponential.Hocket_Sherby('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(8.30E-03 >= equation.CalculateAllDataFittingTarget(equation.Solve()))



class Test_LegendrePolynomial2D(unittest.TestCase):

    def test_SecondDegreeLegendrePolynomial(self):
        equation = pyeq2.Models_2D.LegendrePolynomial.SecondDegreeLegendrePolynomial('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.0146 >= equation.CalculateAllDataFittingTarget(equation.Solve()))



class Test_Logarithmic2D(unittest.TestCase):

    def test_LinearLogarithmic(self):
        equation = pyeq2.Models_2D.Logarithmic.LinearLogarithmic('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(1.20 >= equation.CalculateAllDataFittingTarget(equation.Solve()))

        

class Test_Exponential3D(unittest.TestCase):

    def test_FullCubicExponential(self):
        equation = pyeq2.Models_3D.Exponential.FullCubicExponential('SSQABS')
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.05 >= equation.CalculateAllDataFittingTarget(equation.Solve()))

        

class Test_Polyfunctional2D(unittest.TestCase):

    def test_Polyfunctional2D(self):
        equation = pyeq2.Models_2D.Polyfunctional.UserSelectablePolyfunctional('SSQABS', 'Default', [0,1,3])
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.013 >= equation.CalculateAllDataFittingTarget(equation.Solve()))

        
        
class Test_Polyfunctional3D(unittest.TestCase):

    def test_Polyfunctional3D(self):
        equation = pyeq2.Models_3D.Polyfunctional.UserSelectablePolyfunctional('SSQREL', 'Default', [[0,0], [1,1], [3,3]])
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(8.2 >= equation.CalculateAllDataFittingTarget(equation.Solve()))

        
        
class Test_Rationals(unittest.TestCase):

    def test_Rational2D(self):
        equation = pyeq2.Models_2D.Rational.UserSelectableRational('SSQABS', 'Default', [0,1], [2,3])
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.009 >= equation.CalculateAllDataFittingTarget(equation.Solve()))


    def test_Rational_WithOffset_2D(self):
        equation = pyeq2.Models_2D.Rational.UserSelectableRational('SSQABS', 'Offset', [0,1], [2,3])
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.008 >= equation.CalculateAllDataFittingTarget(equation.Solve()))


        
class Test_Polynomials(unittest.TestCase):

    def test_Polynomial2D(self):
        equation = pyeq2.Models_2D.Polynomial.UserSelectablePolynomial('SSQABS', 'Default', 2)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.015 >= equation.CalculateAllDataFittingTarget(equation.Solve()))


    def test_Polynomial3D(self):
        equation = pyeq2.Models_3D.Polynomial.UserSelectablePolynomial('SSQABS', 'Default', 2, 2)
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(2.92E-04 >= equation.CalculateAllDataFittingTarget(equation.Solve()))


    def test_UserCustomizablePolynomial2D(self):
        flags = [8,9, 10]
        equation = pyeq2.Models_2D.Polynomial.UserCustomizablePolynomial('SSQABS', inPolynomial2DFlags=flags) # SSQABS by default
        pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
        self.assertTrue(0.015 >= equation.CalculateAllDataFittingTarget(equation.Solve()))

        
        
class Test_InstantiationOfAllEquations(unittest.TestCase):
    
    def test_InstantiationOfAllNamedEquations(self): # The test is that no exceptions are raised
        for submodule in inspect.getmembers(pyeq2.Models_2D) + inspect.getmembers(pyeq2.Models_3D):
            if inspect.ismodule(submodule[1]):
                for equationClass in inspect.getmembers(submodule[1]):
                    if inspect.isclass(equationClass[1]):
                        equationClass[1]('SSQABS') # non-offset forms
                        if equationClass[1].autoGenerateOffsetForm == True:
                            equationClass[1]('SSQABS', 'Offset') # offset forms

                    
        
if __name__ == '__main__':
    unittest.main()
