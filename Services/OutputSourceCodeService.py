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

cppOutputSourceCodeUpperComment = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me directly using zunzun@zunzun.com.
//
//      James

'''

class OutputSourceCodeService(object):

    def ConvertCppToCSHARP(self, inString):
        newString = inString.replace('abs(', 'Math.Abs(')
        newString = newString.replace('pow(', 'Math.Pow(')
        newString = newString.replace('log(', 'Math.Log(')
        newString = newString.replace('log10(', 'Math.Log10(')
        newString = newString.replace('exp(', 'Math.Exp(')
        newString = newString.replace('cos(', 'Math.Cos(')

        newString = newString.replace('asin(', 'ASIN(') # so sin is not confused with asin
        newString = newString.replace('sin(', 'Math.Sin(')
        newString = newString.replace('ASIN(', 'Math.Asin(')
        
        newString = newString.replace('atan(', 'ATAN(') # so tan is not confused with atan
        newString = newString.replace('tan(', 'Math.Tan(')
        newString = newString.replace('ATAN(', 'Math.Atan(')
                        
        newString = newString.replace('tanh(', 'Math.Tanh(')
        newString = newString.replace('cosh(', 'Math.Cosh(')
        if newString[0] == '\t':
            newString = '\t' + newString
        newString = newString.replace('\n\t', '\n\t\t')
        return newString


    def ConvertCppToVBA(self, inString):
        newString = inString.replace(';', '') # no need for semicolons
        newString = newString.replace('double ', 'var ')
        newString = newString.replace('temp += ', 'temp = temp + ')
        newString = newString.replace('temp -= ', 'temp = temp - ')
        newString = newString.replace('abs(', 'Abs(')
        newString = newString.replace('pow(', 'Application.WorksheetFunction.power(')
        newString = newString.replace('log(', 'Application.WorksheetFunction.ln(')
        newString = newString.replace('log10(', 'Application.WorksheetFunction.log(')
        newString = newString.replace('exp(', 'Exp(')
        #newString = newString.replace('sin(', 'math.sin(')
        #newString = newString.replace('cos(', 'math.cos(')
        #newString = newString.replace('tan(', 'math.tan(')
        newString = newString.replace('tanh(', 'Application.WorksheetFunction.tanh(')
        newString = newString.replace('cosh(', 'Application.WorksheetFunction.cosh(')
        newString = newString.replace('//', "'") # comment token
        return newString


    def ConvertCppToPYTHON(self, inString):
        newString = inString.replace(';', '') # no need for semicolons
        newString = newString.replace('double ', '')
        newString = newString.replace('abs(', 'math.fabs(')
        newString = newString.replace('pow(', 'math.pow(')
        newString = newString.replace('log(', 'math.log(')
        newString = newString.replace('log10(', 'math.log10(')
        newString = newString.replace('exp(', 'math.exp(')
        newString = newString.replace('cos(', 'math.cos(')
        
        newString = newString.replace('asin(', 'ASIN(') # so sin is not confused with asin
        newString = newString.replace('sin(', 'math.sin(')
        newString = newString.replace('ASIN(', 'math.asin(')
        
        newString = newString.replace('atan(', 'ATAN(') # so tan is not confused with atan
        newString = newString.replace('tan(', 'math.tan(')
        newString = newString.replace('ATAN(', 'math.atan(')
        
        newString = newString.replace('tanh(', 'math.tanh(')
        newString = newString.replace('cosh(', 'math.cosh(')
        newString = newString.replace('//', '#') # comment token
        newString = newString.replace('\t', '    ')
        return newString


    def ConvertCppToJAVA(self, inString):
        newString = inString.replace('abs(', 'Math.abs(')
        newString = newString.replace('pow(', 'Math.pow(')
        newString = newString.replace('log(', 'Math.log(')
        newString = newString.replace('log10(', 'Math.log10(')
        newString = newString.replace('exp(', 'Math.exp(')
        newString = newString.replace('cos(', 'Math.cos(')
        
        newString = newString.replace('asin(', 'ASIN(') # so sin is not confused with asin
        newString = newString.replace('sin(', 'Math.sin(')
        newString = newString.replace('ASIN(', 'Math.asin(')

        newString = newString.replace('atan(', 'ATAN(') # so tan is not confused with atan
        newString = newString.replace('tan(', 'Math.tan(')
        newString = newString.replace('ATAN(', 'Math.atan(')
        
        newString = newString.replace('tanh(', 'Math.tanh(')
        newString = newString.replace('cosh(', 'Math.cosh(')
        if newString[0] == '\t':
            newString = '\t' + newString
        newString = newString.replace('\n\t', '\n\t\t')
        return newString


    def ConvertCppToJULIA(self, inString):
        newString = inString.replace(';', '') # no need for semicolons
        newString = newString.replace('double ', '')
        newString = newString.replace('//', "#") # comment token
        return newString


    def ConvertCppToFORTRAN90(self, inString):
        newString = inString.replace(';', '') # no need for semicolons
        newString = newString.replace('temp += ', 'temp = temp + ')
        newString = newString.replace('double ', 'real :: ')
        newString = newString.replace('//', "!") # comment token
        return newString


    def ConvertCppToSCILAB(self, inString):
        newString = inString.replace('double ', '')
        newString = newString.replace('temp += ', 'temp = temp + ')
        newString = newString.replace('temp -= ', 'temp = temp - ')
        newString = newString.replace('pow(', 'power(')
        return newString


    def ConvertCppToMATLAB(self, inString):
        newString = inString.replace('pow(', 'power(')
        newString = newString.replace('double ', '')
        newString = newString.replace('temp += ', 'temp = temp + ')
        newString = newString.replace('temp -= ', 'temp = temp - ')
        newString = newString.replace('*', '.*') # multiply
        newString = newString.replace('//', '%') # comment token
        newString = newString.replace('/', './') # divide
        return newString


    def GetOutputSourceCodeCPP(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            if inEquation.GetDimensionality() == 2:
                return self.SplineCodeCPP_2D(inEquation)
            if inEquation.GetDimensionality() == 3:
                return self.SplineCodeCPP_3D(inEquation)
    
        s = cppOutputSourceCodeUpperComment
        s += '\n#include <math.h>\n\n'
        s += '// Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '// Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        s += 'double ' + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation)
        if inEquation.GetDimensionality() == 2:
            s += '_model(double x_in)'
        else:
            s += '_model(double x_in, double y_in)'
        s += '''
{
	double temp;
	temp = 0.0;

	// coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += '	double ' + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ';\n'
        s += '\n' + inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation)
        s += '''	return temp;
}
'''
        return s


    def GetOutputSourceCodeCSHARP(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToCSHARP(cppOutputSourceCodeUpperComment)
        s += '\nusing System;\n\n'
        s += '// Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '// Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        s += "class " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation)+ "\n{\n"
        if inEquation.GetDimensionality() == 2:
            s += "\tdouble " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(double x_in)\n\t{\n"
        else:
            s += "\tdouble " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(double x_in, double y_in)\n\t{\n"
        s += '''\t\tdouble temp;
\t\ttemp = 0.0;

\t\t// coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\t\tdouble " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ";\n"
        s += "\n"
        
        s += self.ConvertCppToCSHARP(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))

        s += "\t\treturn temp;\n\t}\n}\n"
        return s


    def GetOutputSourceCodeVBA(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToVBA(cppOutputSourceCodeUpperComment)
        s += '\' Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '\' Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "Public Function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation)+ "_model(x_in)\n"
        else:
            s += "Public Function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n"
        s += '''\ttemp = 0.0

\t' coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\tConst " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + "\n"
        s += "\n"

        s += self.ConvertCppToVBA(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))

        s += "\t" + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model = temp\n"
        s += "End Function\n"
        return s


    def GetOutputSourceCodePYTHON(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            if inEquation.GetDimensionality() == 2:
                return self.SplineCodePYTHON_2D(inEquation)
            if inEquation.GetDimensionality() == 3:
                return self.SplineCodePYTHON_3D(inEquation)
    
        s = self.ConvertCppToPYTHON(cppOutputSourceCodeUpperComment)
        s += '\nimport math\n\n'
        s += '# Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '# Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "def " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in):\n"
        else:
            s += "def " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation)+ "_model(x_in, y_in):\n"
        s += '''    temp = 0.0

    # coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "    " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + "\n"
        s += "\n"

        s += self.ConvertCppToPYTHON(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))

        s += "    return temp\n"
        return s


    def GetOutputSourceCodeJAVA(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            if inEquation.GetDimensionality() == 2:
                return self.SplineCodeJAVA_2D(inEquation)
            if inEquation.GetDimensionality() == 3:
                return self.SplineCodeJAVA_3D(inEquation)
    
        s = self.ConvertCppToJAVA(cppOutputSourceCodeUpperComment)        
        s += '\nimport java.lang.Math;\n\n'
        s += '// Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '// Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        s += "class " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation)+ "\n{\n"
        if inEquation.GetDimensionality() == 2:
            s += "\tdouble " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(double x_in)\n\t{\n"
        else:
            s += "\tdouble " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(double x_in, double y_in)\n\t{\n"
        s += '''\t\tdouble temp;
\t\ttemp = 0.0;

\t\t// coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\t\tdouble " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ";\n"
        s += "\n"
        
        s += self.ConvertCppToJAVA(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))

        s += "\t\treturn temp;\n\t}\n}\n"
        return s


    def GetOutputSourceCodeJAVASCRIPT(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            if inEquation.GetDimensionality() == 2:
                return self.SplineCodeJAVASCRIPT_2D(inEquation)
            if inEquation.GetDimensionality() == 3:
                return self.SplineCodeJAVASCRIPT_3D(inEquation)
    
        s = self.ConvertCppToJAVA(cppOutputSourceCodeUpperComment) # reuse existing code
        s += '\n'
        s += '// Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '// Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in)\n\t{\n"
        else:
            s += "function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n\t{\n"
        s += '''\tvar temp;
\ttemp = 0.0;

\t// coefficients
'''
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\tvar " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ";\n"
        s += "\n"
        
        s += self.ConvertCppToJAVA(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation)).replace('\t\ttemp', '\ttemp')

        s += "\treturn temp;\n}\n"
        return s


    def GetOutputSourceCodeSCILAB(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToSCILAB(cppOutputSourceCodeUpperComment)
        s += '\n'
        s += '// Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '// Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "function y = " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in)\n"
        else:
            s += "function z = " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n"
        s += "\ttemp = 0.0;\n\n"

        s += "\t// coefficients\n"
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\t" + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ";\n"
        s += "\n"
        
        s += self.ConvertCppToSCILAB(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))
        
        if inEquation.GetDimensionality() == 2:
            s += "\n\ty = temp;\n"
        else:
            s += "\n\tz = temp;\n"
        s += "endfunction\n"
        return s


    def GetOutputSourceCodeMATLAB(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToMATLAB(cppOutputSourceCodeUpperComment)
        s += '\n'
        s += '% Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '% Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "function y = " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in)\n"
        else:
            s += "function z = " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n"
        s += "\ttemp = 0.0;\n\n"

        s += "\t% coefficients\n"
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\t" + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + ";\n"
        s += "\n"

        s += self.ConvertCppToMATLAB(inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation))

        if inEquation.GetDimensionality() == 2:
            s += "\n\ty = temp;\n"
        else:
            s += "\n\tz = temp;\n"
        return s


    def GetOutputSourceCodeJULIA(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToJULIA(cppOutputSourceCodeUpperComment)
        s += '\n'
        cppSourceCode = inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation)
        if -1 != cppSourceCode.find('pow('):
            s += '# julia has no power function, only an operator, create\n'
            s += '# a function for pyeq2 automated source code generation\n'
            s += 'pow(x,y) = x ^ y\n'
            s += '\n'
        s += '# Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '# Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in)\n"
        else:
            s += "function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n"
        s += "\ttemp = 0.0\n\n"

        s += "\t# coefficients\n"
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "\t" + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + "\n"
        s += "\n"

        s += self.ConvertCppToJULIA(cppSourceCode)

        s += "\nend\n"
        return s


    def GetOutputSourceCodeFORTRAN90(self, inEquation, inDigitsOfPrecisionString = '16'):
        if inEquation.splineFlag == True:
            raise NotImplementedError('Not implemented for splines')

        s = self.ConvertCppToFORTRAN90(cppOutputSourceCodeUpperComment)
        s += '\n'
        cppSourceCode = inEquation.extendedVersionHandler.AssembleOutputSourceCodeCPP(inEquation)
        if -1 != cppSourceCode.find('pow('):
            s += '! fortran90 has no power function, only an operator, create\n'
            s += '! a function for pyeq2 automated source code generation\n'
            s += 'real function pow(a, b)\n'
            s += 'real :: a ! input\n'
            s += 'real :: b ! input\n'
            s += 'real :: c ! output\n'
            s += 'c = a**b\n'
            s += 'end function pow\n'
            s += '\n'
        s += '! Fitting target: lowest ' + inEquation.fittingTargetDictionary[inEquation.fittingTarget] + '\n'
        s += '! Fitting target value = ' + str(inEquation.CalculateAllDataFittingTarget(inEquation.solvedCoefficients)) + '\n\n'
        if inEquation.GetDimensionality() == 2:
            s += "real function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in)\n"
            s += 'real :: x_in ! input\n'
        else:
            s += "real function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model(x_in, y_in)\n"
            s += 'real :: x_in ! input\n'
            s += 'real :: y_in ! input\n'
        s += " real :: temp ! output\n\n"

        s += "! coefficients\n"
        cd = inEquation.extendedVersionHandler.AssembleCoefficientDesignators(inEquation)
        tempString = " = %-." + inDigitsOfPrecisionString + "E"
        for i in range(len(cd)):
            s += "real :: " + cd[i] + tempString % (inEquation.solvedCoefficients[i]) + "\n"
        s += "\n"
        s += "temp = 0.0\n\n"

        s += self.ConvertCppToFORTRAN90(cppSourceCode).replace('\t', '')

        s += '\n'
        s += "end function " + inEquation.extendedVersionHandler.AssembleSourceCodeName(inEquation) + "_model\n"
        return s



    ####################################################################################
    # spline code below this point
    ####################################################################################



    def SplineCodePYTHON_2D(self, inEquation):
        s  = '''# To the best of my knowledge this code is correct.
# If you find any errors or problems please contact
# me at zunzun@zunzun.com.
#      James
#
# the code below was partially based on the fortran code at:
# http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/splev.f
# http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "def " + inEquation.__class__.__name__ + "_evaluation(x_in):\n"
        s += '    t = ['
        for i in range(len(inEquation.scipySpline._eval_args[0])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[0][i])
            if i < (len(inEquation.scipySpline._eval_args[0]) - 1):
                s += ", "
        s += ']\n'
        s += '    coeff = ['
        for i in range(len(inEquation.scipySpline._eval_args[1])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[1][i])
            if i < (len(inEquation.scipySpline._eval_args[1]) - 1):
                s += ", "
        s += ']\n'
        s += '    n = ' + str(len(inEquation.scipySpline._eval_args[0])) + '\n'
        s += '    k = ' + str(inEquation.xOrder) + '\n'
        s += '''
    h = [0.0] * 25

    k1 = k+1
    l = k1
    l1 = l+1

    while x_in < t[l-1] and l1 != (k1+1):
        l1 = l
        l = l-1

    while x_in >= t[l1-1] and l != (n-k1):
        l = l1
        l1 += 1

    hh = [0.0] * 25

    h[0] = 1.0
    for j in range(1, k+1):
        for i in range(j):
            hh[i] = h[i]
        h[0] = 0.0
        for i in range(j):
            li = l+i
            lj = li-j
            if t[li] != t[lj]:
                f = hh[i] / (t[li] - t[lj])
                h[i] = h[i] + f * (t[li] - x_in)
                h[i+1] = f * (x_in - t[lj])
            else:
                h[i+1] = 0.0

    temp = 0.0
    ll = l - k1
    for j in range(k1):
        ll = ll + 1
        temp = temp + coeff[ll-1] * h[j]
        
    return temp
