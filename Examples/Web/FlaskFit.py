import os, sys, inspect

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2ImportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2ImportDirectory not in sys.path:
    sys.path.append(pyeq2ImportDirectory)
    
import pyeq2, GraphUtils, TextUtils
from flask import Flask
from flask import request


# override Flask's default file cache for the files we generate
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
6.161    11.327 ending text is ignored
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
  2.0 2.6 4.0  ending text is ignored
  1.479  2.957   6.583
  1.387  2.963   6.744
  2.843  1.984   0.0315
  2.485  2.320   0.0639
  0.742  2.568   6.581
  0.607  2.571   6.753
'''

@app.route('/')
def test_curve_fiting_and_plotting():

    # First a simple form for a 2D fitter
    htmlToReturn_2Dform = '' # build this string as we progress
    
    # this HTML table gives an visual outline around the form
    htmlToReturn_2Dform += '<table border=1 cellpadding=20>\n'

    htmlToReturn_2Dform += '<tr><td><b>Example 2D f(x) Web Fitter</b></td></tr>\n'

    # HTML form for the 2D fitter
    htmlToReturn_2Dform += '<tr><td>\n'
    htmlToReturn_2Dform += '<form action="/simplefitter_2D" method="post" target=_blank>\n'

    # text data entry
    htmlToReturn_2Dform += '--- 2D Text Data ---<br>\n'
    htmlToReturn_2Dform += '<textarea  rows="10" cols="45" name="textdata" wrap=off>\n'
    htmlToReturn_2Dform += "Example 2D data for testing\n"
    htmlToReturn_2Dform  += exampleData_2D
    htmlToReturn_2Dform += '</textarea>\n'

    htmlToReturn_2Dform += '<br><br>'

    # radio buttons on form to choose equation
    htmlToReturn_2Dform += '''
    --- Example 2D Equations ---<br>
<input type="radio" name="equation" value="Linear" checked>Linear Polynomial
<br>
<input type="radio" name="equation" value="Quadratic">Quadratic Polynomial
<br>
<input type="radio" name="equation" value="Cubic">Cubic Polynomial
<br>
<input type="radio" name="equation" value="WitchA">Witch Of Maria Agnesi A
<br>
<input type="radio" name="equation" value="VanDeemter">VanDeemter Chromatography
<br>
<input type="radio" name="equation" value="GammaRayDegreesB">Gamma Ray Angular Distribution (degrees) B
<br>
<br>
'''

    htmlToReturn_2Dform += '<input type="submit" value="Submit">\n'
    htmlToReturn_2Dform += '</form>\n' # end of 2D fitter form

    htmlToReturn_2Dform += '<br><br>'
    
    htmlToReturn_2Dform += '<a href="/equationlist_2D">Link to all standard 2D equations</a>\n'
    htmlToReturn_2Dform += '</td></tr></table>\n' # end of 2D fitter table outline



    # now a simple 3D fitter
    htmlToReturn_3Dform = ''
    
    # HTML table gives an visual outline around the form
    htmlToReturn_3Dform += '<table border=1 cellpadding=20>\n'

    htmlToReturn_3Dform += '<tr><td><b>Example 3D f(x,y) Web Fitter</b></td></tr>\n'

    # HTML form for the 3D fitter
    htmlToReturn_3Dform += '<tr><td>\n'
    htmlToReturn_3Dform += '<form action="/simplefitter_3D" method="post" target=_blank>\n'

    # text data entry
    htmlToReturn_3Dform += '--- 3D Text Data ---<br>\n'
    htmlToReturn_3Dform += '<textarea  rows="10" cols="45" name="textdata" wrap=off>\n'
    htmlToReturn_3Dform += "Example 3D data for testing\n"
    htmlToReturn_3Dform  += exampleData_3D
    htmlToReturn_3Dform += '</textarea>\n'

    htmlToReturn_3Dform += '<br><br>\n'

    # radio buttons on form to choose equation
    htmlToReturn_3Dform += '''
    --- Example 3D Equations ---<br>
