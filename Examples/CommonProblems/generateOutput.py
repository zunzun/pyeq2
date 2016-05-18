import os, sys, copy, numpy, scipy
import numpy.random, inspect

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-master'):raise Exception('Please rename git checkout directory from "pyeq2-master" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2ImportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2ImportDirectory not in sys.path:
    sys.path.append(pyeq2ImportDirectory)

import pyeq2, matplotlib
matplotlib.use('Agg') # must be used prior to the next statement
import matplotlib.pyplot as plt


largeAnimationGraphWidth = 800
largeAnimationGraphHeight = 600
smallAnimationGraphWidth = 200
smallAnimationGraphHeight = 150

# ensure that 360 is evenly divisible by both of these modulus numbers
largeAnimationModulus = 2
smallAnimationModulus = largeAnimationModulus * 5 # multiple of the large modulus

largeAnimationDelayBetweenFrames = 10
# make the visual speed of smaller animation equal to the large animation
smallAnimationDelayBetweenFrames = ((smallAnimationModulus / largeAnimationModulus) *  largeAnimationDelayBetweenFrames) / 2

# the code edits and re-fits this data
# manually set here, then assign as needed
rawData = numpy.array([
    [
        numpy.array([5.357, 5.797, 5.936, 6.161, 6.697, 6.731, 6.775, 8.442, 9.861]),
        []
    ],
    numpy.array([0.376, 0.874, 1.049, 1.327, 2.054, 2.077, 2.138, 4.744, 7.104])
])
rawData[0][1] = numpy.ones(len(rawData[0][0])) # for bug in odr


# common function to create a single plot file
def SaveModelScatterConfidence(in_fileName, in_equation, in_Ymax, in_Ymin):
    
    # raw data
    x_data = in_equation.dataCache.allDataCacheDictionary['IndependentData'][0]
    y_data = in_equation.dataCache.allDataCacheDictionary['DependentData']
    
    # now create data for the fitted in_equation plot
    xModel = numpy.linspace(min(x_data), max(x_data))

    tempcache = in_equation.dataCache
    in_equation.dataCache = pyeq2.dataCache()
    in_equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xModel, xModel])
    in_equation.dataCache.FindOrCreateAllDataCache(in_equation)
    yModel = in_equation.CalculateModelPredictions(in_equation.solvedCoefficients, in_equation.dataCache.allDataCacheDictionary)
    in_equation.dataCache = tempcache
    
    # now use matplotlib to create the PNG file
    if -1 != in_fileName.find('_large'): # large animation frame
        fig = plt.figure(figsize=(float(largeAnimationGraphWidth ) / 100.0, float(largeAnimationGraphHeight ) / 100.0), dpi=100)
    else: # small animation frame
        fig = plt.figure(figsize=(float(smallAnimationGraphWidth ) / 100.0, float(smallAnimationGraphHeight ) / 100.0), dpi=100)
    ax = fig.add_subplot(1,1,1)
    
    # first the raw data as a scatter plot
    if -1 != in_fileName.find('_small'): # small animation frame
        ax.plot(x_data, y_data,  'D', markersize = 2)
    else:
        ax.plot(x_data, y_data,  'D')
    
    # now the model as a line plot
    ax.plot(xModel, yModel, label = 'Fitted Equation')
        
    # now calculate confidence intervals
    # http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_nlin_sect026.htm
    # http://www.staff.ncl.ac.uk/tom.holderness/software/pythonlinearfit
    mean_x = numpy.mean(x_data)	# mean value of x
    n = len(x_data)		# number of samples
    
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
    ax.plot(xModel[booleanMask], upper[booleanMask], linestyle='dashed', color='blue', label = '95% Confidence Intervals')
    
    if -1 != in_fileName.find('_small'): # small animation frame
        ax.set_ylabel("Y Data", size='small') # Y axis data label
        ax.set_xlabel("X Data", size='small') # X axis data label
    else:
        ax.set_ylabel("Y Data") # Y axis data label
        ax.set_xlabel("X Data") # X axis data label
    
    if -1 != in_fileName.find('_small'): # small animation frame
        for xlabel_i in ax.get_xticklabels():
            xlabel_i.set_fontsize(xlabel_i.get_fontsize() * 0.5) 
        for ylabel_i in ax.get_yticklabels():
            ylabel_i.set_fontsize(ylabel_i.get_fontsize() * 0.5)
    
    plt.ylim(in_Ymin, in_Ymax)

    # legends on large images
    # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
    if -1 != in_fileName.find('large'): # large animation frame
        ax.legend(loc=2, fontsize='small')

    fig.tight_layout()
    fig.savefig(in_fileName) # create PNG file
    plt.close('all') # clear pyplot else memory use becomes large


