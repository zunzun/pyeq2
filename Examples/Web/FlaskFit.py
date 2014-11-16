import os, sys

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2, GraphUtils
from flask import Flask


app = Flask(__name__)
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
    equation=pyeq2.Models_2D.Polynomial.Linear()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()
    
    # create graph
    outputFilePath = "static/scatterplot_one.png" # one
    title = "Example Of A Simple Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"    
    GraphUtils.SaveModelScatterConfidence(outputFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br>'
    htmlToReturn +=  '<img src="' + outputFilePath + '">'


    htmlToReturn += '<br><br><br> <hr> <br><br><br>'

    
    # fit a more complex model (see the pyeq2 library)
    # Maxwell-Wiechert with offset, fit to lowest SSQ Relative error
    equation=pyeq2.Models_2D.Engineering.MaxwellWiechert_1('SSQREL', 'Offset')
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # create graph
    outputFilePath = "static/scatterplot_two.png" # two
    title = "Example Of A Complex Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(outputFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br>'
    htmlToReturn +=  '<img src="' + outputFilePath + '">'

    
    htmlToReturn += '<br><br><br> <hr> <br><br><br>'

    
    # now a poorly fitting model
    equation=pyeq2.Models_2D.Exponential.SimpleExponential()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_2D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()
    
    # create graph
    outputFilePath = "static/scatterplot_three.png" # three
    title = "Example Of A Poorly Fitting Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    GraphUtils.SaveModelScatterConfidence(outputFilePath,
                                          equation, title, xAxisLabel, yAxisLabel) 

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn +=  '<img src="' + outputFilePath + '">'


    # now a 3D surface and contour plot


    htmlToReturn += '<br><br><br> <hr> <br><br><br>'

    
    # fit a 3D surface
    # Polynomial Full Cubic
    equation=pyeq2.Models_3D.Polynomial.FullCubic()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData_3D, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()

    # create graphs
    outputFilePath_Surface = "static/surface.png" # surface plot
    outputFilePath_Contour = "static/contour.png" # contour plot
    surfaceTitle = "Example Surface Plot"
    contourTitle = "Example Contour Plot"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
    zAxisLabel = "Z data"
    GraphUtils.SurfaceAndContourPlots(outputFilePath_Surface,
                                      outputFilePath_Contour,
                                      equation, surfaceTitle, contourTitle,
                                      xAxisLabel, yAxisLabel, zAxisLabel)    

    # generate HTML
    htmlToReturn +=  equation.GetDisplayName() + '<br><br>'
    htmlToReturn +=  equation.GetDisplayHTML() + '<br><br>'
    htmlToReturn +=  '<img src="' + outputFilePath_Surface + '"><br><br>'
    htmlToReturn +=  '<img src="' + outputFilePath_Contour + '"><br><br>'


    # done fitting, finish by returning HTML
    return htmlToReturn


if __name__ == '__main__':
    app.run()
