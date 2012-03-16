#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2012 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)
#    Version info: $Id$

import numpy, scipy.interpolate, scipy.optimize, scipy.odr.odrpack, copy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them

import pyeq2
import diffev

class custom_prng_for_diffev(numpy.random.mtrand.RandomState):
    
    def __init__(self):
        numpy.random.mtrand.RandomState.__init__(self)
        numpy.random.seed(3) # yield repeatable results
        self.max_index = 5000
        self.array = numpy.random.rand(self.max_index)
        self.index = 0

    
    def rand(self, inSize):
        if self.index + inSize > self.max_index:
            self.index = 0
        return_val = self.array[self.index:self.index + inSize]
        self.index += inSize
        return return_val



class SolverService(object):
    
    def __init__(self):
        self.fminIterationLimit = 2500


    def SolveUsingLinear(self, inModel):
        if (inModel.CanLinearSolverBeUsedForSSQABS()) == False and (inModel.fittingTarget == "SSQABS"):
            raise Excpetion, 'This equation cannot use a linear SSQ solver'
        inModel.solvedCoefficients = numpy.linalg.lstsq(inModel.dataCache.FindOrCreateAllDataCache(inModel).T, inModel.dataCache.allDataCacheDictionary['DependentData'])[0]
        return inModel.solvedCoefficients


    def SolveUsingSimplex(self, inModel):
        fmin_xtol = 1.0E-16
        fmin_ftol = 1.0E-16
        fmin_FunctionLimit = 2500
        inModel.dataCache.FindOrCreateAllDataCache(inModel)
        inModel.solvedCoefficients = scipy.optimize.fmin(inModel.CalculateAllDataFittingTarget, inModel.estimatedCoefficients, maxiter = len(inModel.estimatedCoefficients) * self.fminIterationLimit, maxfun = len(inModel.estimatedCoefficients) * fmin_FunctionLimit, disp = 0, xtol=fmin_xtol, ftol=fmin_ftol)
        return inModel.solvedCoefficients


    def SolveUsingDE(self, inModel): # adapts to number of coefficients
        crossoverProbabilityForGA = 0.6
        diffScaleForGA = 0.9
        
        numberOfCoefficients = len(inModel.GetCoefficientDesignators())
        
        oneThirdOfPopulationSizeForGA = 25 * numberOfCoefficients
        if oneThirdOfPopulationSizeForGA > 100:
            oneThirdOfPopulationSizeForGA = 100 
        
        maxGenerationsForGA = 10 * numberOfCoefficients
        if maxGenerationsForGA > 25:
            maxGenerationsForGA = 25

        guessDivisorForGA = 2.0 * numberOfCoefficients
        if guessDivisorForGA > 10.0:
            guessDivisorForGA = 10.0

        inModel.dataCache.FindOrCreateReducedDataCache(inModel)
        
        numpy.random.seed(3) # yield repeatable results
        largeValuesArray = numpy.random.random(oneThirdOfPopulationSizeForGA * numberOfCoefficients) * 2000.0 - 1000.0
        smallValuesArray = numpy.random.random(oneThirdOfPopulationSizeForGA * numberOfCoefficients) * 2.0 - 1.0
        tinyValuesArray = numpy.random.random(oneThirdOfPopulationSizeForGA * numberOfCoefficients) * .002 - .001
        pop0 = numpy.append(largeValuesArray, numpy.append(smallValuesArray, tinyValuesArray))
        numpy.random.shuffle(pop0)
        pop0 = pop0.reshape(oneThirdOfPopulationSizeForGA * 3, numberOfCoefficients)

        if inModel.estimatedCoefficients != []:
            pop0[0] = copy.deepcopy(inModel.estimatedCoefficients) # DE will overwrite these values, so use deepcopy
            
        depData = inModel.dataCache.reducedDataCacheDictionary['DependentData']
        sufficientSolution = (max(depData) - min(depData)) / guessDivisorForGA
        de = diffev.DiffEvolver(inModel.CalculateReducedDataFittingTarget, pop0, crossover_rate = crossoverProbabilityForGA, scale = diffScaleForGA, strategy = ('best', 1, 'bin'), prng = custom_prng_for_diffev())
        de.solve(sufficientSolution, maxGenerationsForGA)
        return de.best_vector


    def SolveUsingLevenbergMarquardt(self, inModel):
        LM1 = None
        LM2 = None
        SSQ1 = 1.0E300
        SSQ2 = 1.0E300
            
        inModel.dataCache.FindOrCreateAllDataCache(inModel)
        inModel.dataCache.FindOrCreateReducedDataCache(inModel)

        results = []
        # first try is with initial coefficients are equal to 1
        try:
            LM1, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], numpy.ones(len(inModel.GetCoefficientDesignators())), maxfev=1000000) # initial coefficients are all equal to 1
            SSQ1 = inModel.CalculateAllDataFittingTarget(LM1)
            results.append([SSQ1, LM1])
        except:
            LM1 = None
            SSQ1 = 1.0E300
            
        # next try is with initial coefficients from DE
        try:
            LM2, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], inModel.deEstimatedCoefficients, maxfev=1000000) # initial coefficients are all equal to 1
            SSQ2 = inModel.CalculateAllDataFittingTarget(LM2)
            results.append([SSQ2, LM2])
        except:
            LM2 = None
            SSQ2 = 1.0E300
                
        # now try using estimated coefficients, if any
        if len(inModel.estimatedCoefficients) > 0:
            estimatedOK = False
            try:
                LM3 = inModel.estimatedCoefficients
                SSQ3 = inModel.CalculateAllDataFittingTarget(LM3)
                results.append([SSQ3, LM3])
            except:
                LM3 = None
                SSQ3 = 1.0E300
            try:
                LM4, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], inModel.estimatedCoefficients, maxfev=1000000)
                SSQ4 = inModel.CalculateAllDataFittingTarget(LM4)
                results.append([SSQ4, LM4])
            except:
                LM4 = None
                SSQ4 = 1.0E300
                
        if results == []:
            return numpy.ones(len(inModel.GetCoefficientDesignators()))
        
        if len(results) > 1:
            results.sort(self.ResultListSortFunction)
            
        return results[0][1]


    def ResultListSortFunction(selg, a, b): # utility function
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        return 0



    def SolveUsingSpline(self, inModel):
        data = inModel.dataCache.FindOrCreateAllDataCache(inModel)
        if inModel.GetDimensionality() == 2:
            inModel.scipySpline = scipy.interpolate.fitpack2.UnivariateSpline(data[0], inModel.dataCache.allDataCacheDictionary['DependentData'], s=inModel.smoothingFactor, k=inModel.xOrder)
            inModel.solvedCoefficients = inModel.scipySpline._eval_args
            return inModel.solvedCoefficients
        else:
            inModel.scipySpline = scipy.interpolate.fitpack2.SmoothBivariateSpline(data[0], data[1], inModel.dataCache.allDataCacheDictionary['DependentData'], s=inModel.smoothingFactor, kx=inModel.xOrder, ky=inModel.yOrder)
            inModel.solvedCoefficients = inModel.scipySpline.tck
            return inModel.solvedCoefficients


    def SolveUsingODR(self, inModel):
        ODR1 = None
        SSQ1 = 1.0E300
        ODR2 = None
        SSQ2 = 1.0E300

        data = inModel.dataCache.FindOrCreateAllDataCache(inModel)
        modelObject = scipy.odr.odrpack.Model(inModel.WrapperForODR)
        dataObject = scipy.odr.odrpack.Data(inModel.dataCache.allDataCacheDictionary['IndependentData'], inModel.dataCache.allDataCacheDictionary['DependentData'])
        
        # first try is with initial coefficients are equal to 1
        myodr = scipy.odr.odrpack.ODR(dataObject, modelObject, beta0=numpy.ones(len(inModel.GetCoefficientDesignators())),  maxit=len(inModel.GetCoefficientDesignators()) * self.fminIterationLimit)
        myodr.set_job(fit_type=0, deriv=0) # explicit ODR, faster forward-only finite differences for derivatives
        out = myodr.run()
        ODR1 = out.beta
        SSQ1 = out.sum_square
        if numpy.any(numpy.isnan(ODR1)):
            ODR1 = None
            SSQ1 = 1.0E300
            
        # now try using estimated coefficients, if any
        if len(inModel.estimatedCoefficients) > 0:
            myodr = scipy.odr.odrpack.ODR(dataObject, modelObject, beta0=inModel.estimatedCoefficients,  maxit=len(inModel.GetCoefficientDesignators()) * self.fminIterationLimit)
            myodr.set_job(fit_type=0, deriv=0) # explicit ODR, faster forward-only finite differences for derivatives
            out = myodr.run()
            ODR2 = out.beta
            SSQ2 = out.sum_square
            if numpy.any(numpy.isnan(ODR1)):
                ODR2 = None
                SSQ2 = 1.0E300

        if SSQ2 > SSQ1:
            inModel.solvedCoefficients = ODR1
            return inModel.solvedCoefficients
        else:
            inModel.solvedCoefficients = ODR2
            return inModel.solvedCoefficients
