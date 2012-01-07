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

import sys
import numpy
numpy.seterr(over = 'raise', divide = 'raise', invalid = 'raise', under = 'ignore') # numpy raises warnings, convert to exceptions to trap them



def Ones(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    return numpy.ones_like(data[0])
   

def X(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    return data[0]


def NegX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    return -1.0 * data[0]


def RecipX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = 1.0 / data[0]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    return data[1]

   
def NegY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    return -1.0 * data[1]


def RecipY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = 1.0 / data[1]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def SinX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.sin(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Pow2SinX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.power(numpy.sin(data[0]), 2.0)
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def TanX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.tan(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CoshX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.cosh(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Log10X(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log10(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue = numpy.power(data[0], args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowLogX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue = numpy.power(numpy.log(data[0]), args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowExpX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue =  numpy.power(numpy.exp(data[0]), args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Polyfunctional2D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args)
    try:
        returnValue = eqInstance.polyfunctionalEquationList[args].value(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Rational2D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args)
    try:
        returnValue = eqInstance.rationalEquationList[args].value(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def TwoPiX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = 2.0 * numpy.pi * data[0]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def NistEnsoCosX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue =  numpy.cos(2.0 * numpy.pi * data[0] / 12.0)
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def NistEnsoSinX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.sin(2.0 * numpy.pi * data[0] / 12.0)
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def ExpX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.exp(data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def ExpXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.exp(data[0] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def XSQMINUSYSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = (data[0] * data[0]) - (data[1] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def YSQMINUSXSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = (data[1] * data[1]) - (data[0] * data[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def XSQPLUSYSQ(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = (data[0] * data[0]) + (data[1] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.exp(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Polyfunctional3D(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args)
    try:
        returnValue = eqInstance.polyfunctionalEquationList[args[0]].value(data[0]) * eqInstance.polyfunctionalEquationList[args[1]].value(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue = numpy.power(numpy.log(data[1]), args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue = numpy.power(numpy.exp(data[1]), args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowX_PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0]) + str(args[1])
    try:
        returnValue = numpy.power(data[0], args[0]) * numpy.power(data[1], args[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowLogX_PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0]) + str(args[1])
    try:
        returnValue = numpy.power(numpy.log(data[0]), args[0]) * numpy.power(numpy.log(data[1]), args[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowExpX_PowExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0]) + str(args[1])
    try:
        returnValue = numpy.power(numpy.exp(data[0]), args[0]) * numpy.power(numpy.exp(data[1]), args[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowX_PowLogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0]) + str(args[1])
    try:
        returnValue = numpy.power(data[0], args[0]) * numpy.power(numpy.log(data[1]), args[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowLogX_PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0]) + str(args[1])
    try:
        returnValue = numpy.power(numpy.log(data[0]), args[0]) * numpy.power(data[1], args[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def PowY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(args[0])
    try:
        returnValue = numpy.power(data[1], args[0])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def Log10Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log10(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[0] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def SinXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.sin(data[0] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def TanXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.tan(data[0] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CoshXY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.cosh(data[0] * data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CoshY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.cosh(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def CoshXCoshY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.cosh(data[0]) * numpy.cosh(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def TanY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.tan(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def TanXTanY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.tan(data[0]) * numpy.tan(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def SinY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.sin(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def SinXSinY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.sin(data[0]) * numpy.sin(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def XY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = data[0] * data[1]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def XOVERY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = data[0] / data[1]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def XPLUSY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = data[0] + data[1]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogX_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[0]) * numpy.log(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def ExpX_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.exp(data[0]) * numpy.log(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogX_ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[0]) * numpy.exp(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def ExpX_ExpY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.exp(data[0]) * numpy.exp(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def X_LogY(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = data[0] * numpy.log(data[1])
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LogX_Y(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name
    try:
        returnValue = numpy.log(data[0]) * data[1]
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


# see http://en.wikipedia.org/wiki/Legendre_polynomials
def LegendreX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
    cosineFlag = args[1]
   
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(n)
           
    try:
        if cosineFlag == 1: # convert degrees to radians
            data = numpy.cos(numpy.radians(data[0]))
        elif cosineFlag == 2: # already in radians
            data = numpy.cos(data[0])
        else: # no cosine
            data = data[0]

        if n == 0:
            returnValue = numpy.ones_like(data)
        elif n == 1:
            returnValue = data
        elif n == 2:
            returnValue = (1.0 / 2.0) * (3.0*numpy.power(data, 2.0) - 1.0)
        elif n == 3:
            returnValue = (1.0 / 2.0) * (5.0*numpy.power(data, 3.0) - 3.0*data)
        elif n == 4:
            returnValue = (1.0 / 8.0) * (35.0*numpy.power(data, 4.0) - 30.0*numpy.power(data, 2.0) + 3.0)
        elif n == 5:
            returnValue = (1.0 / 8.0) * (63.0*numpy.power(data, 5.0) - 70.0*numpy.power(data, 3.0) + 15.0*data)
        elif n == 6:
            returnValue = (1.0 / 16.0) * (231.0*numpy.power(data, 6.0) - 315.0*numpy.power(data, 4.0) + 105.0*numpy.power(data, 2.0) - 5.0)
        elif n == 7:
            returnValue = (1.0 / 16.0) * (429.0*numpy.power(data, 7.0) - 693.0*numpy.power(data, 5.0) + 315.0*numpy.power(data, 3.0) - 35.0*data)
        elif n == 8:
            returnValue = (1.0 / 128.0) * (6435.0*numpy.power(data, 8.0) - 12012.0*numpy.power(data, 6.0) + 6930.0*numpy.power(data, 4.0) - 1260.0*numpy.power(data, 2.0) + 35.0)
        elif n == 9:
            returnValue = (1.0 / 128.0) * (12155.0*numpy.power(data, 9.0) - 25740.0*numpy.power(data, 7.0) + 18018.0*numpy.power(data, 5.0) - 4620.0*numpy.power(data, 3.0) + 315.0*data)
        elif n == 10:
            returnValue = (1.0 / 256.0) * (46189.0*numpy.power(data, 10.0) - 109395.0*numpy.power(data, 8.0) + 90090.0*numpy.power(data, 6.0) - 30030.0*numpy.power(data, 4.0) + 3465.0*numpy.power(data, 2.0) - 63.0)
        else:
            raise Exception("Legendre Polynomial Degree of " + str(n) + " is too high, please use a degree of 10 or less.") # will be trapped
           
        if numpy.alltrue(numpy.isfinite(returnValue)):
            return returnValue
        return 1.0E300 * numpy.ones_like(data[0])
    except:
        return 1.0E300 * numpy.ones_like(data[0])


def LegendreCosineDegreesX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
   
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(n)
    else:
        return LegendreX(data=data, args = [n, 1], eqInstance=eqInstance, NameOrValueFlag=NameOrValueFlag)


def LegendreCosineRadiansX(data=None, args=None, eqInstance=None, NameOrValueFlag=0):
    n = args[0]
   
    if NameOrValueFlag: # name used by cache, must be distinct
        return sys._getframe().f_code.co_name + '_' + str(n)
    else:
        return LegendreX(data=data, args = [n, 2], eqInstance=eqInstance, NameOrValueFlag=NameOrValueFlag)