def Outlier_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Single Outlier At End Point'
    htmlText = '''
Outliers are often caused by manual<br>
errors in recording experimental data.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'

    print specificBaseName

    Ymax = 30.0
    Ymin = -10.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = copy.copy(rawData[0])
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = copy.copy(rawData[1])
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            offset = numpy.sin(numpy.radians(i)) * 14.0 # sine wave multiplier per animation frame
            equation.dataCache.allDataCacheDictionary['DependentData'][-1] =  rawData[0][0][-1] + offset
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()
            
            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci194_large.png',
                              specificBaseName + '_ci086_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def Outlier_B():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Single Outlier At Mid Point'
    htmlText = '''
Outliers are often caused by manual<br>
errors in recording experimental data.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'

    print specificBaseName
    
    Ymax = 25.0
    Ymin = -10.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = copy.copy(rawData[0])
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = copy.copy(rawData[1])
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            offset = numpy.sin(numpy.radians(i)) * 14.0 # sine wave multiplier per animation frame
            equation.dataCache.allDataCacheDictionary['DependentData'][6] =  rawData[0][0][6] + offset
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()

            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci200_large.png',
                              specificBaseName + '_ci086_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def Scatter_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Data Scatter Over Entire Range'
    htmlText = '''
The effect of data scatter can be reduced<br>
by increasing the total number of data points.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 25.0
    Ymin = -5.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    numpy.random.seed(7) # yield repeatable results
    noiseArray = numpy.random.random_sample(len(rawData[0][0])) * 14.0 - 7.0
    
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = copy.copy(rawData[0])
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = copy.copy(rawData[1])
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            offsetArray = numpy.sin(numpy.radians(i)) * noiseArray # sine wave multiplier per animation frame
            equation.dataCache.allDataCacheDictionary['DependentData'] =  rawData[0][0] + offsetArray
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()

            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)
 
    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci000_large.png',
                              specificBaseName + '_ci090_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def ParallelData_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Fitting Parallel Data'
    htmlText = '''
This is often caused by environmental<br>
changes during data collection, such as<br>
temperature changes on different days<br>
when making multiple data collection runs.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 15.0
    Ymin = -5.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    xdata = copy.copy(rawData[0][0])
    ydata = copy.copy(rawData[1])

    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = [numpy.append(xdata, xdata), numpy.ones(2 * len(xdata))]
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = numpy.append(ydata, ydata)
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            equation.dataCache.allDataCacheDictionary['DependentData'] = numpy.append(ydata + numpy.sin(numpy.radians(i)) * 4.9, ydata - numpy.sin(numpy.radians(i)) * 4.9)
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()

            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci000_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def LargeStep_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Data With A Large Step'
    htmlText = '''
This is often caused by environmental<br>
changes during data collection such as a<br>
temperature change during a lunch break.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 35.0
    Ymin = -15.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    fixedArray = numpy.array([7.0, 7.0, 7.0, 7.0, 7.0, -7.0, -7.0, -7.0, -7.0])
    
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = copy.copy(rawData[0])
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = copy.copy(rawData[1])
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            offsetArray = numpy.sin(numpy.radians(i)) * fixedArray # sine wave multiplier per animation frame
            equation.dataCache.allDataCacheDictionary['DependentData'] =  rawData[0][0] + offsetArray
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()

            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                    
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)

    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci000_large.png',
                              specificBaseName + '_ci090_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def PoorlyDefined_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Data With A Poorly Defined Region'
    htmlText = '''
