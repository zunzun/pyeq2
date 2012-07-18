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
    
    # these are taken from docs for scipy.optimize.minimize, except for 'Levenberg=Marquardt'.
    # The algorithms 'L-BFGS-B' and 'TNC' are not on the list as they are bounded versions of other algorithms listed here.
    ListOfNonLinearSolverAlgorithmNames = ['Levenberg-Marquardt','NelderMead','Powell','CG','BFGS','Newton-CG','Anneal','COBYLA','SLSQP']
    
    
    def __init__(self):
        self.fminIterationLimit = 2500
        self.fmin_xtol = 1.0E-16
        self.fmin_ftol = 1.0E-16
        self.fmin_FunctionLimit = 2500
        

    def ResultListSortFunction(self, a, b): # utility function
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        return 0


    def SolveUsingLinear(self, inModel):
        if (inModel.CanLinearSolverBeUsedForSSQABS()) == False and (inModel.fittingTarget == "SSQABS"):
            raise Excpetion, 'This equation cannot use a linear SSQ solver'
        inModel.solvedCoefficients = numpy.linalg.lstsq(inModel.dataCache.FindOrCreateAllDataCache(inModel).T, inModel.dataCache.allDataCacheDictionary['DependentData'])[0]
        return inModel.solvedCoefficients


    def SolveUsingSimplex(self, inModel):
        inModel.dataCache.FindOrCreateAllDataCache(inModel)
        inModel.solvedCoefficients = scipy.optimize.fmin(inModel.CalculateAllDataFittingTarget, inModel.estimatedCoefficients, maxiter = len(inModel.estimatedCoefficients) * self.fminIterationLimit, maxfun = len(inModel.estimatedCoefficients) * self.fmin_FunctionLimit, disp = 0, xtol=self.fmin_xtol, ftol=self.fmin_ftol)
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
        
        inModel.solvedCoefficients = de.best_vector
        return inModel.solvedCoefficients


    def SolveUsingSelectedAlgorithm(self, inModel, inAlgorithmName):
        
        if inAlgorithmName not in self.ListOfNonLinearSolverAlgorithmNames:
            raise Exception('"' + inAlgorithmName + '" was not in the list of known non-linear solver algorithm names.  Please see the SolverService class definition.')

        inModel.dataCache.FindOrCreateAllDataCache(inModel)
        inModel.dataCache.FindOrCreateReducedDataCache(inModel)

        results = []
        # try with initial coefficients equal to 1
        try:
            if inAlgorithmName == 'Levenberg-Marquardt':
                coeffs, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], numpy.ones(len(inModel.GetCoefficientDesignators())), maxfev=1000000)
            else:
                coeffs = scipy.optimize.minimize(inModel.CalculateAllDataFittingTarget, numpy.ones(len(inModel.GetCoefficientDesignators())), method=inAlgorithmName, maxiter = len(inModel.estimatedCoefficients) * self.fminIterationLimit, disp = 0)
            SSQ = inModel.CalculateAllDataFittingTarget(coeffs)
            results.append([SSQ, coeffs])
        except:
            pass
            
        # try with initial coefficients from DE
        try:
            if inAlgorithmName == 'Levenberg-Marquardt':
                coeffs, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], inModel.deEstimatedCoefficients, maxfev=1000000) # initial coefficients are all equal to 1
            else:
                coeffs = scipy.optimize.minimize(inModel.CalculateAllDataFittingTarget, inModel.deEstimatedCoefficients, method=inAlgorithmName, maxiter = len(inModel.estimatedCoefficients) * self.fminIterationLimit, disp = 0)
            SSQ = inModel.CalculateAllDataFittingTarget(coeffs)
            results.append([SSQ, coeffs])
        except:
            pass
                
        # try using estimated coefficients, if any
        if len(inModel.estimatedCoefficients) > 0:
            try:
                coeffs = inModel.estimatedCoefficients
                SSQ = inModel.CalculateAllDataFittingTarget(coeffs)
                results.append([SSQ, coeffs])
            except:
                pass
                
            try:
                if inAlgorithmName == 'Levenberg-Marquardt':
                    coeffs, unused = scipy.optimize.curve_fit(inModel.WrapperForScipyCurveFit, None, inModel.dataCache.allDataCacheDictionary['DependentData'], inModel.estimatedCoefficients, maxfev=1000000)
                else:
                    coeffs = scipy.optimize.minimize(inModel.CalculateAllDataFittingTarget, inModel.estimatedCoefficients, method=inAlgorithmName, maxiter = len(inModel.estimatedCoefficients) * self.fminIterationLimit, disp = 0)
                SSQ = inModel.CalculateAllDataFittingTarget(coeffs)
                results.append([SSQ, coeffs])
            except:
                pass
                
        if results == []:
            return numpy.ones(len(inModel.GetCoefficientDesignators()))
        
        if len(results) > 1:
            results.sort(self.ResultListSortFunction)
            
        inModel.solvedCoefficients = results[0][1]
        return inModel.solvedCoefficients


    def SolveUsingODR(self, inModel):

        data = inModel.dataCache.FindOrCreateAllDataCache(inModel)
        modelObject = scipy.odr.odrpack.Model(inModel.WrapperForODR)
        if len(inModel.dataCache.allDataCacheDictionary['Weights']):
            dataObject = scipy.odr.odrpack.Data(inModel.dataCache.allDataCacheDictionary['IndependentData'], inModel.dataCache.allDataCacheDictionary['DependentData'], inModel.dataCache.allDataCacheDictionary['Weights'])
        else:
            dataObject = scipy.odr.odrpack.Data(inModel.dataCache.allDataCacheDictionary['IndependentData'], inModel.dataCache.allDataCacheDictionary['DependentData'])
        
        results = []
        
        # try with initial coefficients equal to 1
        try:
            myodr = scipy.odr.odrpack.ODR(dataObject, modelObject, beta0=numpy.ones(len(inModel.GetCoefficientDesignators())),  maxit=len(inModel.GetCoefficientDesignators()) * self.fminIterationLimit)
            myodr.set_job(fit_type=0, deriv=0) # explicit ODR, faster forward-only finite differences for derivatives
            out = myodr.run()
            coeffs = out.beta
            SSQ = out.sum_square
            if not numpy.any(numpy.isnan(coeffs)):
                results.append([SSQ, coeffs])
        except:
            pass
            
        # try with initial coefficients from DE
        try:
            myodr = scipy.odr.odrpack.ODR(dataObject, modelObject, beta0=inModel.deEstimatedCoefficients,  maxit=len(inModel.GetCoefficientDesignators()) * self.fminIterationLimit)
            myodr.set_job(fit_type=0, deriv=0) # explicit ODR, faster forward-only finite differences for derivatives
            out = myodr.run()
            coeffs = out.beta
            SSQ = out.sum_square
            if not numpy.any(numpy.isnan(coeffs)):
                results.append([SSQ, coeffs])
        except:
            pass
            
        # try using estimated coefficients, if any
        if len(inModel.estimatedCoefficients) > 0:
            try:
                coeffs = inModel.estimatedCoefficients
                SSQ = inModel.CalculateAllDataFittingTarget(coeffs)
                results.append([SSQ, coeffs])
            except:
                pass
                
            try:
                myodr = scipy.odr.odrpack.ODR(dataObject, modelObject, beta0=inModel.estimatedCoefficients,  maxit=len(inModel.GetCoefficientDesignators()) * self.fminIterationLimit)
                myodr.set_job(fit_type=0, deriv=0) # explicit ODR, faster forward-only finite differences for derivatives
                out = myodr.run()
                coeffs = out.beta
                SSQ = out.sum_square
                if not numpy.any(numpy.isnan(coeffs)):
                    results.append([SSQ, coeffs])
            except:
                pass
                
        if results == []:
            return numpy.ones(len(inModel.GetCoefficientDesignators()))
        
        if len(results) > 1:
            results.sort(self.ResultListSortFunction)
            
        inModel.solvedCoefficients = results[0][1]
        return inModel.solvedCoefficients



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
