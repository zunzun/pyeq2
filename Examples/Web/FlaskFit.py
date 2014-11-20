import os, sys

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2, GraphUtils, TextUtils
from flask import Flask



# override Flask's default 60 second file cache for the files we generate
class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('.png'):
            return 0.000001
        if name.lower().endswith('.txt'):
            return 0.000001
        return flask.Flask.get_send_file_max_age(self, name)


app = MyFlask(__name__)
app.debug = True # only for development, never for production



exampleData_2D = '''
  X        Y
5.357    10.376
5.457    10.489
5.936    11.049
6.161    11.327
6.697    12.054
8.442    14.744
9.769    17.068
9.861    17.104
'''

exampleData_3D = '''
    X      Y       Z
  3.017  2.175   0.0320
  2.822  2.624   0.0629
  1.784  3.144   6.570
  1.712  3.153   6.721
  2.972  2.106   0.0313
  2.719  2.542   0.0643
  1.479  2.957   6.583
  1.387  2.963   6.744
  2.843  1.984   0.0315
  2.485  2.320   0.0639
  0.742  2.568   6.581
  0.607  2.571   6.753
'''

@app.route('/')
def test_curve_fiting_and_plotting():

    htmlToReturn = '' # build this as we progress through the example
    
    htmlToReturn += '<center>' # makes the output slightly more appealing



    # fit a straight line
    print "Simple Model"
    equation=pyeq2.Models_2D.Polynomial.Linear()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_one.txt" # one
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_one.txt" # one
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graphs
    graphFilePath = "static/model_and_scatterplot_one.png" # one
    title = "Example Of A Simple Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(graphFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    absErrorPlotFilePath = "static/abs_error_one.png" # one
    title = "Absolute Error For Simple Model"
    xAxisLabel = "X data"
    yAxisLabel = "Absolute Error"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'



    htmlToReturn += '<br><br><br> <hr> <br><br><br>'


    
    # fit a more complex model (see the pyeq2 library)
    print "Complex Model"
    # Maxwell-Wiechert with offset, fit to lowest SSQ Relative error
    equation=pyeq2.Models_2D.Engineering.MaxwellWiechert_1('SSQREL', 'Offset')
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_two.txt" # two
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_two.txt" # two
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graph
    graphFilePath = "static/model_and_scatterplot_two.png" # two
    title = "Example Of A Complex Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(graphFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    absErrorPlotFilePath = "static/abs_error_two.png" # two
    title = "Absolute Error For Complex Model"
    xAxisLabel = "X data"
    yAxisLabel = "Absolute Error"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'


    
    htmlToReturn += '<br><br><br> <hr> <br><br><br>'


    
    # now a poorly fitting model
    print "Poorly Fitting Nodel"
    equation=pyeq2.Models_2D.Exponential.SimpleExponential()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_three.txt" # three
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_three.txt" # three
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graph
    graphFilePath = "static/model_and_scatterplot_three.png" # three
    title = "Example Of A Poorly Fitting Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(graphFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    absErrorPlotFilePath = "static/abs_error_three.png" # three
    title = "Absolute Error For Poorly Fitting Model"
    xAxisLabel = "X data"
    yAxisLabel = "Absolute Error"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'



    htmlToReturn += '<br><br><br> <hr> <br><br><br>'



    # fit a 3D surface
    print "Surface Model"
    # Polynomial Full Cubic
    equation=pyeq2.Models_3D.Polynomial.FullCubic()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_3D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_four.txt" # four
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_four.txt" # four
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graphs
    graphFilePath_Surface = "static/surface.png" # surface plot
    graphFilePath_Contour = "static/contour.png" # contour plot
    surfaceTitle = "Example Surface Plot"
    contourTitle = "Example Contour Plot"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    zAxisLabel = "Z data"
    GraphUtils.SurfaceAndContourPlots(graphFilePath_Surface,
                                      graphFilePath_Contour,
                                      equation, surfaceTitle, contourTitle,
                                      xAxisLabel, yAxisLabel, zAxisLabel)    

    absErrorPlotFilePath = "static/abs_error_four.png" # four
    title = "Absolute Error For Surface Plot"
    xAxisLabel = "X data"
    yAxisLabel = "Absolute Error"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath_Surface + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath_Contour + '"><br><br>'



    htmlToReturn += '<br><br><br> <hr> <br><br><br>'



    # make a simple form for interactive fitting
    htmlToReturn += 'Simple web fitter<br><br>'
    htmlToReturn += '<form action="/simplefitter" method="post">'
    htmlToReturn += '<input type="radio" name="equation" value="Linear" checked>Linear Equation'
    htmlToReturn += '<br>'
    htmlToReturn += '<input type="radio" name="equation" value="Quadratic">Quadratic Equation'
    htmlToReturn += '<br>'
    htmlToReturn += '<input type="radio" name="equation" value="Cubic">Cubic Equation'
    htmlToReturn += '<br><br>'
    htmlToReturn += 'Text Data<br>'
    htmlToReturn += '<textarea  rows="10" cols="25" name="textdata">'
    htmlToReturn  += exampleData_2D
    htmlToReturn += '</textarea>'
    htmlToReturn += '<br><br>'
    htmlToReturn += '<input type="submit" value="Submit">'
    htmlToReturn += '</form>'    
    
    
    # finish by returning the HTML to Flask
    return htmlToReturn



@app.route('/simplefitter', methods=['POST'])
def simplefitterWithNoFormDataValidation():
    from flask import request
    htmlToReturn = '' # build this HTML as we progress
    
    formTextData = request.form['textdata']
    formEquation = request.form['equation']

    if formEquation == 'Linear':
        equation = pyeq2.Models_2D.Polynomial.Linear()
    elif formEquation == 'Quadratic':
        equation = pyeq2.Models_2D.Polynomial.Quadratic()
    elif formEquation == 'Cubic':
        equation = pyeq2.Models_2D.Polynomial.Cubic()
    
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(formTextData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_simplefitter.txt" # simplefitter
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_simplefitter.txt" # simplefitter
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graph
    graphFilePath = "static/model_and_scatterplot_simplefitter.png" # simplefitter
    title = "Example Of An HTML FORM Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(graphFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    absErrorPlotFilePath = "static/abs_error_simplefitter.png" # simplefitter
    title = "Absolute Error For An HTML FORM Model"
    xAxisLabel = "X data"
    yAxisLabel = "Absolute Error"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'

    return htmlToReturn



if __name__ == '__main__':
    app.run()
