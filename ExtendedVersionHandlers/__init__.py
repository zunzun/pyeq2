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

import ExtendedVersionHandler_Default
import ExtendedVersionHandler_Offset
import ExtendedVersionHandler_Reciprocal
import ExtendedVersionHandler_ReciprocalWithOffset
import ExtendedVersionHandler_Inverse
import ExtendedVersionHandler_InverseWithOffset
import ExtendedVersionHandler_LinearDecay
import ExtendedVersionHandler_LinearDecayAndOffset
import ExtendedVersionHandler_LinearGrowth
import ExtendedVersionHandler_LinearGrowthAndOffset
import ExtendedVersionHandler_ExponentialGrowth
import ExtendedVersionHandler_ExponentialGrowthAndOffset
import ExtendedVersionHandler_ExponentialDecay
import ExtendedVersionHandler_ExponentialDecayAndOffset

extendedVersionHandlerNameList = []
for i in dir():
    splitted = i.split('_')
    if splitted[0] == 'ExtendedVersionHandler':
        extendedVersionHandlerNameList.append(splitted[1])

