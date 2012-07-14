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

import pyeq2

import numpy, scipy.interpolate, scipy.stats
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them



class IModel(object):
    splineFlag = False
    userSelectablePolynomialFlag = False
    userSelectablePolyfunctionalFlag = False
    userSelectableRationalFlag = False
    userDefinedFunctionFlag = False

    # "e" is removed so it is not mistaken for Euler's constant "e"
    # "l" is removed so it is not mistaken for the number "1" - some fonts make these appear the same or very similar
    # "o" is removed so it is not mistaken for the number "0" - some fonts make these appear the same or very similar
    # VBA is case insensitive, so coefficient 'a' looks the same to VBA as coefficient 'A' - use double characters instead of capital letters
    # "x", "y", "xx", and "yy" are removed so they are not mistaken for variables named x or y
    listOfAdditionalCoefficientDesignators = ['a','b','c','d','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','z','aa','bb','cc','dd','ff','gg','hh','ii','jj','kk','mm','nn','pp','qq','rr','ss','tt','uu','vv','ww','zz']
    
    fittingTargetDictionary = {'SSQABS': 'sum of squared absolute error',
                               'SSQREL': 'sum of squared relative error',
                               'ODR':    'sum of squared orthogonal distance',
                               'ABSABS': 'sum of absolute value of absolute error',
                               'ABSREL': 'sum of absolute value of relative error',
                               'PEAKABS':'peak absolute value of absolute error',
                               'PEAKREL':'peak absolute value of relative error',
                               'AIC':    'Akaike Information Criterion',
                               'BIC':    'Bayesian Information Criterion'
                              }
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        if inExtendedVersionName == '':
            inExtendedVersionName = 'Default'
            
        if inFittingTarget not in self.fittingTargetDictionary.keys():
            raise Exception, str(inFittingTarget) + ' is not in the IModel class fitting target dictionary.'
        
        self.extendedVersionHandler = eval('pyeq2.ExtendedVersionHandlers.ExtendedVersionHandler_' + inExtendedVersionName.replace(' ', '') + '.ExtendedVersionHandler_' + inExtendedVersionName.replace(' ', '') + '()')
        
        self.dataCache = pyeq2.dataCache()
        self.upperCoefficientBounds = []
        self.lowerCoefficientBounds = []
        self.estimatedCoefficients = []
        self.fixedCoefficients = []
        self.solvedCoefficients = []
        self.polyfunctional2DFlags = []
        self.polyfunctional3DFlags = []
        self.xPolynomialOrder = None
        self.yPolynomialOrder = None
        self.rationalNumeratorFlags = []
        self.rationalDenominatorFlags = []
        self.fittingTarget = inFittingTarget
        self.deEstimatedCoefficients = []

        
        self.independentData1CannotContainZeroFlag = False
        self.independentData1CannotContainPositiveFlag = False
        self.independentData1CannotContainNegativeFlag = False
        self.independentData2CannotContainZeroFlag = False
        self.independentData2CannotContainPositiveFlag = False
        self.independentData2CannotContainNegativeFlag = False
        
        try:
            if self._dimensionality == 2:
                self.exampleData = '''
    X        Y
  5.357    0.376
  5.457    0.489
  5.797    0.874
  5.936    1.049
  6.161    1.327
  6.697    2.054
  6.731    2.077
  6.775    2.138
  8.442    4.744
  9.769    7.068
  9.861    7.104
'''
            else:
                self.exampleData = '''
    X      Y       Z
  3.017  2.175   0.320
  2.822  2.624   0.629
  2.632  2.839   0.950
  2.287  3.030   1.574
  2.207  3.057   1.725
  2.048  3.098   2.035
  1.963  3.115   2.204
  1.784  3.144   2.570
  1.712  3.153   2.721
  2.972  2.106   0.313
  2.719  2.542   0.643
  2.495  2.721   0.956
  2.070  2.878   1.597
  1.969  2.899   1.758
  1.768  2.929   2.088
  1.677  2.939   2.240
  1.479  2.957   2.583
  1.387  2.963   2.744
  2.843  1.984   0.315
  2.485  2.320   0.639
  2.163  2.444   0.954
  1.687  2.525   1.459
  1.408  2.547   1.775
  1.279  2.554   1.927
  1.016  2.564   2.243
  0.742  2.568   2.581
  0.607  2.571   2.753
'''
        except:
            pass


    def CalculateCoefficientAndFitStatistics(self):
        # ensure integers are promoted to floating point with "1.0 * var"
        self.nobs = 1.0 * len(self.dataCache.allDataCacheDictionary['DependentData'])  # number of observations
        self.ncoef = 1.0 * len(self.solvedCoefficients)          # number of coef.
        self.df_e = self.nobs - self.ncoef                 # degrees of freedom, error
        self.df_r = self.ncoef - 1.0                              # degrees of freedom, regression
        self.sumOfSquaredErrors = numpy.sum(self.modelAbsoluteError * self.modelAbsoluteError)

        try:
            self.r2 = 1.0 - self.modelAbsoluteError.var()/self.dataCache.allDataCacheDictionary['DependentData'].var()
        except:
            self.r2 = None

        try:
            self.rmse = numpy.sqrt(self.sumOfSquaredErrors / self.nobs)
        except:
            self.rmse = None

        try:
            self.r2adj = 1.0 - (1.0 - self.r2)*((self.nobs - 1.0)/(self.nobs-self.ncoef))   # adjusted R-square
        except:
            self.r2adj = None


        try:
            self.Fstat = (self.r2/self.df_r) / ((1.0 - self.r2)/self.df_e)  # model F-statistic
        except:
            self.Fstat = None

        try:
            self.Fpv = 1.0 - scipy.stats.f.cdf(self.Fstat, self.df_r, self.df_e)  # F-statistic p-value
        except:
            self.Fpv = None

        # Model log-likelihood, AIC, and BIC criterion values
        try:
            self.ll = -(self.nobs*0.5)*(1.0 + numpy.log(2.0*numpy.pi)) - (self.nobs*0.5)*numpy.log(numpy.dot(self.modelAbsoluteError,self.modelAbsoluteError)/self.nobs)
        except:
            self.ll = None

        try:
            self.aic = -2.0*self.ll/self.nobs + (2.0*self.ncoef/self.nobs)
        except:
            self.aic = None

        try:
            self.bic = -2.0*self.ll/self.nobs + (self.ncoef*numpy.log(self.nobs))/self.nobs
        except:
            self.bic = None

        if self.splineFlag == True: # not appicable to splines.  This might be better done with 
            self.cov_beta = None
            self.sd_beta = None
            self.tstat_beta = None
            self.pstat_beta = None
            self.ci = None
            return
        else:
            # see both scipy.odr.odrpack and http://www.scipy.org/Cookbook/OLS
            # this is inefficient but works for every possible case
            model = scipy.odr.odrpack.Model(self.WrapperForODR)
            self.dataCache.FindOrCreateAllDataCache(self)
            data = scipy.odr.odrpack.Data(self.dataCache.allDataCacheDictionary['IndependentData'], self.dataCache.allDataCacheDictionary['DependentData'])
            myodr = scipy.odr.odrpack.ODR(data, model, beta0=self.solvedCoefficients,  maxit=0)
            myodr.set_job(fit_type=2)
            parameterStatistics = myodr.run()
            self.cov_beta = parameterStatistics.cov_beta # parameter covariance matrix
            try:
                self.sd_beta = parameterStatistics.sd_beta * parameterStatistics.sd_beta
            except:
                self.sd_beta = None
            self.ci = []
            
            t_df = scipy.stats.t.ppf(0.975, self.df_e)
            
            for i in range(len(self.solvedCoefficients)):
                self.ci.append([self.solvedCoefficients[i] - t_df * parameterStatistics.sd_beta[i], self.solvedCoefficients[i] + t_df * parameterStatistics.sd_beta[i]])

            try:
                self.tstat_beta = self.solvedCoefficients / parameterStatistics.sd_beta # coeff t-statistics
            except:
                self.tstat_beta = None

            try:
                self.pstat_beta = (1.0 - scipy.stats.t.cdf(numpy.abs(self.tstat_beta), self.df_e)) * 2.0    # coef. p-values
            except:
                self.pstat_beta = None


    def CalculateModelErrors(self, inCoeffs, inDictionary):
        if self.upperCoefficientBounds != []:
            for i in range(len(inCoeffs)):
                if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                    if inCoeffs[i] > self.upperCoefficientBounds[i]:
                        inCoeffs[i] = self.upperCoefficientBounds[i]
        if self.lowerCoefficientBounds != []:
            for i in range(len(inCoeffs)):
                if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                    if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                        inCoeffs[i] = self.lowerCoefficientBounds[i]
        if self.fixedCoefficients != []:
            for i in range(len(inCoeffs)):
                if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                    inCoeffs[i] = self.fixedCoefficients[i]
        self.modelPredictions = self.CalculateModelPredictions(inCoeffs, inDictionary)
        self.modelAbsoluteError = self.modelPredictions - inDictionary['DependentData']
        try:
            if self.dataCache.DependentDataContainsZeroFlag == False:
                self.modelRelativeError = self.modelAbsoluteError / inDictionary['DependentData']
                self.modelPercentError = self.modelRelativeError * 100.0
        except:
            self.dataCache.DependentDataContainsZeroFlag = True # this is effectively true if this code is reached
            self.modelRelativeError = []
            self.modelPercentError = []


    def CalculateReducedDataFittingTarget(self, inCoeffs):
        #save time by checking constraints and bounds first
        if not self.AreCoefficientsWithinBounds(inCoeffs):
            try: # set any bounds
                if self.upperCoefficientBounds != []:
                    for i in range(len(inCoeffs)):
                        if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                            if inCoeffs[i] > self.upperCoefficientBounds[i]:
                                inCoeffs[i] = self.upperCoefficientBounds[i]
                if self.lowerCoefficientBounds != []:
                    for i in range(len(inCoeffs)):
                        if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                            if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                                inCoeffs[i] = self.lowerCoefficientBounds[i]
            except:
                pass
            
        # return SSQ as we are only using this method for guessing initial coefficients
        try:
            # set any fixed coefficients
            if self.fixedCoefficients != []:
                for i in range(len(inCoeffs)):
                    if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                        inCoeffs[i] = self.fixedCoefficients[i]
 
            error = self.CalculateModelPredictions(inCoeffs, self.dataCache.reducedDataCacheDictionary) - self.dataCache.reducedDataCacheDictionary['DependentData']
            ssq = numpy.sum(numpy.square(error))
        except:
            return 1.0E300
        if numpy.isfinite(ssq):
            return ssq
        else:
            return 1.0E300


    def CalculateAllDataFittingTarget(self, inCoeffs):
        #save time by checking bounds first
        if not self.AreCoefficientsWithinBounds(inCoeffs):
            try: # set to bounds
                if self.upperCoefficientBounds != []:
                    for i in range(len(inCoeffs)):
                        if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                            if inCoeffs[i] > self.upperCoefficientBounds[i]:
                                inCoeffs[i] = self.upperCoefficientBounds[i]
                if self.lowerCoefficientBounds != []:
                    for i in range(len(inCoeffs)):
                        if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                            if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                                inCoeffs[i] = self.lowerCoefficientBounds[i]
            except:
                pass

        try:
            # set any fixed coefficients
            if self.fixedCoefficients != []:
                for i in range(len(inCoeffs)):
                    if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                        inCoeffs[i] = self.fixedCoefficients[i]
                        
            self.CalculateModelErrors(inCoeffs, self.dataCache.allDataCacheDictionary)
            error = self.modelAbsoluteError
            
            if len(self.dataCache.allDataCacheDictionary['Weights']):
                error = error * self.dataCache.allDataCacheDictionary['Weights']
                
            if self.fittingTarget == "SSQABS":
                val = numpy.sum(numpy.square(error))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "SSQREL":
                error = error / self.dataCache.allDataCacheDictionary['DependentData']
                val = numpy.sum(numpy.square(error))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "ABSABS":
                val = numpy.sum(numpy.abs(error))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "ABSREL":
                
                val = numpy.sum(numpy.abs(error / self.dataCache.allDataCacheDictionary['DependentData']))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "PEAKABS":
                val = numpy.max(numpy.abs(error))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "PEAKREL":
                val = numpy.max(numpy.abs(error / self.dataCache.allDataCacheDictionary['DependentData']))
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300

            if self.fittingTarget == "ODR": # this is inefficient but works for every possible case
                model = scipy.odr.odrpack.Model(self.WrapperForODR)
                if self.dataCache.allDataCacheDictionary['Weights']:
                    data = scipy.odr.odrpack.Data(self.dataCache.allDataCacheDictionary['IndependentData'],  self.dataCache.allDataCacheDictionary['DependentData'], we = self.dataCache.allDataCacheDictionary['Weights'])
                else:
                    data = scipy.odr.odrpack.Data(self.dataCache.allDataCacheDictionary['IndependentData'],  self.dataCache.allDataCacheDictionary['DependentData'])
                myodr = scipy.odr.odrpack.ODR(data, model, beta0=inCoeffs, maxit=0)
                myodr.set_job(fit_type=2)
                out = myodr.run()
                val = out.sum_square
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            # remaining targets require these
            ncoef = 1.0 * len(inCoeffs)
            nobs = 1.0 * len(self.dataCache.allDataCacheDictionary['DependentData'])
            ll = -(nobs*0.5)*(1.0 + numpy.log(2.0*numpy.pi)) - (nobs*0.5)*numpy.log(numpy.dot(error,error)/nobs)

            if self.fittingTarget == "AIC":
                val = -2.0*ll/nobs + (2.0*ncoef/nobs)
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
                    
            if self.fittingTarget == "BIC":
                val = -2.0*ll/nobs + (ncoef*numpy.log(nobs))/nobs
                if numpy.isfinite(val):
                    return val
                else:
                    return 1.0E300
        except:
            return 1.0E300


    def Solve(self, inNonLinearSolverAlgorithmName='Levenberg-Marquardt'):
        
        solver = pyeq2.solverService()
                
        # if any of these conditions exist, a linear solver cannot be used
        if self.fixedCoefficients != [] or self.upperCoefficientBounds != [] or self.lowerCoefficientBounds != [] or len(self.dataCache.allDataCacheDictionary['Weights']):
            self._canLinearSolverBeUsedForSSQABS = False
        
        # selection of different solvers and algorithms.
        if self.splineFlag:
            return solver.SolveUsingSpline(self)
        elif self.fittingTarget == 'SSQABS' and self.CanLinearSolverBeUsedForSSQABS() == True:
            return solver.SolveUsingLinear(self)
        elif self.fittingTarget == 'ODR':
            if len(self.deEstimatedCoefficients) == 0:
                self.deEstimatedCoefficients = solver.SolveUsingDE(self)
            return solver.SolveUsingODR(self)
        else:
            if len(self.deEstimatedCoefficients) == 0:
                self.deEstimatedCoefficients = solver.SolveUsingDE(self)
            self.estimatedCoefficients = solver.SolveUsingSelectedAlgorithm(self, inAlgorithmName=inNonLinearSolverAlgorithmName)
            return solver.SolveUsingSimplex(self)


    def AreCoefficientsWithinBounds(self, inCoeffs):
        if self.upperCoefficientBounds != []:
            for index in range(len(inCoeffs)):
                if inCoeffs[index] > self.upperCoefficientBounds[index]:
                    return False
        if self.lowerCoefficientBounds != []:
            for index in range(len(inCoeffs)):
                if inCoeffs[index] < self.lowerCoefficientBounds[index]:
                    return False
        return True


    def GetDisplayName(self):
        return self.extendedVersionHandler.AssembleDisplayName(self)
        

    def GetDisplayHTML(self):
        return self.extendedVersionHandler.AssembleDisplayHTML(self)


    def GetDimensionality(self):
        return self._dimensionality


    def CanLinearSolverBeUsedForSSQABS(self):
        return self.extendedVersionHandler.CanLinearSolverBeUsedForSSQABS(self._canLinearSolverBeUsedForSSQABS)


    def WrapperForScipyCurveFit(self, data, *inCoeffs):
        inCoeffs = numpy.array(inCoeffs) # so coefficient assigment can be made
        if self.upperCoefficientBounds != []:
            for i in range(len(inCoeffs)):
                if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                    if inCoeffs[i] > self.upperCoefficientBounds[i]:
                        inCoeffs[i] = self.upperCoefficientBounds[i]
        if self.lowerCoefficientBounds != []:
            for i in range(len(inCoeffs)):
                if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                    if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                        inCoeffs[i] = self.lowerCoefficientBounds[i]
        if self.fixedCoefficients != []:
            for i in range(len(inCoeffs)):
                if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                    inCoeffs[i] = self.fixedCoefficients[i]
        return self.CalculateModelPredictions(inCoeffs, self.dataCache.allDataCacheDictionary)


    def WrapperForODR(self, inCoeffs, data):
        if numpy.array_equal(data, self.dataCache.allDataCacheDictionary['IndependentData']):
            if self.upperCoefficientBounds != []:
                for i in range(len(inCoeffs)):
                    if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                        if inCoeffs[i] > self.upperCoefficientBounds[i]:
                            inCoeffs[i] = self.upperCoefficientBounds[i]
            if self.lowerCoefficientBounds != []:
                for i in range(len(inCoeffs)):
                    if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                        if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                            inCoeffs[i] = self.lowerCoefficientBounds[i]
            if self.fixedCoefficients != []:
                for i in range(len(inCoeffs)):
                    if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                        inCoeffs[i] = self.fixedCoefficients[i]
            result = self.CalculateModelPredictions(inCoeffs, self.dataCache.allDataCacheDictionary)
        else:
            tempCache = self.dataCache.allDataCacheDictionary
            self.dataCache.allDataCacheDictionary = {}
            self.dataCache.allDataCacheDictionary['IndependentData'] = data
            self.dataCache.FindOrCreateAllDataCache(self)
            if self.upperCoefficientBounds != []:
                for i in range(len(inCoeffs)):
                    if self.upperCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                        if inCoeffs[i] > self.upperCoefficientBounds[i]:
                            inCoeffs[i] = self.upperCoefficientBounds[i]
            if self.lowerCoefficientBounds != []:
                for i in range(len(inCoeffs)):
                    if self.lowerCoefficientBounds[i] != None: # use None as a flag for coefficients that are not fixed
                        if inCoeffs[i] < self.lowerCoefficientBounds[i]:
                            inCoeffs[i] = self.lowerCoefficientBounds[i]
            if self.fixedCoefficients != []:
                for i in range(len(inCoeffs)):
                    if self.fixedCoefficients[i] != None: # use None as a flag for coefficients that are not fixed
                        inCoeffs[i] = self.fixedCoefficients[i]
            result = self.CalculateModelPredictions(inCoeffs, self.dataCache.allDataCacheDictionary)
            self.dataCache.allDataCacheDictionary = tempCache
        return result

    
    def GetCoefficientDesignators(self):
        return self.extendedVersionHandler.AssembleCoefficientDesignators(self)

    
    def ShouldDataBeRejected(self, unused):
        return self.extendedVersionHandler.ShouldDataBeRejected(self)
