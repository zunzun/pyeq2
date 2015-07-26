import os, sys
import  wx
import numpy, scipy

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wx import NavigationToolbar2Wx # not used in this example
from matplotlib.figure import Figure

import matplotlib
import matplotlib.pyplot

if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2



# see the included wxNestedTabsExample.py file
class CoefficientAndFitStatisticsReport(wx.Panel):
    def __init__(self, parent, equation):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        self.text = wx.TextCtrl(self, -1, '', style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL|wx.TE_READONLY)
        
        if equation.upperCoefficientBounds or equation.lowerCoefficientBounds:
            self.text.AppendText('This model has coefficient bounds. Parameter statistics may\n')
            self.text.AppendText('not be valid for parameter values at or near the bounds.\n')
            self.text.AppendText('\n')
        
        self.text.AppendText('Degress of freedom error ' + str(equation.df_e) + '\n')
        self.text.AppendText('Degress of freedom regression ' + str(equation.df_r) + '\n')
        
        if equation.rmse == None:
            self.text.AppendText('Root Mean Squared Error (RMSE): n/a\n')
        else:
            self.text.AppendText('Root Mean Squared Error (RMSE): ' + str(equation.rmse) + '\n')
        
        if equation.r2 == None:
            self.text.AppendText('R-squared: n/a\n')
        else:
            self.text.AppendText('R-squared: ' + str(equation.r2) + '\n')
        
        if equation.r2adj == None:
            self.text.AppendText('R-squared adjusted: n/a\n')
        else:
            self.text.AppendText('R-squared adjusted: ' + str(equation.r2adj) + '\n')
        
        if equation.Fstat == None:
            self.text.AppendText('Model F-statistic: n/a\n')
        else:
            self.text.AppendText('Model F-statistic: ' + str(equation.Fstat) + '\n')
        
        if equation.Fpv == None:
            self.text.AppendText('Model F-statistic p-value: n/a\n')
        else:
            self.text.AppendText('Model F-statistic p-value: ' + str(equation.Fpv) + '\n')
        
        if equation.ll == None:
            self.text.AppendText('Model log-likelihood: n/a\n')
        else:
            self.text.AppendText('Model log-likelihood: ' + str(equation.ll) + '\n')
        
        if equation.aic == None:
            self.text.AppendText('Model AIC: n/a\n')
        else:
            self.text.AppendText('Model AIC: ' + str(equation.aic) + '\n')
        
        if equation.bic == None:
            self.text.AppendText('Model BIC: n/a\n')
        else:
            self.text.AppendText('Model BIC: ' + str(equation.bic) + '\n')
        
        
        self.text.AppendText('\n')
        self.text.AppendText("Individual Parameter Statistics:\n")
        for i in range(len(equation.solvedCoefficients)):
            if equation.tstat_beta == None:
                tstat = 'n/a'
            else:
                tstat = '%-.5E' %  ( equation.tstat_beta[i])
        
            if equation.pstat_beta == None:
                pstat = 'n/a'
            else:
                pstat = '%-.5E' %  ( equation.pstat_beta[i])
        
            if equation.sd_beta != None:
                self.text.AppendText("Coefficient %s = %-.16E, std error: %-.5E\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i], equation.sd_beta[i]))
            else:
                self.text.AppendText("Coefficient %s = %-.16E, std error: n/a\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
            self.text.AppendText("          t-stat: %s, p-stat: %s, 95 percent confidence intervals: [%-.5E, %-.5E]\n" % (tstat,  pstat, equation.ci[i][0], equation.ci[i][1]))
        
        
        self.text.AppendText('\n')
        self.text.AppendText("Coefficient Covariance Matrix:\n")
        for i in  equation.cov_beta:
            self.text.AppendText(str(i) + '\n')
        
        sizer = wx.BoxSizer()
        sizer.Add(self.text, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()



class SourceCodeReport(wx.Panel):
    def __init__(self, parent, equation, lanuageNameString):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        exec('code = pyeq2.outputSourceCodeService().GetOutputSourceCode' + lanuageNameString + '(equation)')
        self.text = wx.TextCtrl(self, -1, code, style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL|wx.TE_READONLY)

        sizer = wx.BoxSizer()
        sizer.Add(self.text, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()



class AbsoluteErrorStatisticsReport(wx.Panel):
    def __init__(self, parent, titleString, tempdata):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        self.text = wx.TextCtrl(self, -1, '', style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL|wx.TE_READONLY)

        self.text.AppendText(titleString + '\n\n')
        
        # must at least have max and min
        minData = min(tempdata)
        maxData = max(tempdata)
        
        if maxData == minData:
            self.text.AppendText('All data has the same value,\n')
            self.text.AppendText("value = %-.16E\n" % (minData))
            self.text.AppendText('statistics cannot be calculated.')
        else:
            self.text.AppendText("max = %-.16E\n" % (maxData))
            self.text.AppendText("min = %-.16E\n" % (minData))
            
            try:
                temp = scipy.mean(tempdata)
                self.text.AppendText("mean = %-.16E\n" % (temp))
            except:
                self.text.AppendText("mean gave error in calculation\n")

            try:
                temp = scipy.stats.sem(tempdata)
                self.text.AppendText("standard error of mean = %-.16E\n" % (temp))
            except:
                self.text.AppendText("standard error of mean gave error in calculation\n")

            try:
                temp = scipy.median(tempdata)
                self.text.AppendText("median = %-.16E\n" % (temp))
            except:
                self.text.AppendText("median gave error in calculation\n")

            try:
                temp = scipy.var(tempdata)
                self.text.AppendText("variance = %-.16E\n" % (temp))
            except:
                self.text.AppendText("variance gave error in calculation\n")

            try:
                temp = scipy.std(tempdata)
                self.text.AppendText("std. deviation = %-.16E\n" % (temp))
            except:
                self.text.AppendText("std. deviation gave error in calculation\n")

            try:
                temp = scipy.stats.skew(tempdata)
                self.text.AppendText("skew = %-.16E\n" % (temp))
            except:
                self.text.AppendText("skew gave error in calculation\n")

            try:
                temp = scipy.stats.kurtosis(tempdata)
                self.text.AppendText("kurtosis = %-.16E\n" % (temp))
            except:
                self.text.AppendText("kurtosis gave error in calculation\n")
        
    
        sizer = wx.BoxSizer()
        sizer.Add(self.text, 1, wx.EXPAND)
    
        self.SetSizer(sizer)
        self.Fit()



class CoefficientsReport(wx.Panel):
    def __init__(self, parent, equation):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        self.text = wx.TextCtrl(self, -1, '\n', style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL|wx.TE_READONLY)
        cd = equation.GetCoefficientDesignators()
        for i in range(len(equation.solvedCoefficients)):
            self.text.AppendText("%s = %-.16E\n" % (cd[i], equation.solvedCoefficients[i]))

            sizer = wx.BoxSizer()
            sizer.Add(self.text, 1, wx.EXPAND)
        
            self.SetSizer(sizer)
            self.Fit()



# see the included wxNestedTabsExample.py file
# and the included wxMatplotlibExample.py file
class PanelContainingOneGraphReport(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.parent = parent
        self.parent.dep_data = None
        self.parent.abs_error = None
        self.parent.per_error = None
        self.parent.x_data = None
        self.parent.y_data = None
        self.parent.z_data = None
        self.parent.X = None
        self.parent.Y = None
        self.parent.Z = None
        
        self.figure = matplotlib.pyplot.figure()
        matplotlib.pyplot.grid(True)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()



class Report_AbsoluteErrorGraph(PanelContainingOneGraphReport):
    def draw(self, equation):
        if not self.parent.dep_data:
            self.parent.dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
        if not self.parent.abs_error:
            self.parent.abs_error = equation.modelAbsoluteError
        self.axes.plot(self.parent.dep_data, self.parent.abs_error, 'D')
        if equation.GetDimensionality() == 2:
            self.axes.set_title('Absolute Error vs. X Data') # add a title
            self.axes.set_xlabel('X Data') # X axis data label
        else:
            self.axes.set_title('Absolute Error vs. Z Data') # add a title
            self.axes.set_xlabel('Z Data') # X axis data label
        self.axes.set_ylabel(" Absolute Error") # Y axis label is always is absolute error



class Report_PercentErrorGraph(PanelContainingOneGraphReport):
    def draw(self, equation):
        if not self.parent.dep_data:
            self.parent.dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
        if not self.parent.per_error:
            self.parent.per_error = equation.modelPercentError
        self.axes.plot(self.parent.dep_data, self.parent.per_error, 'D')
        if equation.GetDimensionality() == 2:
            self.axes.set_title('Percent Error vs. X Data') # add a title
            self.axes.set_xlabel('X Data') # X axis data label
        else:
            self.axes.set_title('APercent Error vs. Z Data') # add a title
            self.axes.set_xlabel('Z Data') # X axis data label
        self.axes.set_ylabel(" Percent Error") # Y axis label is always is percent error



class Report_SurfacePlot(PanelContainingOneGraphReport):
    def draw(self, equation):
        if not self.parent.x_data:
            self.parent.x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]
        if not self.parent.y_data:
            self.parent.y_data = equation.dataCache.allDataCacheDictionary['IndependentData'][1]
        if not self.parent.z_data:
            self.parent.z_data = equation.dataCache.allDataCacheDictionary['DependentData']
            
        from mpl_toolkits.mplot3d import Axes3D # 3D apecific
        from matplotlib import cm # to colormap from blue to red
        
        if not self.parent.Z:
            xModel = numpy.linspace(min(self.parent.x_data), max(self.parent.x_data), 20)
            yModel = numpy.linspace(min(self.parent.y_data), max(self.parent.y_data), 20)
            self.parent.X, self.parent.Y = numpy.meshgrid(xModel, yModel)
        
            tempcache = equation.dataCache
            equation.dataCache = pyeq2.dataCache()
            equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([self.parent.X, self.parent.Y])
            equation.dataCache.FindOrCreateAllDataCache(equation)
            self.parent.Z = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.dataCache = tempcache
    
        self.axes = self.figure.gca(projection='3d')
        self.axes.plot_surface(self.parent.X, self.parent.Y, self.parent.Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=1, antialiased=True)
    
        self.axes.scatter(self.parent.x_data, self.parent.y_data, self.parent.z_data)
    
        self.axes.set_title('Surface Plot (click-drag with mouse)') # add a title for surface plot
        self.axes.set_xlabel('X Data') # X axis data label
        self.axes.set_ylabel('Y Data') # Y axis data label
        self.axes.set_zlabel('Z Data') # Z axis data label



class Report_ContourPlot(PanelContainingOneGraphReport):
    def draw(self, equation):
        if not self.parent.x_data:
            self.parent.x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]
        if not self.parent.y_data:
            self.parent.y_data = equation.dataCache.allDataCacheDictionary['IndependentData'][1]
        if not self.parent.z_data:
            self.parent.z_data = equation.dataCache.allDataCacheDictionary['DependentData']
            
        if not self.parent.Z:
            xModel = numpy.linspace(min(self.parent.x_data), max(self.parent.x_data), 20)
            yModel = numpy.linspace(min(self.parent.y_data), max(self.parent.y_data), 20)
            self.parent.X, self.parent.Y = numpy.meshgrid(xModel, yModel)
        
            tempcache = equation.dataCache
            equation.dataCache = pyeq2.dataCache()
            equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([self.parent.X, self.parent.Y])
            equation.dataCache.FindOrCreateAllDataCache(equation)
            self.parent.Z = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.dataCache = tempcache
        
        self.axes.plot(self.parent.x_data, self.parent.y_data, 'o')

        self.axes.set_title('Contour Plot') # add a title for contour plot
        self.axes.set_xlabel('X Data') # X axis data label
        self.axes.set_ylabel('Y Data') # Y axis data label
    
        numberOfContourLines = 16
        CS = matplotlib.pyplot.contour(self.parent.X, self.parent.Y, self.parent.Z, numberOfContourLines, colors='k')
        matplotlib.pyplot.clabel(CS, inline=1, fontsize=10) # labels for contours



class Report_ModelScatterConfidenceGraph(PanelContainingOneGraphReport):
    def draw(self, equation):
        if not self.parent.y_data:
            self.parent.y_data = equation.dataCache.allDataCacheDictionary['DependentData']
        if not self.parent.x_data:
            self.parent.x_data = equation.dataCache.allDataCacheDictionary['IndependentData'][0]

        # now create data for the fitted equation plot
        xModel = numpy.linspace(min(self.parent.x_data), max(self.parent.x_data))
    
        tempcache = equation.dataCache
        equation.dataCache = pyeq2.dataCache()
        equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xModel, xModel])
        equation.dataCache.FindOrCreateAllDataCache(equation)
        yModel = equation.CalculateModelPredictions(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
        equation.dataCache = tempcache
    
        # first the raw data as a scatter plot
        self.axes.plot(self.parent.x_data, self.parent.y_data,  'D')
    
        # now the model as a line plot
        self.axes.plot(xModel, yModel)
    
        # now calculate confidence intervals
        # http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_nlin_sect026.htm
        # http://www.staff.ncl.ac.uk/tom.holderness/software/pythonlinearfit
        mean_x = numpy.mean(self.parent.x_data)			# mean of x
        n = equation.nobs		    # number of samples in the origional fit
    
        t_value = scipy.stats.t.ppf(0.975, equation.df_e) # (1.0 - (a/2)) is used for two-sided t-test critical value, here a = 0.05
    
        confs = t_value * numpy.sqrt((equation.sumOfSquaredErrors/equation.df_e)*(1.0/n + (numpy.power((xModel-mean_x),2.0)/
                                                                                                 ((numpy.sum(numpy.power(self.parent.x_data,2)))-n*(numpy.power(mean_x,2.0))))))
    
        # get lower and upper confidence limits based on predicted y and confidence intervals
        upper = yModel + abs(confs)
        lower = yModel - abs(confs)
    
        # mask off any numbers outside the existing plot limits
        booleanMask = yModel > matplotlib.pyplot.ylim()[0]
        booleanMask &= (yModel < matplotlib.pyplot.ylim()[1])
    
        # color scheme improves visibility on black background lines or points
        self.axes.plot(xModel[booleanMask], lower[booleanMask], linestyle='solid', color='white')
        self.axes.plot(xModel[booleanMask], upper[booleanMask], linestyle='solid', color='white')
        self.axes.plot(xModel[booleanMask], lower[booleanMask], linestyle='dashed', color='blue')
        self.axes.plot(xModel[booleanMask], upper[booleanMask], linestyle='dashed', color='blue')
    
        self.axes.set_title('Model With 95% Confidence Limits') # add a title
        self.axes.set_xlabel('X Data') # X axis data label
        self.axes.set_ylabel('Y Data') # Y axis data label



# see the included wxNestedTabsExample.py file
class TopLevelResultsNotebook(wx.Notebook):
    def __init__(self, parent, equation):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        # graphs
        graphReportsTab = wx.Notebook(self)
        self.AddPage(graphReportsTab, "Graph Reports")
        
        if equation.GetDimensionality() == 2:
            modelConfidenceScatter = Report_ModelScatterConfidenceGraph(graphReportsTab)
            modelConfidenceScatter.draw(equation)
            graphReportsTab.AddPage(modelConfidenceScatter, "Model With 95%Confidence")
        else:
            surfacePlot = Report_SurfacePlot(graphReportsTab)
            surfacePlot.draw(equation)
            graphReportsTab.AddPage(surfacePlot, "Surface Plot")
            
            contourPlot = Report_ContourPlot(graphReportsTab)
            contourPlot.draw(equation)
            graphReportsTab.AddPage(contourPlot, "Contour Plot")

        absoluteErrorGraph = Report_AbsoluteErrorGraph(graphReportsTab)
        absoluteErrorGraph.draw(equation)
        graphReportsTab.AddPage(absoluteErrorGraph, "Absolute Error")
    
        percentErrorGraph = Report_PercentErrorGraph(graphReportsTab)
        percentErrorGraph.draw(equation)
        graphReportsTab.AddPage(percentErrorGraph, "Percent Error")
        
        textReportsTab = wx.Notebook(self)
        self.AddPage(textReportsTab, "Text Reports")
        
        textReport1 = CoefficientAndFitStatisticsReport(textReportsTab, equation)
        textReportsTab.AddPage(textReport1, "Coefficient And Fit Statistics")
        
        textReport2 = CoefficientsReport(textReportsTab, equation)
        textReportsTab.AddPage(textReport2, "Coefficient Listing")
        
        textReport3 = AbsoluteErrorStatisticsReport(textReportsTab, 'Absolute Error Statistics', equation.modelAbsoluteError)
        textReportsTab.AddPage(textReport3, "Absolute Error Statistics")
        
        sourceCodeTab = wx.Notebook(self)
        self.AddPage(sourceCodeTab, "Source Code")

        aourcecode1 = SourceCodeReport(sourceCodeTab, equation, 'CPP')
        sourceCodeTab.AddPage(aourcecode1, "C++")

        aourcecode2 = SourceCodeReport(sourceCodeTab, equation, 'CSHARP')
        sourceCodeTab.AddPage(aourcecode2, "CSHARP")
    
        aourcecode3 = SourceCodeReport(sourceCodeTab, equation, 'VBA')
        sourceCodeTab.AddPage(aourcecode3, "VBA")
    
        aourcecode4 = SourceCodeReport(sourceCodeTab, equation, 'PYTHON')
        sourceCodeTab.AddPage(aourcecode4, "PYTHON")
    
        aourcecode5 = SourceCodeReport(sourceCodeTab, equation, 'JAVA')
        sourceCodeTab.AddPage(aourcecode5, "JAVA")
    
        aourcecode6 = SourceCodeReport(sourceCodeTab, equation, 'JAVASCRIPT')
        sourceCodeTab.AddPage(aourcecode6, "JAVASCRIPT")
    
        aourcecode7 = SourceCodeReport(sourceCodeTab, equation, 'SCILAB')
        sourceCodeTab.AddPage(aourcecode7, "SCILAB")
    
        aourcecode8 = SourceCodeReport(sourceCodeTab, equation, 'MATLAB')
        sourceCodeTab.AddPage(aourcecode8, "MATLAB")



# see the included wxNestedTabsExample.py file
class ResultsDialog(wx.Dialog):
    def __init__(self, parent, msg, caption,
                 pos=wx.DefaultPosition, size=(900,700),
                 style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER, equation=None):
        wx.Dialog.__init__(self, parent, -1, caption, pos, size, style)
        self.CenterOnParent()

        panel = wx.Panel(self)
    
        topLevelResultsNotebook = TopLevelResultsNotebook(panel, equation)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topLevelResultsNotebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()



# Code taken from wx-3.0-gtk2/wx/lib/dialogs.py
class StatusDialog(wx.Dialog):
    def __init__(self, parent, msg, caption,
                 pos=wx.DefaultPosition, size=(500,300),
                 style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, -1, caption, pos, size, style)
        self.CenterOnParent()
        self.text = wx.TextCtrl(self, -1, msg, style=wx.TE_MULTILINE | wx.TE_READONLY)
