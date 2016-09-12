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

import pyeq2

import numpy
try:
    import scipy.interpolate, scipy.stats
except:
    pass
numpy.seterr(all= 'ignore')



class IModel(object):
    splineFlag = False
    userSelectablePolynomialFlag = False
    userCustomizablePolynomialFlag = False
    userSelectablePolyfunctionalFlag = False
    userSelectableRationalFlag = False
    userDefinedFunctionFlag = False
    
    independentData1CannotContainZeroFlag = False
    independentData1CannotContainPositiveFlag = False
    independentData1CannotContainNegativeFlag = False
    independentData2CannotContainZeroFlag = False
    independentData2CannotContainPositiveFlag = False
    independentData2CannotContainNegativeFlag = False
    
    independentData1CannotContainBothPositiveAndNegativeFlag = False
    independentData2CannotContainBothPositiveAndNegativeFlag = False    

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
                               'LNQREL': 'sum of squared log[predicted/actual]',
                               'ABSREL': 'sum of absolute value of relative error',
                               'PEAKABS':'peak absolute value of absolute error',
                               'PEAKREL':'peak absolute value of relative error',
                               'AIC':    'Akaike Information Criterion',
                               'BIC':    'Bayesian Information Criterion'
                              }
    

    def __init__(self, inFittingTarget = 'SSQABS', inExtendedVersionName = 'Default'):
        if inExtendedVersionName == '':
            inExtendedVersionName = 'Default'
            
        if inFittingTarget not in list(self.fittingTargetDictionary.keys()):
            raise Exception(str(inFittingTarget) + ' is not in the IModel class fitting target dictionary.')
        self.fittingTarget = inFittingTarget
        
        inExtendedVersionName = inExtendedVersionName.replace(' ', '')
        if inExtendedVersionName not in  pyeq2.ExtendedVersionHandlers.extendedVersionHandlerNameList:
            raise Exception(inExtendedVersionName + ' is not in the list of extended version handler names.')
        
        allowedExtendedVersion = True
        if (-1 != inExtendedVersionName.find('Offset')) and (self.autoGenerateOffsetForm == False):
            allowedExtendedVersion = False
        if (-1 != inExtendedVersionName.find('Reciprocal')) and (self.autoGenerateReciprocalForm == False):
            allowedExtendedVersion = False
        if (-1 != inExtendedVersionName.find('Inverse')) and (self.autoGenerateInverseForms == False):
            allowedExtendedVersion = False
        if (-1 != inExtendedVersionName.find('Growth')) and (self.autoGenerateGrowthAndDecayForms == False):
            allowedExtendedVersion = False
        if (-1 != inExtendedVersionName.find('Decay')) and (self.autoGenerateGrowthAndDecayForms == False):
            allowedExtendedVersion = False
        if allowedExtendedVersion == False:
            raise Exception('This equation does not allow an extended version named  "' + inExtendedVersionName + '".')            
        self.extendedVersionHandler = eval('pyeq2.ExtendedVersionHandlers.ExtendedVersionHandler_' + inExtendedVersionName + '.ExtendedVersionHandler_' + inExtendedVersionName + '()')
        
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
        self.deEstimatedCoefficients = []
        
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
        # unweighted values are always calculated, weighted values are calculated below if user supplied weights
        self.nobs = len(self.dataCache.allDataCacheDictionary['DependentData'])  # number of observations
        self.ncoef = len(self.solvedCoefficients)          # number of coef.
        self.df_e = self.nobs - self.ncoef                 # degrees of freedom, error
        self.df_r = self.ncoef - 1                              # degrees of freedom, regression
        self.sumOfSquaredErrors = numpy.sum(self.modelAbsoluteError * self.modelAbsoluteError)

        # if coefficients have bounds or fixed values, these calculations
        # can fail.  The constraints are for the solver.  Calculate these
        # statistics without constraints, and warn users that do use any
        # constraints that these statistics are not valid if near bounds.
        # Values for fixed coefficients should be correct if they are
        # only fixed as a constraint for the solver.

        # temporarily remove constraints, restore later
        upperCoefficientBounds = self.upperCoefficientBounds
        lowerCoefficientBounds = self.lowerCoefficientBounds
        fixedCoefficients = self.fixedCoefficients
        self.upperCoefficientBounds = []
        self.lowerCoefficientBounds = []
        self.fixedCoefficients = []
        
        try:
            self.r2 = 1.0 - self.modelAbsoluteError.var()/self.dataCache.allDataCacheDictionary['DependentData'].var()

            # extremely poor fits can have absolute error variance greater than sample
            # variance at machine precision levels, giving tiny negative R-squared values
            if self.r2 < 0.0:
                self.r2 = None
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
        # from http://stackoverflow.com/questions/7458391/python-multiple-linear-regression-using-ols-code-with-specific-data
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

        if self.splineFlag == True: # not appicable to splines
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

        if len(self.dataCache.allDataCacheDictionary['Weights']):
            self.nobs_weighted = len(self.dataCache.allDataCacheDictionary['DependentData'])  # number of observations
            self.ncoef_weighted = len(self.solvedCoefficients)          # number of coef.
            self.df_e_weighted = self.nobs - self.ncoef                 # degrees of freedom, error
            self.df_r_weighted = self.ncoef - 1                              # degrees of freedom, regression
            absoluteErrorWeighted = self.modelAbsoluteError * self.dataCache.allDataCacheDictionary['Weights']
            self.sumOfSquaredErrors_weighted = numpy.sum(absoluteErrorWeighted * absoluteErrorWeighted)
    
            try:
                self.r2_weighted = 1.0 - absoluteErrorWeighted.var()/self.dataCache.allDataCacheDictionary['DependentData'].var()
            except:
                self.r2_weighted= None
    
            try:
                self.rmse_weighted = numpy.sqrt(self.sumOfSquaredErrors_weighted / self.nobs_weighted)
            except:
                self.rmse_weighted = None
    
            try:
                self.r2adj_weighted = 1.0 - (1.0 - self.r2_weighted)*((self.nobs_weighted - 1.0)/(self.nobs_weighted-self.ncoef_weighted))   # adjusted R-square
            except:
                self.r2adj_weighted = None
    
    
            try:
                self.Fstat_weighted = (self.r2_weighted/self.df_r_weighted) / ((1.0 - self.r2_weighted)/self.df_e_weighted)  # model F-statistic
            except:
                self.Fstat_weighted = None
    
            try:
                self.Fpv_weighted = 1.0 - scipy.stats.f.cdf(self.Fstat_weighted, self.df_r_weighted, self.df_e_weighted)  # F-statistic p-value
            except:
                self.Fpv_weighted = None
    
            # Model log-likelihood, AIC, and BIC criterion values
            try:
                self.ll_weighted = -(self.nobs_weighted*0.5)*(1.0 + numpy.log(2.0*numpy.pi)) - (self.nobs_weighted*0.5)*numpy.log(numpy.dot(absoluteErrorWeighted,absoluteErrorWeighted)/self.nobs_weighted)
            except:
                self.ll_weighted = None
    
            try:
                self.aic_weighted = -2.0*self.ll_weighted/self.nobs_weighted + (2.0*self.ncoef_weighted/self.nobs_weighted)
            except:
                self.aic_weighted = None
    
            try:
                self.bic_weighted = -2.0*self.ll_weighted/self.nobs_weighted + (self.ncoef_weighted*numpy.log(self.nobs_weighted))/self.nobs_weighted
            except:
                self.bic_weighted = None
    
            if self.splineFlag == True: # not appicable to splines
                self.cov_beta_weighted = None
                self.sd_beta_weighted = None
                self.tstat_beta_weighted = None
                self.pstat_beta_weighted = None
                self.ci_weighted = None
                return
            else:
                # see both scipy.odr.odrpack and http://www.scipy.org/Cookbook/OLS
                # this is inefficient but works for every possible case
                model_weighted = scipy.odr.odrpack.Model(self.WrapperForODR)
                self.dataCache.FindOrCreateAllDataCache(self)
                data_weighted = scipy.odr.odrpack.Data(self.dataCache.allDataCacheDictionary['IndependentData'], self.dataCache.allDataCacheDictionary['DependentData'], self.dataCache.allDataCacheDictionary['Weights'])
                myodr_weighted = scipy.odr.odrpack.ODR(data_weighted, model_weighted, beta0=self.solvedCoefficients,  maxit=0)
                myodr_weighted.set_job(fit_type=2)
                parameterStatistics_weighted = myodr_weighted.run()
                self.cov_beta_weighted = parameterStatistics.cov_beta # parameter covariance matrix
                try:
                    self.sd_beta_weighted = parameterStatistics_weighted.sd_beta * parameterStatistics_weighted.sd_beta
                except:
                    self.sd_beta_weighted = None
                self.ci_weighted = []
                
                t_df_weighted = scipy.stats.t.ppf(0.975, self.df_e_weighted)
                
                for i in range(len(self.solvedCoefficients)):
                    self.ci_weighted.append([self.solvedCoefficients[i] - t_df_weighted * parameterStatistics_weighted.sd_beta[i], self.solvedCoefficients[i] + t_df_weighted * parameterStatistics_weighted.sd_beta[i]])
    
                try:
                    self.tstat_beta_weighted = self.solvedCoefficients / parameterStatistics_weighted.sd_beta # coeff t-statistics
                except:
                    self.tstat_beta_weighted = None
    
                try:
                    self.pstat_beta_weighted = (1.0 - scipy.stats.t.cdf(numpy.abs(self.tstat_beta_weighted), self.df_e_weighted)) * 2.0    # coef. p-values
                except:
                    self.pstat_beta_weighted = None
        else:
            self.nobs_weighted = None
            self.ncoef_weighted = None
            self.df_e_weighted = None
            self.df_r_weighted = None
            self.sumOfSquaredErrors_weighted = None
            self.r2_weighted = None
            self.rmse_weighted = None
            self.r2adj_weighted = None
            self.Fstat_weighted = None
            self.Fpv_weighted = None
            self.ll_weighted = None
            self.aic_weighted = None
            self.bic_weighted = None
            self.cov_beta_weighted = None
            self.sd_beta_weighted = None
            self.tstat_beta_weighted = None
            self.pstat_beta_weighted = None
            self.ci_weighted = None

        # restore constraints, as users will not expect them to have changed
        self.upperCoefficientBounds = upperCoefficientBounds
        self.lowerCoefficientBounds = lowerCoefficientBounds
        self.fixedCoefficients = fixedCoefficients
                    

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
                    
            # see http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2635088
            if self.fittingTarget == "LNQREL":
                
                Q = numpy.abs(self.modelPredictions / self.dataCache.allDataCacheDictionary['DependentData'])
                sumsqlogQ = numpy.sum(numpy.square(numpy.log(Q)))
                val = sumsqlogQ
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

            # ODR does not use "error" above, which can be weighted, so weights are passed to ODR if used
            if self.fittingTarget == "ODR": # this is inefficient but works for every possible case
                model = scipy.odr.odrpack.Model(self.WrapperForODR)
                if len(self.dataCache.allDataCacheDictionary['Weights']):
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
                if  (self.upperCoefficientBounds[index] != None) and  (inCoeffs[index] > self.upperCoefficientBounds[index]):
                    return False
        if self.lowerCoefficientBounds != []:
            for index in range(len(inCoeffs)):
                if (self.lowerCoefficientBounds[index] != None) and (inCoeffs[index] < self.lowerCoefficientBounds[index]):
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
        if not numpy.all(numpy.isfinite(data)):
            return numpy.ones(len(self.dataCache.allDataCacheDictionary['DependentData'])) * 1.0E300
        
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
        
        # should data be rejected?
        true_or_false = self.extendedVersionHandler.ShouldDataBeRejected(self)

        if self.dataCache.DependentDataContainsZeroFlag and self.fittingTarget[-3:] == "REL":
            true_or_false = True
        
        # if yes, why?
        self.reasonWhyDataRejected = 'unknown condition' # hopefully this will not be used
        if true_or_false:
            if self.dataCache.DependentDataContainsZeroFlag and self.fittingTarget[-3:] == "REL":
                self.reasonWhyDataRejected = 'The data contains at least one dependent data value of exactly 0.0, a relative fit cannot be performed as divide-by-zero errors would occur.'
            
            if self.independentData1CannotContainZeroFlag and self.dataCache.independentData1ContainsZeroFlag:
                self.reasonWhyDataRejected = 'This equation requires non-zero values for the first independent variable (X). At least one of the values was exactly equal to zero. Examples that would fail would be ln(x) and 1/x.'
    
            if self.equation.independentData1CannotContainNegativeFlag and self.dataCache.independentData1ContainsNegativeFlag:
                self.reasonWhyDataRejected = 'This equation requires non-negative values for the first independent variable (X). At least one of the values was negative. One example that would fail is ln(x).'
    
            if self.equation.independentData1CannotContainPositiveFlag and self.dataCache.independentData1ContainsPositiveFlag:
                self.reasonWhyDataRejected = 'This equation requires non-positive values for the first independent variable (X). At least one of the values was positive. One xample that would fail would be ln(-x), please check the data.'
    
            if self.equation.independentData1CannotContainBothPositiveAndNegativeFlag and self.dataCache.independentData1ContainsPositiveFlag and self.dataCache.independentData1ContainsNegativeFlag:
                self.reasonWhyDataRejected = 'This equation cannot have both positive and negative values for the first independent variable (X)/'

        return true_or_false


    def RecursivelyConvertIntStringsToFloatStrings(self, inList):
        returnList = []
        for item in inList:
            if type(item) == type([]): # is this item another list?
                returnList.append(self.RecursivelyConvertIntStringsToFloatStrings(item))
            else:
                if type(item) == type(str('')): # is this item a string?
                    if  item.isdigit():
                        returnList.append(str(float(item))) # convert the integer to its floating point representation
                    else:
                        returnList.append(item)
                else:
                    returnList.append(item)
        return returnList