'''
        return s


    def SplineCodeCPP_2D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/splev.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "double " + inEquation.__class__.__name__ + "_evaluation(double x_in)\n"
        s += '{\n'
        s += '    double t [] = {'
        for i in range(len(inEquation.scipySpline._eval_args[0])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[0][i])
            if i < (len(inEquation.scipySpline._eval_args[0]) - 1):
                s += ", "
        s += '};\n'
        s += '    double coeff [] = {'
        for i in range(len(inEquation.scipySpline._eval_args[1])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[1][i])
            if i < (len(inEquation.scipySpline._eval_args[1]) - 1):
                s += ", "
        s += '};\n'
        s += '    int n = ' + str(len(inEquation.scipySpline._eval_args[0])) + ';\n'
        s += '    int k = ' + str(inEquation.xOrder) + ';\n'
        s += '''
    double h [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    double hh [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

    int i, j, li, lj, ll;
    double f, temp;
    
    int k1 = k+1;
    int l = k1;
    int l1 = l+1;

    while ((x_in < t[l-1]) && (l1 != (k1+1)))
    {
        l1 = l;
        l = l-1;
    }

    while ((x_in >= t[l1-1]) && (l != (n-k1)))
    {
        l = l1;
        l1 += 1;
    }

    h[0] = 1.0;
    for (j = 1; j < k+1; j++)
    {
        for (i = 0; i < j; i++)
        {
            hh[i] = h[i];
        }
        h[0] = 0.0;
        for (i = 0; i < j; i++)
        {
            li = l+i;
            lj = li-j;
            if (t[li] != t[lj])
            {
                f = hh[i] / (t[li] - t[lj]);
                h[i] = h[i] + f * (t[li] - x_in);
                h[i+1] = f * (x_in - t[lj]);
            }
            else
            {
                h[i+1] = 0.0;
            }
        }
    }

    temp = 0.0;
    ll = l - k1;
    for (j = 0; j < k1; j++)
    {
        ll = ll + 1;
        temp = temp + coeff[ll-1] * h[j];
    }
    
    return temp;
}
'''
        return s


    def SplineCodeJAVASCRIPT_3D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbisp.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "    function " + inEquation.__class__.__name__ + "_evaluation(x_in, y_in)\n"
        s += '    {\n'
        s += '        var tx = ['
        for i in range(len(inEquation.scipySpline.get_knots()[0])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[0][i])
            if i < (len(inEquation.scipySpline.get_knots()[0]) - 1):
                s += ", "
        s += '];\n'
        s += '        var ty = ['
        for i in range(len(inEquation.scipySpline.get_knots()[1])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[1][i])
            if i < (len(inEquation.scipySpline.get_knots()[1]) - 1):
                s += ", "
        s += '];\n'
        s += '        var coeff = ['
        for i in range(len(inEquation.scipySpline.get_coeffs())):
            s += "%-.16E" % (inEquation.scipySpline.get_coeffs()[i])
            if i < (len(inEquation.scipySpline.get_coeffs()) - 1):
                s += ", "
        s += '];\n'
        s += '        var nx = ' + str(len(inEquation.scipySpline.get_knots()[0])) + ';\n'
        s += '        var ny = ' + str(len(inEquation.scipySpline.get_knots()[1])) + ';\n'
        s += '        var kx = ' + str(inEquation.xOrder) + ';\n'
        s += '        var ky = ' + str(inEquation.yOrder) + ';\n'
        s += '''
        var h = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        var hh = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        var w_x = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        var w_y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];

        var i, j, li, lj, lx, ky1, nky1, ly, i1, j1, l2;
        var f, temp;

        var kx1 = kx+1;
        var nkx1 = nx-kx1;
        var l = kx1;
        var l1 = l+1;

        while ((x_in >= tx[l1-1]) && (l != nkx1))
        {
            l = l1;
            l1 = l+1;
        }
        
        h[0] = 1.0;
        for (j = 1; j < kx+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (tx[li] != tx[lj])
                {
                    f = hh[i] / (tx[li] - tx[lj]);
                    h[i] = h[i] + f * (tx[li] - x_in);
                    h[i+1] = f * (x_in - tx[lj]);
                }
                else
                {
                    h[i+1-1] = 0.0;
                }
            }
        }
        
        lx = l-kx1;
        for (j = 0; j < kx1; j++)
        {
            w_x[j] = h[j];
        }

        ky1 = ky+1;
        nky1 = ny-ky1;
        l = ky1;
        l1 = l+1;

        while ((y_in >= ty[l1-1]) && (l != nky1))
        {
            l = l1;
            l1 = l+1;
        }
        
        h[0] = 1.0;
        for (j = 1; j < ky+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (ty[li] != ty[lj])
                {
                    f = hh[i] / (ty[li] - ty[lj]);
                    h[i] = h[i] + f * (ty[li] - y_in);
                    h[i+1] = f * (y_in - ty[lj]);
                }
                else
                {
                    h[i+1-1] = 0.0;
                }
            }
        }

        ly = l-ky1;
        for (j = 0; j < ky1; j++)
        {
            w_y[j] = h[j];
        }

        l = lx*nky1;
        for (i1 = 0; i1 < kx1; i1++)
        {
            h[i1] = w_x[i1];
        }
            
        l1 = l+ly;
        temp = 0.0;
        for (i1 = 0; i1 < kx1; i1++)
        {
            l2 = l1;
            for (j1 = 0; j1 < ky1; j1++)
            {
                l2 = l2+1;
                temp = temp + coeff[l2-1] * h[i1] * w_y[j1];
            }
            l1 = l1+nky1;
        }
            
        return temp;
    }
