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

import StringIO # cStringIO is not safe for Unicode comments, use StringIO instead

import numpy
numpy.seterr(all= 'ignore')


class DataConverterService(object):


    # data is in columns
    def ConvertAndSortColumnarASCII(self, inRawData, inModel, inUseWeightsFlag):
        # you should first process commas before calling this method,
        # as it uses the default token delimiters in string split()
        #
        # For example, convert $1,234.56 to 1234.56 or 1,23 to 1.23
        # Different number systems have commas in different places
        # and the Python built-in float() method uses decimal notation
        # or scientific notation only

        # cache some data set characteristics for later use,
        # these are for the data domains of individual equations
        inModel.dataCache.independentData1ContainsZeroFlag = False
        inModel.dataCache.independentData2ContainsZeroFlag = False
        inModel.dataCache.independentData1ContainsPositiveFlag = False
        inModel.dataCache.independentData2ContainsPositiveFlag = False
        inModel.dataCache.independentData1ContainsNegativeFlag = False
        inModel.dataCache.independentData2ContainsNegativeFlag = False

        # used in calculation of relative error to prevent divide-by-zero exceptions
        inModel.dataCache.DependentDataContainsZeroFlag = False

        if inUseWeightsFlag:
            minimumNumberOfTokens = inModel.GetDimensionality() + 1
        else:
            minimumNumberOfTokens = inModel.GetDimensionality()

        # StringIO() allows using file methods on text
        rawData = StringIO.StringIO(inRawData).readlines()

        # OK, now load in the data
        dataLists = [[], [], [], []]
        for line in rawData:

            # split the line into string tokens using the default string split() delimiters
            tokenlist = line.split()

            # test this line for minimum required number of string tokens
            if len(tokenlist) < minimumNumberOfTokens:
                continue

            # use the python built-in float() conversion and discard if any exceptions
            if inModel.GetDimensionality() == 1:
                try:
                    a = float(tokenlist[0])
                except:
                    continue
                if a > 1.0E300 or a < -1.0E300:
                    continue
                if a < 0.0:
                    inModel.dataCache.independentData1ContainsNegativeFlag = True
                elif a > 0.0:
                    inModel.dataCache.independentData1ContainsPositiveFlag = True
                else:
                    inModel.dataCache.independentData1ContainsZeroFlag = True

                dataLists[0].append(a)
                dataLists[1].append(1.0)
                dataLists[2].append(1.0)
                dataLists[3].append(1.0)

            if inModel.GetDimensionality() == 2:
                try:
                    a = float(tokenlist[0])
                    b = float(tokenlist[1])
                    if inUseWeightsFlag:
                        c = float(tokenlist[2])
                    else:
                        c = 1.0
                    d = 1.0
                    
                except:
                    continue
                if a > 1.0E300 or a < -1.0E300:
                    continue
                if b > 1.0E300 or b < -1.0E300:
                    continue
                if b == 0.0:
                    inModel.dataCache.DependentDataContainsZeroFlag = True
                if a < 0.0:
                    inModel.dataCache.independentData1ContainsNegativeFlag = True
                elif a > 0.0:
                    inModel.dataCache.independentData1ContainsPositiveFlag = True
                else:
                    inModel.dataCache.independentData1ContainsZeroFlag = True
                
                dataLists[0].append(c)
                dataLists[1].append(d)
                dataLists[2].append(a)
                dataLists[3].append(b)

            if inModel.GetDimensionality() == 3:
                try:
                    a = float(tokenlist[0])
                    b = float(tokenlist[1])
                    c = float(tokenlist[2])
                    if inUseWeightsFlag:
                        d = float(tokenlist[3])
                    else:
                        d = 1.0
                except:
                    continue
                if a > 1.0E300 or a < -1.0E300:
                    continue
                if b > 1.0E300 or b < -1.0E300:
                    continue
                if c > 1.0E300 or c < -1.0E300:
                    continue
                if c == 0.0:
                    inModel.dataCache.DependentDataContainsZeroFlag = True
                if a < 0.0:
                    inModel.dataCache.independentData1ContainsNegativeFlag = True
                elif a > 0.0:
                    inModel.dataCache.independentData1ContainsPositiveFlag = True
                else:
                    inModel.dataCache.independentData1ContainsZeroFlag = True
                if b < 0.0:
                    inModel.dataCache.independentData2ContainsNegativeFlag = True
                elif b > 0.0:
                    inModel.dataCache.independentData2ContainsPositiveFlag = True
                else:
                    inModel.dataCache.independentData2ContainsZeroFlag = True

                dataLists[0].append(d)
                dataLists[1].append(a)
                dataLists[2].append(b)
                dataLists[3].append(c)
                
        if inModel.ShouldDataBeRejected(inModel) == True:
            raise Exception(inModel.reasonWhyDataRejected)
            
        if inModel.GetDimensionality() == 1:
            dataLists[0].sort()
            inModel.dataCache.allDataCacheDictionary['IndependentData'] = [numpy.array(dataLists[0]), dataLists[1]]
            return
            
        arrayLists = numpy.array(dataLists) # for sorting all data by values of dependent variable
        indices = numpy.argsort(arrayLists[3])

        inModel.dataCache.allDataCacheDictionary['DependentData'] = numpy.array(arrayLists[3][indices])
        
        if inModel.GetDimensionality() == 2:
            inModel.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([arrayLists[2][indices], numpy.ones(len(arrayLists[0]))]) # the second  _unused_  list is for a bug in scipy.odr, which is used to calculate standard errors on parameters
        if inModel.GetDimensionality() == 3:
            inModel.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([arrayLists[1][indices], arrayLists[2][indices]])
            
        if inUseWeightsFlag:
            inModel.dataCache.allDataCacheDictionary['Weights'] = numpy.array(arrayLists[0][indices])
        else:
            inModel.dataCache.allDataCacheDictionary['Weights'] = []


    def ConvertNumpyArrays(self, inRawData, inModel):
        pass


    def ConvertPythonSequences(self, inRawData, inModel):
        pass
