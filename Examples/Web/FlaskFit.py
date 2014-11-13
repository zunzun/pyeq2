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

exampleData = '''
  X        Y
5.357    10.376
5.457    10.489
5.797    10.874
5.936    11.049
6.161    11.327
6.697    12.054
6.731    12.077
6.775    12.138
8.442    14.744
9.769    17.068
9.861    17.104
'''

@app.route('/')
def test_curve_fiting_and_plotting():

    htmlToReturn = '' # build this as we progress through the example
    
    # fitting a straight line is simple
    equation=pyeq2.Models_2D.Polynomial.Linear()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()
    
    # well, that was easy.  Now for the graphing
    outputFilePath = "static/scatterplot_one.png" # one
    title = "Example With A Simple Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
 
    # now create plot as a PNG file
    GraphUtils.SaveModelScatterConfidence(outputFilePath, equation, title, xAxisLabel, yAxisLabel) 
    htmlToReturn +=  '<img src="' + outputFilePath + '">'


    htmlToReturn += '<br><br>'

    
    # now fit a more complex model (see the pyeq2 library)
    # Maxwell-Wiechert with offset, fit to lowest SSQ Relative error
    equation=pyeq2.Models_2D.Engineering.MaxwellWiechert_1('SSQREL', 'Offset')
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()
    
    outputFilePath = "static/scatterplot_two.png" # two
    title = "Example With A Complex Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
 
    # now create plot as a PNG file
    GraphUtils.SaveModelScatterConfidence(outputFilePath, equation, title, xAxisLabel, yAxisLabel) 
    htmlToReturn +=  '<img src="' + outputFilePath + '">'

    
    htmlToReturn += '<br><br>'

    
    # now create a poorly fitting model
    equation=pyeq2.Models_2D.Exponential.SimpleExponential()
    pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(exampleData, equation, False)
    equation.Solve()
    equation.CalculateModelErrors(equation.solvedCoefficients, equation.dataCache.allDataCacheDictionary)
    equation.CalculateCoefficientAndFitStatistics()
    
    outputFilePath = "static/scatterplot_three.png" # three
    title = "Example With A Poorly Fitting Model"
    xAxisLabel = "X data"
    yAxisLabel = "Y data"
 
    # now create plot as a PNG file
    GraphUtils.SaveModelScatterConfidence(outputFilePath, equation, title, xAxisLabel, yAxisLabel) 
    htmlToReturn +=  '<img src="' + outputFilePath + '">'

    return htmlToReturn

if __name__ == '__main__':
    app.run()