'''
        return s


    def SplineCodeJAVA_2D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/splev.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "class " + inEquation.__class__.__name__ + "\n"
        s += '{\n'
        s += "    double " + inEquation.__class__.__name__ + "_evaluation(double x_in)\n"
        s += '    {\n'
        s += '        double t [] = {'
        for i in range(len(inEquation.scipySpline._eval_args[0])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[0][i])
            if i < (len(inEquation.scipySpline._eval_args[0]) - 1):
                s += ", "
        s += '};\n'
        s += '        double coeff [] = {'
        for i in range(len(inEquation.scipySpline._eval_args[1])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[1][i])
            if i < (len(inEquation.scipySpline._eval_args[1]) - 1):
                s += ", "
        s += '};\n'
        s += '        int n = ' + str(len(inEquation.scipySpline._eval_args[0])) + ';\n'
        s += '        int k = ' + str(inEquation.xOrder) + ';\n'
        s += '''
        double h [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double hh [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

        int i, j, li, lj, ll;
        double f, temp;
        
        int k1 = k+1;
        int l = k1;
        int l1 = l+1;

        while ((x_in < t[l-1]) && (l1 != (k1+1)))
        {
            l1 = l;
            l = l-1;
        }

        while ((x_in >= t[l1-1]) && (l != (n-k1)))
        {
            l = l1;
            l1 += 1;
        }

        h[0] = 1.0;
        for (j = 1; j < k+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (t[li] != t[lj])
                {
                    f = hh[i] / (t[li] - t[lj]);
                    h[i] = h[i] + f * (t[li] - x_in);
                    h[i+1] = f * (x_in - t[lj]);
                }
                else
                {
                    h[i+1] = 0.0;
                }
            }
        }

        temp = 0.0;
        ll = l - k1;
        for (j = 0; j < k1; j++)
        {
            ll = ll + 1;
            temp = temp + coeff[ll-1] * h[j];
        }
        
        return temp;
    }
}
'''
        return s


    def SplineCodeJAVASCRIPT_2D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/splev.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "    function " + inEquation.__class__.__name__ + "_evaluation(x_in)\n"
        s += '    {\n'
        s += '        var t = ['
        for i in range(len(inEquation.scipySpline._eval_args[0])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[0][i])
            if i < (len(inEquation.scipySpline._eval_args[0]) - 1):
                s += ", "
        s += '];\n'
        s += '        var coeff = ['
        for i in range(len(inEquation.scipySpline._eval_args[1])):
            s += "%-.16E" % (inEquation.scipySpline._eval_args[1][i])
            if i < (len(inEquation.scipySpline._eval_args[1]) - 1):
                s += ", "
        s += '];\n'
        s += '        var n = ' + str(len(inEquation.scipySpline._eval_args[0])) + ';\n'
        s += '        var k = ' + str(inEquation.xOrder) + ';\n'
        s += '''
        var h = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        var hh = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];

        var i, j, li, lj, ll;
        var f, temp;
        
        var k1 = k+1;
        var l = k1;
        var l1 = l+1;

        while ((x_in < t[l-1]) && (l1 != (k1+1)))
        {
            l1 = l;
            l = l-1;
        }

        while ((x_in >= t[l1-1]) && (l != (n-k1)))
        {
            l = l1;
            l1 += 1;
        }

        h[0] = 1.0;
        for (j = 1; j < k+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (t[li] != t[lj])
                {
                    f = hh[i] / (t[li] - t[lj]);
                    h[i] = h[i] + f * (t[li] - x_in);
                    h[i+1] = f * (x_in - t[lj]);
                }
                else
                {
                    h[i+1] = 0.0;
                }
            }
        }

        temp = 0.0;
        ll = l - k1;
        for (j = 0; j < k1; j++)
        {
            ll = ll + 1;
            temp = temp + coeff[ll-1] * h[j];
        }
        
        return temp;
    }