<input type="radio" name="equation" value="Linear" checked>Linear Polynomial
<br>
<input type="radio" name="equation" value="FullQuadratic">Full Quadratic Polynomial
<br>
<input type="radio" name="equation" value="FullCubic">Full Cubic Polynomial
<br>
<input type="radio" name="equation" value="MonkeySaddleA">Monkey Saddle A
<br>
<input type="radio" name="equation" value="GaussianCurvatureOfWhitneysUmbrellaA">Gaussian Curvature Of Whitneys Umbrella A
<br>
<input type="radio" name="equation" value="NIST_NelsonAutolog">NIST Nelson Autolog
<br>
<br>
'''

    htmlToReturn_3Dform += '<input type="submit" value="Submit">\n'
    htmlToReturn_3Dform += '</form>\n' # end of 3D fitter form

    htmlToReturn_3Dform += '<br><br>'

    htmlToReturn_3Dform += '<a href="/equationlist_3D">Link to all standard 3D equations</a>\n'
    htmlToReturn_3Dform += '</td></tr></table>\n' # end of 3D fitter table outline

    # finish by returning the HTML to Flask
    s = '<html><body>'
    
    s += '<table><tr>'
    s += '<td>' + htmlToReturn_2Dform + '</td>'
    s += '<td> </td>'
    s += '<td>' + htmlToReturn_3Dform + '</td>'
    s += '</tr></table>'
    
    s +='</body></html>'

    return s



@app.route('/simplefitter_2D', methods=['POST'])
def simplefitter_2D_NoFormDataValidation():    
    formTextData = request.form['textdata']
    formEquation = request.form['equation']

    if formEquation == 'Linear':
        equation = pyeq2.Models_2D.Polynomial.Linear()
    elif formEquation == 'Quadratic':
        equation = pyeq2.Models_2D.Polynomial.Quadratic()
    elif formEquation == 'Cubic':
        equation = pyeq2.Models_2D.Polynomial.Cubic()
    elif formEquation == 'WitchA':
        equation = pyeq2.Models_2D.Miscellaneous.WitchOfAgnesiA()
    elif formEquation == 'VanDeemter':
        equation = pyeq2.Models_2D.Engineering.VanDeemterChromatography()
    elif formEquation == 'GammaRayDegreesB':
        equation = pyeq2.Models_2D.LegendrePolynomial.GammaRayAngularDistributionDegreesB()
    
    # the name of the data here is from the form
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(formTextData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_simplefitter_2D.txt" # simplefitter_2D
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_simplefitter_2D.txt" # simplefitter_2D
    TextUtils.SaveSourceCode(sourceCodeFilePath,  equation)

    # create graph
    graphFilePath = "static/model_and_scatterplot_simplefitter_2D.png" # simplefitter_2D
    title = "Example Of An HTML FORM Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(graphFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    absErrorPlotFilePath = "static/abs_error_simplefitter_2D.png" # simplefitter_2D
    title = "Absolute Error For An HTML FORM Model"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath, equation, title, yAxisLabel)

    # generate HTML
    htmlToReturn = ''
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>'
    htmlToReturn +=  '<img src="' + graphFilePath + '"> '
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>'

    return '<html><body>' + htmlToReturn + '</body></html>'



@app.route('/simplefitter_3D', methods=['POST'])
def simplefitter_3D_NoFormDataValidation():
    
    formTextData = request.form['textdata']
    formEquation = request.form['equation']

    if formEquation == 'Linear':
        equation = pyeq2.Models_3D.Polynomial.Linear()
    elif formEquation == 'FullQuadratic':
        equation = pyeq2.Models_3D.Polynomial.FullQuadratic()
    elif formEquation == 'FullCubic':
        equation = pyeq2.Models_3D.Polynomial.FullCubic()
    elif formEquation == 'MonkeySaddleA':
        equation = pyeq2.Models_3D.Miscellaneous.MonkeySaddleA()
    elif formEquation == 'GaussianCurvatureOfWhitneysUmbrellaA':
        equation = pyeq2.Models_3D.Miscellaneous.GaussianCurvatureOfWhitneysUmbrellaA()
    elif formEquation == 'NIST_NelsonAutolog':
        equation = pyeq2.Models_3D.NIST.NIST_NelsonAutolog()
    
    # the name of the data here is from the form
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(formTextData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # save fit statistics to a text file
    fitStatisticsFilePath = "static/fitstatistics_simplefitter_3D.txt" # simplefitter_3D
    TextUtils.SaveCoefficientAndFitStatistics(fitStatisticsFilePath,  equation)

    # save source code to a single text file, all available languages
    sourceCodeFilePath = "static/sourcecode_simplefitter_3D.txt" # simplefitter_3D
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

    absErrorPlotFilePath = "static/abs_error_simplefitter_3D.png" # simplefitter_3D
    title = "Absolute Error For An HTML FORM Model"
    GraphUtils.SaveAbsErrorScatterPlot(absErrorPlotFilePath, equation, title, zAxisLabel)

    # generate HTML
    htmlToReturn = ''
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>\n'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>\n'
    htmlToReturn += '<a href="' + fitStatisticsFilePath + '">Link to parameter and fit statistics</a><br><br>\n'
    htmlToReturn += '<a href="' + sourceCodeFilePath + '">Link to source code, all available languages</a><br><br>\n'
    htmlToReturn +=  '<img src="' + graphFilePath_Surface + '"><br><br>\n'
    htmlToReturn +=  '<img src="' + absErrorPlotFilePath + '"><br><br>\n'
    htmlToReturn +=  '<img src="' + graphFilePath_Contour + '"><br><br>\n'

    return '<html><body>' + htmlToReturn + '</body></html>'



@app.route('/equationlist_2D', methods=['GET'])
def equationlist_2D():
    htmlToReturn = '' # build this as we progress
    
    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in ['Default', 'Offset']:
                        if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                            continue
    
                        equation = equationClass[1]('SSQABS', extendedVersionName)
                        htmlToReturn += '2D ' + submodule[0] + ' --- ' + equation.GetDisplayName() + '<br>\n'
    return '<html><body>' + htmlToReturn + '</body></html>'


@app.route('/equationlist_3D', methods=['GET'])
def equationlist_3D():
    htmlToReturn = '' # build this as we progress
    
    for submodule in inspect.getmembers(pyeq2.Models_3D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in ['Default', 'Offset']:
                        if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                            continue
    
                        equation = equationClass[1]('SSQABS', extendedVersionName)
                        htmlToReturn += '3D ' + submodule[0] + ' --- ' + equation.GetDisplayName() + '<br>\n'
    return '<html><body>' + htmlToReturn + '</body></html>'


if __name__ == '__main__':
    app.run()
