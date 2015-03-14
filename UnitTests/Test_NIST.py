from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, unittest

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
import pyeq2

import NIST_TestingUtilities

# from http://www.itl.nist.gov/div898/strd/nls/nls_info.shtml
#
# The certified results are reported to 11 decimal places for each dataset.
# Clearly, most of these digits are not statistically significant, and we
# are not advocating that results should be reported to this number of
# digits in a statistical context. We do believe, however, that this
# number of digits can be useful when testing the numerical properties of
# a procedure. Except in cases where the certified value is essentially
# zero (for example, as occurs for the three Lanczos problems), a good
# nonlinear least squares procedure should be able to duplicate the
# certified results to at least 4 or 5 digits.

class Test_NIST(unittest.TestCase):
    
    def test_NIST_Nelson_3D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Nelson.dat', True)
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_3D.NIST.NIST_Nelson(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_3D.NIST.NIST_Nelson(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)

    
    def test_NIST_Bennett5_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Bennett5.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Bennett5(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Bennett5(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_BoxBOD_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/BoxBOD.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_BoxBOD(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_BoxBOD(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Chwirut1_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Chwirut1.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Chwirut(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Chwirut(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Chwirut2_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Chwirut2.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Chwirut(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Chwirut(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_DanWood_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/DanWood.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_DanWood(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_DanWood(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_ENSO_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/ENSO.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_ENSO(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_ENSO(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Eckerle4_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Eckerle4.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Eckerle4(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Eckerle4(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Gauss1_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Gauss1.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Gauss2_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Gauss2.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Gauss3_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Gauss3.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Gauss(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Hahn_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Hahn1.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Hahn(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Hahn(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Kirby_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Kirby2.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Kirby(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Kirby(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Lanczos1_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Lanczos1.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Lanczos2_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Lanczos2.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Lanczos3_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Lanczos3.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Lanczos(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_MGH09_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/MGH09.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH09(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH09(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_MGH10_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/MGH10.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH10(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH10(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_MGH17_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/MGH17.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH17(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_MGH17(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Misra1a_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Misra1a.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1a(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1a(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Misra1b_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Misra1b.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1b(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1b(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Misra1c_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Misra1c.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1c(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1c(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Misra1d_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Misra1d.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1d(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Misra1d(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Rat42_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Rat42.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Rat42(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Rat42(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Rat43_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Rat43.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Rat43(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Rat43(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Roszman_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Roszman1.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Roszman(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Roszman(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
    def test_NIST_Thurber_2D(self):
        nistDataObject = NIST_TestingUtilities.LoadDataFileFromNIST('NIST_DataFiles/Thurber.dat')
        result1 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Thurber(), nistDataObject, nistDataObject.Start_1_Values, 'Start 1', False)
        result2 = NIST_TestingUtilities.CalculateAndPrintResults(pyeq2.Models_2D.NIST.NIST_Thurber(), nistDataObject, nistDataObject.Start_2_Values, 'Start 2', False)
        self.assertTrue(result1)
        self.assertTrue(result2)
        
        
        
if __name__ == '__main__':
    unittest.main()