'''
        return s


    def SplineCodePYTHON_3D(self, inEquation):
        s  = '''# To the best of my knowledge this code is correct.
# If you find any errors or problems please contact
# me at zunzun@zunzun.com.
#      James
#
# the code below was partially based on the fortran code at:
# http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbisp.f
# http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "def " + inEquation.__class__.__name__ + "_model(x_in, y_in):\n"
        s += '    tx = ['
        for i in range(len(inEquation.scipySpline.get_knots()[0])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[0][i])
            if i < (len(inEquation.scipySpline.get_knots()[0]) - 1):
                s += ", "
        s += ']\n'
        s += '    ty = ['
        for i in range(len(inEquation.scipySpline.get_knots()[1])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[1][i])
            if i < (len(inEquation.scipySpline.get_knots()[1]) - 1):
                s += ", "
        s += ']\n'
        s += '    coeff = ['
        for i in range(len(inEquation.scipySpline.get_coeffs())):
            s += "%-.16E" % (inEquation.scipySpline.get_coeffs()[i])
            if i < (len(inEquation.scipySpline.get_coeffs()) - 1):
                s += ", "
        s += ']\n'
        s += '    nx = ' + str(len(inEquation.scipySpline.get_knots()[0])) + '\n'
        s += '    ny = ' + str(len(inEquation.scipySpline.get_knots()[1])) + '\n'
        s += '    kx = ' + str(inEquation.xOrder) + '\n'
        s += '    ky = ' + str(inEquation.yOrder) + '\n'
        s += '''
    h = [0.0] * 25
    hh = [0.0] * 25
    w_x = [0.0] * 25
    w_y = [0.0] * 25

    kx1 = kx+1
    nkx1 = nx-kx1
    l = kx1
    l1 = l+1

    while x_in >= tx[l1-1] and l != nkx1:
        l = l1
        l1 = l+1
        
    h[0] = 1.0
    for j in range(1, kx+1):
        for i in range(j):
            hh[i] = h[i]
        h[0] = 0.0
        for i in range(j):
            li = l+i
            lj = li-j
            if tx[li] != tx[lj]:
                f = hh[i] / (tx[li] - tx[lj])
                h[i] = h[i] + f * (tx[li] - x_in)
                h[i+1] = f * (x_in - tx[lj])
            else:
                h[i+1-1] = 0.0
                
    lx = l-kx1
    for j in range(kx1):
        w_x[j] = h[j]

    ky1 = ky+1
    nky1 = ny-ky1
    l = ky1
    l1 = l+1

    while y_in >= ty[l1-1] and l != nky1:
        l = l1
        l1 = l+1
        
    h[0] = 1.0
    for j in range(1, ky+1):
        for i in range(j):
            hh[i] = h[i]
        h[0] = 0.0
        for i in range(j):
            li = l+i
            lj = li-j
            if ty[li] != ty[lj]:
                f = hh[i] / (ty[li] - ty[lj])
                h[i] = h[i] + f * (ty[li] - y_in)
                h[i+1] = f * (y_in - ty[lj])
            else:
                h[i+1-1] = 0.0

    ly = l-ky1
    for j in range(ky1):
        w_y[j] = h[j]

    l = lx*nky1
    for i1 in range(kx1):
        h[i1] = w_x[i1]
        
    l1 = l+ly
    temp = 0.0
    for i1 in range(kx1):
        l2 = l1
        for j1 in range(ky1):
            l2 = l2+1
            temp = temp + coeff[l2-1] * h[i1] * w_y[j1]
        l1 = l1+nky1
        
    return temp
'''
        return s


    def SplineCodeCPP_3D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbisp.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "double " + inEquation.__class__.__name__ + "_evaluation(double x_in, double y_in)\n"
        s += '{\n'
        s += '    double tx [] = {'
        for i in range(len(inEquation.scipySpline.get_knots()[0])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[0][i])
            if i < (len(inEquation.scipySpline.get_knots()[0]) - 1):
                s += ", "
        s += '};\n'
        s += '    double ty [] = {'
        for i in range(len(inEquation.scipySpline.get_knots()[1])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[1][i])
            if i < (len(inEquation.scipySpline.get_knots()[1]) - 1):
                s += ", "
        s += '};\n'
        s += '    double coeff [] = {'
        for i in range(len(inEquation.scipySpline.get_coeffs())):
            s += "%-.16E" % (inEquation.scipySpline.get_coeffs()[i])
            if i < (len(inEquation.scipySpline.get_coeffs()) - 1):
                s += ", "
        s += '};\n'
        s += '    int nx = ' + str(len(inEquation.scipySpline.get_knots()[0])) + ';\n'
        s += '    int ny = ' + str(len(inEquation.scipySpline.get_knots()[1])) + ';\n'
        s += '    int kx = ' + str(inEquation.xOrder) + ';\n'
        s += '    int ky = ' + str(inEquation.yOrder) + ';\n'
        s += '''
    double h [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    double hh [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    double w_x [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    double w_y [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

    int i, j, li, lj, lx, ky1, nky1, ly, i1, j1, l2;
    double f, temp;

    int kx1 = kx+1;
    int nkx1 = nx-kx1;
    int l = kx1;
    int l1 = l+1;

    while ((x_in >= tx[l1-1]) && (l != nkx1))
    {
        l = l1;
        l1 = l+1;
    }
    
    h[0] = 1.0;
    for (j = 1; j < kx+1; j++)
    {
        for (i = 0; i < j; i++)
        {
            hh[i] = h[i];
        }
        h[0] = 0.0;
        for (i = 0; i < j; i++)
        {
            li = l+i;
            lj = li-j;
            if (tx[li] != tx[lj])
            {
                f = hh[i] / (tx[li] - tx[lj]);
                h[i] = h[i] + f * (tx[li] - x_in);
                h[i+1] = f * (x_in - tx[lj]);
            }
            else
            {
                h[i+1-1] = 0.0;
            }
        }
    }
    
    lx = l-kx1;
    for (j = 0; j < kx1; j++)
    {
        w_x[j] = h[j];
    }

    ky1 = ky+1;
    nky1 = ny-ky1;
    l = ky1;
    l1 = l+1;

    while ((y_in >= ty[l1-1]) && (l != nky1))
    {
        l = l1;
        l1 = l+1;
    }
    
    h[0] = 1.0;
    for (j = 1; j < ky+1; j++)
    {
        for (i = 0; i < j; i++)
        {
            hh[i] = h[i];
        }
        h[0] = 0.0;
        for (i = 0; i < j; i++)
        {
            li = l+i;
            lj = li-j;
            if (ty[li] != ty[lj])
            {
                f = hh[i] / (ty[li] - ty[lj]);
                h[i] = h[i] + f * (ty[li] - y_in);
                h[i+1] = f * (y_in - ty[lj]);
            }
            else
            {
                h[i+1-1] = 0.0;
            }
        }
    }

    ly = l-ky1;
    for (j = 0; j < ky1; j++)
    {
        w_y[j] = h[j];
    }

    l = lx*nky1;
    for (i1 = 0; i1 < kx1; i1++)
    {
        h[i1] = w_x[i1];
    }
        
    l1 = l+ly;
    temp = 0.0;
    for (i1 = 0; i1 < kx1; i1++)
    {
        l2 = l1;
        for (j1 = 0; j1 < ky1; j1++)
        {
            l2 = l2+1;
            temp = temp + coeff[l2-1] * h[i1] * w_y[j1];
        }
        l1 = l1+nky1;
    }
        
    return temp;
}
'''
        return s


    def SplineCodeJAVA_3D(self, inEquation):
        s  = '''// To the best of my knowledge this code is correct.
// If you find any errors or problems please contact
// me at zunzun@zunzun.com.
//      James
//
// the code below was partially based on the fortran code at:
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbisp.f
// http://svn.scipy.org/svn/scipy/trunk/scipy/interpolate/fitpack/fpbspl.f

'''
        s += "class " + inEquation.__class__.__name__ + "\n"
        s += '{\n'
        s += "    double " + inEquation.__class__.__name__ + "_evaluation(double x_in, double y_in)\n"
        s += '    {\n'
        s += '        double tx [] = {'
        for i in range(len(inEquation.scipySpline.get_knots()[0])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[0][i])
            if i < (len(inEquation.scipySpline.get_knots()[0]) - 1):
                s += ", "
        s += '};\n'
        s += '        double ty [] = {'
        for i in range(len(inEquation.scipySpline.get_knots()[1])):
            s += "%-.16E" % (inEquation.scipySpline.get_knots()[1][i])
            if i < (len(inEquation.scipySpline.get_knots()[1]) - 1):
                s += ", "
        s += '};\n'
        s += '        double coeff [] = {'
        for i in range(len(inEquation.scipySpline.get_coeffs())):
            s += "%-.16E" % (inEquation.scipySpline.get_coeffs()[i])
            if i < (len(inEquation.scipySpline.get_coeffs()) - 1):
                s += ", "
        s += '};\n'
        s += '        int nx = ' + str(len(inEquation.scipySpline.get_knots()[0])) + ';\n'
        s += '        int ny = ' + str(len(inEquation.scipySpline.get_knots()[1])) + ';\n'
        s += '        int kx = ' + str(inEquation.xOrder) + ';\n'
        s += '        int ky = ' + str(inEquation.yOrder) + ';\n'
        s += '''
        double h [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double hh [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double w_x [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double w_y [] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

        int i, j, li, lj, lx, ky1, nky1, ly, i1, j1, l2;
        double f, temp;

        int kx1 = kx+1;
        int nkx1 = nx-kx1;
        int l = kx1;
        int l1 = l+1;

        while ((x_in >= tx[l1-1]) && (l != nkx1))
        {
            l = l1;
            l1 = l+1;
        }
        
        h[0] = 1.0;
        for (j = 1; j < kx+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (tx[li] != tx[lj])
                {
                    f = hh[i] / (tx[li] - tx[lj]);
                    h[i] = h[i] + f * (tx[li] - x_in);
                    h[i+1] = f * (x_in - tx[lj]);
                }
                else
                {
                    h[i+1-1] = 0.0;
                }
            }
        }
        
        lx = l-kx1;
        for (j = 0; j < kx1; j++)
        {
            w_x[j] = h[j];
        }

        ky1 = ky+1;
        nky1 = ny-ky1;
        l = ky1;
        l1 = l+1;

        while ((y_in >= ty[l1-1]) && (l != nky1))
        {
            l = l1;
            l1 = l+1;
        }
        
        h[0] = 1.0;
        for (j = 1; j < ky+1; j++)
        {
            for (i = 0; i < j; i++)
            {
                hh[i] = h[i];
            }
            h[0] = 0.0;
            for (i = 0; i < j; i++)
            {
                li = l+i;
                lj = li-j;
                if (ty[li] != ty[lj])
                {
                    f = hh[i] / (ty[li] - ty[lj]);
                    h[i] = h[i] + f * (ty[li] - y_in);
                    h[i+1] = f * (y_in - ty[lj]);
                }
                else
                {
                    h[i+1-1] = 0.0;
                }
            }
        }

        ly = l-ky1;
        for (j = 0; j < ky1; j++)
        {
            w_y[j] = h[j];
        }

        l = lx*nky1;
        for (i1 = 0; i1 < kx1; i1++)
        {
            h[i1] = w_x[i1];
        }
            
        l1 = l+ly;
        temp = 0.0;
        for (i1 = 0; i1 < kx1; i1++)
        {
            l2 = l1;
            for (j1 = 0; j1 < ky1; j1++)
            {
                l2 = l2+1;
                temp = temp + coeff[l2-1] * h[i1] * w_y[j1];
            }
            l1 = l1+nky1;
        }
            
        return temp;
    }
}
'''
        return s
