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

import numpy
numpy.seterr(all= 'ignore')



class DataCache(object):
    
    def __init__(self):
        self.reducedDataCacheDictionary = {}
        self.allDataCacheDictionary = {}
        

    def GenerateReducedRawData(self, inModel):
        # find the array indices for the max and min values of each data dimension in the full data set
        minXindex = 0
        maxXindex = 0
        minYindex = 0
        maxYindex = 0
        minZindex = 0
        maxZindex = 0
        for i in range(len(self.allDataCacheDictionary['DependentData'])):
            if self.allDataCacheDictionary['IndependentData'][0][i] < self.allDataCacheDictionary['IndependentData'][0][minXindex]:
                minXindex = i
            if self.allDataCacheDictionary['IndependentData'][0][i] > self.allDataCacheDictionary['IndependentData'][0][maxXindex]:
                maxXindex = i
            if inModel.GetDimensionality() == 3:
                if self.allDataCacheDictionary['IndependentData'][1][i] < self.allDataCacheDictionary['IndependentData'][1][minYindex]:
                    minYindex = i
                if self.allDataCacheDictionary['IndependentData'][1][i] > self.allDataCacheDictionary['IndependentData'][1][maxYindex]:
                    maxYindex = i
            if self.allDataCacheDictionary['DependentData'][i] < self.allDataCacheDictionary['DependentData'][minZindex]:
                minZindex = i
            if self.allDataCacheDictionary['DependentData'][i] > self.allDataCacheDictionary['DependentData'][maxZindex]:
                maxZindex = i

        # now make an array of the *indices* we will use in the reduced data set.
        # NO duplicate entries desired, so use "if value X not in list Y" logic
        indexList = []
        if minXindex not in indexList:
            indexList.append(minXindex)
        if maxXindex not in indexList:
            indexList.append(maxXindex)
        if inModel.GetDimensionality() == 3:
            if minYindex not in indexList:
                indexList.append(minYindex)
            if maxYindex not in indexList:
                indexList.append(maxYindex)
        if minZindex not in indexList:
            indexList.append(minZindex)
        if maxZindex not in indexList:
            indexList.append(maxZindex)

        # if we have have not selected all data points, draw more data point indices
        if len(self.allDataCacheDictionary['DependentData']) > len(indexList):
            for i in range(inModel.numberOfReducedDataPoints):
                index = i * len(self.allDataCacheDictionary['DependentData']) / inModel.numberOfReducedDataPoints
                if index not in indexList:
                    indexList.append(index)
        indexList.sort()
                    
        # now that we have all the locations (indices) of the data points in the reduced
        # data set, draw those points from the full data set and make our reduced data cache
        independentData = [[],[]]
        dependentData = []
        for i in indexList:
            independentData[0].append(self.allDataCacheDictionary['IndependentData'][0][i])
            if inModel.GetDimensionality() == 3:
                independentData[1].append(self.allDataCacheDictionary['IndependentData'][1][i])
            dependentData.append(self.allDataCacheDictionary['DependentData'][i])
        if inModel.GetDimensionality() == 2:
            self.reducedDataCacheDictionary['IndependentData'] = numpy.array([independentData[0], numpy.ones_like(independentData[0])])
        else:
            self.reducedDataCacheDictionary['IndependentData'] = numpy.array(independentData)
        self.reducedDataCacheDictionary['DependentData'] = numpy.array(dependentData)


    def FindOrCreateCache_CommonCode(self, inCacheDictionary, inModel):
        returnCacheDataList = []
        for dataCacheFunction in inModel.GetDataCacheFunctions():
            # if this item is not in the inCacheDictionary, create it and add it to the inCacheDictionary
            if not inCacheDictionary.has_key(dataCacheFunction[0]):
                # strip any numbers from the end of the string
                s = dataCacheFunction[0] # name, including any ending name info
                found = 1
                while found:
                    found = 0
                    lastchar = s[len(s)-1]
                    if lastchar.isdigit() or lastchar == '_' or lastchar == '.' or lastchar == '-' or lastchar == '[' or lastchar == ']' or lastchar == ',' or lastchar == ' ':
                        found = 1
                        s = s[:-1]
                numpy.seterr(all= 'raise') # DataCache functions trap numpy exceptions
                cacheItem = getattr(pyeq2.DataCache.DataCacheFunctions, s)(inCacheDictionary['IndependentData'], dataCacheFunction[1], inModel)
                numpy.seterr(all= 'ignore')
                if not numpy.all(numpy.isfinite(cacheItem)):
                    raise Exception('Error creating data cache for cache function ' + s + '(): could not calculate value. This is usually caused by taking the the exponent of a large number.')
                inCacheDictionary[dataCacheFunction[0]] = cacheItem
            returnCacheDataList.append(inCacheDictionary[dataCacheFunction[0]])
        return numpy.array(returnCacheDataList)

            
    def CalculateNumberOfReducedDataPoints(self, inModel):
        inModel.numberOfReducedDataPoints = len(inModel.GetCoefficientDesignators()) * 3 * inModel.GetDimensionality()
        # if the number of reduced data points is greater than
        # the number of all data points, use the "all data" cache
        if inModel.numberOfReducedDataPoints > len(self.allDataCacheDictionary['DependentData']):
            inModel.numberOfReducedDataPoints = len(self.allDataCacheDictionary['DependentData'])
            
        # if the number of data points in the all data set is not ~1.5 times greater than the
        # number of data points in the reduced data set, just use the all data set directly
        if (1.5 * inModel.numberOfReducedDataPoints) >= len(self.allDataCacheDictionary['DependentData']):
            inModel.numberOfReducedDataPoints = len(self.allDataCacheDictionary['DependentData'])
        
        
    def FindOrCreateReducedDataCache(self, inModel):
        self.CalculateNumberOfReducedDataPoints(inModel)
        
        # if the number of all data points and the number of reduced data points are equal, caches are equal
        if len(self.allDataCacheDictionary['DependentData']) == inModel.numberOfReducedDataPoints:
            self.reducedDataCacheDictionary = self.allDataCacheDictionary

        # if the reduced data cache does not yet have reduced raw data, generate it and add to the cache
        if not self.reducedDataCacheDictionary.has_key('DependentData'):
            self.GenerateReducedRawData(inModel)

        return self.FindOrCreateCache_CommonCode(self.reducedDataCacheDictionary, inModel)


    def FindOrCreateAllDataCache(self, inModel):
        return self.FindOrCreateCache_CommonCode(self.allDataCacheDictionary, inModel)