This can be mitigated by taking additional<br>
data in the region that is poorly defined.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 1000.0
    Ymin = -1000.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    xbase = numpy.array([0.0, 60.0, 120.0])
    equation.dataCache.allDataCacheDictionary['Weights'] = []
    
    #numpy.random.seed(3)
    #randomArray = (numpy.random.random_sample(len(xbase)+1) - 0.5) * 3.0
    randomArray = numpy.array([-50.0, 50.0, 51.0, -50.0])

    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        numpy.random.seed(3)
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            
            equation = pyeq2.Models_2D.Polynomial.Quadratic('SSQABS')
            xdata = xbase  * (0.45 * numpy.sin(numpy.radians(i)) + 0.5)
            xdata = numpy.append(xdata, numpy.array([120.0]))
            equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xdata, numpy.ones(len(xdata))])
            IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
            equation.dataCache.allDataCacheDictionary['DependentData'] =  xdata + randomArray
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()

            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci022_large.png',
                              specificBaseName + '_ci090_large.png',
                              specificBaseName + '_ci270_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def RandomData_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Fitting Random Data'
    htmlText = '''
This illustrates the effect of fitting completely<br>
random data that has no relationship of any kind.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 1.0
    Ymin = 0.0
    
    equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    numpy.random.seed(3) # yield repeatable results
    randomArrayX = numpy.random.random_sample(195)
    randomArrayY = numpy.random.random_sample(195)
    equation.dataCache.allDataCacheDictionary['Weights'] = []
    
    # ensure a X data range for the graph, as on
    # all other plots the X data range is constant
    randomArrayX[0] = 0.001
    randomArrayX[1] = 0.999
    
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            index = i
            if i > 180:
                index = 180 - (i%180)
            equation = pyeq2.Models_2D.Polynomial.Linear('SSQABS')
            xdata = randomArrayX[:15 + index/2]
            ydata = randomArrayY[:15 + index/2]
            equation.dataCache.allDataCacheDictionary['IndependentData'] = numpy.array([xdata, numpy.ones(len(xdata))])
            IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
            equation.dataCache.allDataCacheDictionary['DependentData'] =  ydata
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()
            
            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci000_large.png',
                              specificBaseName + '_ci180_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]


def MissingOffset_A():
    specificBaseName = inspect.stack()[0][3]
    htmlTitle = 'Equation Missing An Offset'
    htmlText = '''
