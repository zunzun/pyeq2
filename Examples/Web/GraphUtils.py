import os, sys

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import matplotlib
import matplotlib.pyplot as plt
import numpy, scipy, pyeq2


def SaveModelScatterConfidence(in_filePath, in_equation, in_title, in_xAxisLabel, in_yAxisLabel):
    
    # raw data
    x_data = in_equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = in_equation.dataCache.allDataCacheDictionary['DependentData']
    
    # now create data for the fitted in_equation plot
    xModel = numpy.linspace(min(x_data), max(x_data))

    in_equation.dataCache = pyeq2.dataCache()
    in_equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xModel, xModel])
    in_equation.dataCache.FindOrCreateAllDataCache(in_equation)
    yModel = in_equation.CalculateModelPredictions(in_equation.solvedCoefficients, in_equation.dataCache.allDataCacheDictionary)
    
    # now use matplotlib to create the PNG file
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1,1,1)
    
    # first the raw data as a scatter plot
    ax.plot(x_data, y_data,  '+')
    
    # now the model as a line plot
    ax.plot(xModel, yModel)
    
    # now calculate confidence intervals
    # http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_nlin_sect026.htm
    # http://www.staff.ncl.ac.uk/tom.holderness/software/pythonlinearfit
    mean_x = numpy.mean(x_data)			# mean of x
    n = in_equation.nobs		    # number of samples in the origional fit
    
    t_value = scipy.stats.t.ppf(0.975, in_equation.df_e) # (1.0 - (a/2)) is used for two-sided t-test critical value, here a = 0.05
                            
    confs = t_value * numpy.sqrt((in_equation.sumOfSquaredErrors/in_equation.df_e)*(1.0/n + (numpy.power((xModel-mean_x),2.0)/
                                ((numpy.sum(numpy.power(x_data,2)))-n*(numpy.power(mean_x,2.0))))))

    # get lower and upper confidence limits based on predicted y and confidence intervals
    upper = yModel + abs(confs)
    lower = yModel - abs(confs)
    
    # mask off any numbers outside the existing plot limits
    booleanMask = yModel > matplotlib.pyplot.ylim()[0]
    booleanMask &= (yModel < matplotlib.pyplot.ylim()[1])
    
    # color scheme improves visibility on black background lines or points
    ax.plot(xModel[booleanMask], lower[booleanMask], linestyle='solid', color='white')
    ax.plot(xModel[booleanMask], upper[booleanMask], linestyle='solid', color='white')
    ax.plot(xModel[booleanMask], lower[booleanMask], linestyle='dashed', color='blue')
    ax.plot(xModel[booleanMask], upper[booleanMask], linestyle='dashed', color='blue')
    
    ax.set_title(in_title) # add a title
    ax.set_xlabel(in_xAxisLabel) # X axis data label
    ax.set_ylabel(in_yAxisLabel) # Y axis data label
    
    fig.savefig(in_filePath) # create PNG file


def SurfaceAndContourPlots(in_filePathSurface, in_filePathContour, in_equation,
                           in_surfaceTitle, in_contourTitle,
                           in_xAxisLabel, in_yAxisLabel, in_zAxisLabel):

    # raw data
    x_data = in_equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = in_equation.dataCache.allDataCacheDictionary['IndependentData'][1]
    z_data = in_equation.dataCache.allDataCacheDictionary['DependentData']

    from mpl_toolkits.mplot3d import Axes3D # 3D apecific
    from matplotlib import cm # to colormap from blue to red
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    xModel = numpy.linspace(min(x_data), max(x_data), 20)
    yModel = numpy.linspace(min(y_data), max(y_data), 20)
    X, Y = numpy.meshgrid(xModel, yModel)

    in_equation.dataCache = pyeq2.dataCache()
    in_equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([X, Y])
    in_equation.dataCache.FindOrCreateAllDataCache(in_equation)
    Z = in_equation.CalculateModelPredictions(in_equation.solvedCoefficients, in_equation.dataCache.allDataCacheDictionary)
    
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=1, antialiased=True)
    
    ax.set_title(in_surfaceTitle) # add a title for surface plot
    ax.set_xlabel(in_xAxisLabel) # X axis data label
    ax.set_ylabel(in_yAxisLabel) # Y axis data label
    ax.set_zlabel(in_zAxisLabel) # Y axis data label
    
    fig.savefig(in_filePathSurface) # create PNG file

    # contour plot here
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1,1,1)

    ax.plot(x_data, y_data, 'o', color='0.8', markersize=3) # draw these first so contour lines overlay.  Color=number is grayscale

    ax.set_title(in_contourTitle) # add a title for contour plot
    ax.set_xlabel(in_xAxisLabel) # X data label
    ax.set_ylabel(in_yAxisLabel) # Y data label

    numberOfContourLines = 10
    plt.contour(X, Y, Z, numberOfContourLines, colors='k')
    fig.savefig(in_filePathContour) # create PNG file


