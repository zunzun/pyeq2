from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys, os, unittest

# the pyeq2 directory is located up one level from here
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))

import pyeq2
import DataForUnitTests

import numpy
numpy.seterr(all= 'ignore')


class mockModel(object):
    
    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        self.dataCache = pyeq2.dataCache()
    
    def ShouldDataBeRejected(self, inModel):
        return False

    def GetDimensionality(self):
        return self._dimensionality


service = pyeq2.Services.DataConverterService.DataConverterService()



class TestConversions(unittest.TestCase):
    
    def test_ConversionOfColumns_ASCII_2D_NoWeights_ExampleData(self):
        converted_IndepData_ShouldBe = numpy.array([[5.357, 5.457, 5.797, 5.936, 6.161, 6.697, 6.731, 6.775, 8.442, 9.769, 9.861],
                                                    [1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]])
        converted_DepData_ShouldBe = numpy.array([0.376, 0.489, 0.874, 1.049, 1.327, 2.054, 2.077, 2.138, 4.744, 7.068, 7.104])
        converted_Weights_ShouldBe = None
        model = mockModel('SSQABS')
        model._dimensionality = 2
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInColumns_2D, model, False)
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['DependentData'], converted_DepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['IndependentData'], converted_IndepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Weights'], converted_Weights_ShouldBe).all())
    
    def test_ConversionOfColumns_ASCII_2D_NoWeights(self):
        converted_IndepData_ShouldBe = numpy.array([[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
                                                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
        converted_DepData_ShouldBe = numpy.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
        converted_Weights_ShouldBe = None
        model = mockModel('SSQABS')
        model._dimensionality = 2
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns, model, False)
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['DependentData'], converted_DepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['IndependentData'], converted_IndepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Weights'], converted_Weights_ShouldBe).all())
    
    def test_ConversionOfColumns_ASCII_2D_Weights(self):
        converted_IndepData_ShouldBe = numpy.array([[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
                                                  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
        converted_DepData_ShouldBe = numpy.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
        converted_Weights_ShouldBe = numpy.array([3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9])
        model = mockModel('SSQABS')
        model._dimensionality = 2
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns, model, True)
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['DependentData'], converted_DepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['IndependentData'], converted_IndepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Weights'], converted_Weights_ShouldBe).all())


    def test_ConversionOfColumns_ASCII_3D_NoWeights(self):
        converted_IndepData_ShouldBe = numpy.array([[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
                                                  [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]])
        converted_DepData_ShouldBe = numpy.array([3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9])
        converted_Weights_ShouldBe = None
        model = mockModel('SSQABS')
        model._dimensionality = 3
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns, model, False)
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['DependentData'], converted_DepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['IndependentData'], converted_IndepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Weights'], converted_Weights_ShouldBe).all())


    def test_ConversionOfColumns_ASCII_3D_Weights(self):
        converted_IndepData_ShouldBe = numpy.array([[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
                                                  [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]])
        converted_DepData_ShouldBe = numpy.array([3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9])
        converted_Weights_ShouldBe = numpy.array([4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9])
        model = mockModel('SSQABS')
        model._dimensionality = 3
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns, model, True)
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['DependentData'], converted_DepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['IndependentData'], converted_IndepData_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Weights'], converted_Weights_ShouldBe).all())



if __name__ == '__main__':
    unittest.main()