This illustrates the effect of fitting data with<br>
an offset to an equation that does not have one.<br>
<br>
This can be caused by experimental equipment<br>
introducing bias (such as a DC offset) during<br>
data acquisition.  Fitting the data to an<br>
equation with an offset will reveal the bias.'''
    thumbnailAnimationName = specificBaseName + '_small.gif'
    fullsizeAnimationName = specificBaseName + '_large.gif'
    
    print specificBaseName

    Ymax = 14.0
    Ymin = -4.0
    
    equation = pyeq2.Models_2D.Exponential.SimpleExponential('SSQABS')
    dimensionality = equation.GetDimensionality()
    equation.dataCache.DependentDataContainsZeroFlag = True # do not need relative error calculations, this flag turns them off
        
    fixedArray = numpy.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    
    for i in range(0, 360):
        extraZerosString = ''
        if i < 100:
            extraZerosString = '0'
        if i < 10:
            extraZerosString = '00'
        
        equation.dataCache.allDataCacheDictionary['IndependentData'] = copy.copy(rawData[0])
        IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
        equation.dataCache.allDataCacheDictionary['DependentData'] = copy.copy(rawData[1])
        equation.dataCache.allDataCacheDictionary['Weights'] = []
        
        if not i % largeAnimationModulus:
            print i,;sys.stdout.flush()
            offset = numpy.fabs(i-180) / 90.0
            equation.dataCache.allDataCacheDictionary['IndependentData'] =  numpy.array([fixedArray, numpy.ones(len(fixedArray))])
            IndependentDataArray = equation.dataCache.allDataCacheDictionary['IndependentData']
            equation.dataCache.allDataCacheDictionary['DependentData'] =  numpy.power(2.0, fixedArray + offset)
            DependentDataArray = equation.dataCache.allDataCacheDictionary['DependentData']
            equation.dataCache.allDataCacheDictionary['Weights'] =  []
            equation.Solve()
            equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
            equation.CalculateCoefficientAndFitStatistics()
            
            fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_large.png'
            SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
            
            # small animation, create fewer frames
            if not (i % smallAnimationModulus):
                graphWidth = smallAnimationGraphWidth
                graphHeight = smallAnimationGraphHeight
                fileName = specificBaseName + '_ci' + extraZerosString + str(i) + '_small.png'
                SaveModelScatterConfidence(fileName, equation, Ymax, Ymin)
                
    print
    # convert all PNG files to GIF for gifsicle to use
    commandString = 'mogrify -format gif *png'
    print "Calling " + commandString
    os.popen(commandString)
    
    # make small GIF animation
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(smallAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*small.gif > ' + specificBaseName + '_small.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # make large GIF animation        
    commandString = 'gifsicle --loop --colors 256 --delay ' + str(largeAnimationDelayBetweenFrames) + " " + specificBaseName + '_ci*large.gif > ' + specificBaseName + '_large.gif'
    print "Calling " + commandString
    os.popen(commandString)

    # remove unused files, saving the ones in this list
    stillImageFileNameList = [specificBaseName + '_ci180_large.png',
                              specificBaseName + '_ci270_large.png',
                              specificBaseName + '_ci000_large.png']
    currentDir = os.listdir('.')
    for filename in currentDir:
        if (-1 != filename.find('_ci')) and (-1 != filename.find('small')):
            os.remove(filename)
        if (-1 != filename.find('_ci')) and (-1 != filename.find('large.gif')):
            os.remove(filename)
        if (-1 != filename.find(specificBaseName)) and (-1 != filename.find('_large.png')) and (filename not in stillImageFileNameList):
            os.remove(filename)

    return [htmlTitle, htmlText, specificBaseName, stillImageFileNameList]



# HTML and image  generation
htmlInfo = []
htmlInfo.append( Outlier_A() )
htmlInfo.append( Outlier_B() )
htmlInfo.append( ParallelData_A() )
htmlInfo.append( LargeStep_A() )
htmlInfo.append( PoorlyDefined_A() )
htmlInfo.append( MissingOffset_A() )
htmlInfo.append( Scatter_A() )
htmlInfo.append( RandomData_A() )

# individual HTML files
for i in htmlInfo:
    individualFile = open(i[2] + '.html', 'w')
    individualFile.write('<html><body><center>')
    individualFile.write('<br><b>' + i[0] + '</b><br><br>' + i[1] + '<br>')
    individualFile.write('<img src="' + i[2] + '_large.gif"><br><br><br>---- <b>Still Images</b> -----<br>')
    for fileName in i[3]:
        individualFile.write('<img src="' + fileName + '"><br><br>')
    individualFile.write('</body></html>')
    individualFile.close()

# top-level index.html file
htmlIndexFile = open('index.html', 'w')
htmlIndexFile.write('<html><body><table align="center"border=1>\n')
for i in htmlInfo:
    htmlIndexFile.write('<tr><td align="center">')
    htmlIndexFile.write('<br><br><b>' + i[0] + '</b><br><br><a href="' + i[2] + '.html"><img src="' + i[2] + '_small.gif">')
    htmlIndexFile.write('<br><br>High resolution animation<br>and still images</a><br><br></td>\n<td><large>' + i[1] + '</large></td></tr>\n')
htmlIndexFile.write('</table></body></html>')
htmlIndexFile.close()
