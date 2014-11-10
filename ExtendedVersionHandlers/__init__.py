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

from . import ExtendedVersionHandler_Default
from . import ExtendedVersionHandler_Offset
from . import ExtendedVersionHandler_Reciprocal
from . import ExtendedVersionHandler_ReciprocalWithOffset
from . import ExtendedVersionHandler_Inverse
from . import ExtendedVersionHandler_InverseWithOffset
from . import ExtendedVersionHandler_LinearDecay
from . import ExtendedVersionHandler_LinearDecayAndOffset
from . import ExtendedVersionHandler_LinearGrowth
from . import ExtendedVersionHandler_LinearGrowthAndOffset
from . import ExtendedVersionHandler_ExponentialGrowth
from . import ExtendedVersionHandler_ExponentialGrowthAndOffset
from . import ExtendedVersionHandler_ExponentialDecay
from . import ExtendedVersionHandler_ExponentialDecayAndOffset

extendedVersionHandlerNameList = []
for i in dir():
    splitted = i.split('_')
    if splitted[0] == 'ExtendedVersionHandler':
        extendedVersionHandlerNameList.append(splitted[1])

