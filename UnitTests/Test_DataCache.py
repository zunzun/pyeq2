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


class mockModel_2D(object):
    
    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        self.dataCache = pyeq2.dataCache()
        self._dimensionality = 2
        
    def GetCoefficientDesignators(self):
        return ['a', 'b']
        
    def GetDimensionality(self):
        return self._dimensionality
        
    def ShouldDataBeRejected(self, inModel):
        return False

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.ExpX(NameOrValueFlag=1), []])
        return functionList


class mockModel_3D(object):

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        self.dataCache = pyeq2.dataCache()
        self._dimensionality = 3
    
    def GetCoefficientDesignators(self):
        return ['a', 'b', 'c']

    def GetDimensionality(self):
        return self._dimensionality
        
    def ShouldDataBeRejected(self, inModel):
        return False

    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Ones(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1, args=[2.0]), [2.0]])
        return functionList


service = pyeq2.Services.DataConverterService.DataConverterService()



class TestDataCache(unittest.TestCase):
    
    def test_ReducedDataSize_2D(self):
        model = mockModel_2D('SSQABS')
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiIntegerDataInColumns, model, False)
        model.dataCache.FindOrCreateReducedDataCache(model)
        self.assertEqual(len(model.dataCache.reducedDataCacheDictionary['X']), 13)
    
    
    def test_DataCache_2D(self):
        cached_X_ShouldBe = numpy.array([3.017, 0.742, 0.607, 2.822])
        cached_ExpX_ShouldBe = numpy.exp(numpy.array([3.017, 0.742, 0.607, 2.822]))
        
        model = mockModel_2D('SSQABS')
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns_small, model, False)
        model.dataCache.FindOrCreateAllDataCache(model)
        model.dataCache.FindOrCreateReducedDataCache(model)
        
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['X'], cached_X_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['ExpX'], cached_ExpX_ShouldBe).all())
        
        self.assertTrue(numpy.equal(model.dataCache.reducedDataCacheDictionary['X'], cached_X_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.reducedDataCacheDictionary['ExpX'], cached_ExpX_ShouldBe).all())


    def test_DataCache_3D(self):
        cached_X_ShouldBe = numpy.array([3.017, 0.607, 0.742, 2.822])
        cached_Y_ShouldBe = numpy.array([2.175, 2.571, 2.568, 2.624])
        
        model = mockModel_3D('SSQABS')
        service.ConvertAndSortColumnarASCII(DataForUnitTests.asciiDataInFourColumns_small, model, False)
        model.dataCache.FindOrCreateAllDataCache(model)
        model.dataCache.FindOrCreateReducedDataCache(model)
        
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['X'], cached_X_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.allDataCacheDictionary['Y'], cached_Y_ShouldBe).all())

        self.assertTrue(numpy.equal(model.dataCache.reducedDataCacheDictionary['X'], cached_X_ShouldBe).all())
        self.assertTrue(numpy.equal(model.dataCache.reducedDataCacheDictionary['Y'], cached_Y_ShouldBe).all())



if __name__ == '__main__':
    unittest.main()
