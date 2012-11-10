from __future__ import print_function # prepare for conversion to Python 3
from __future__ import unicode_literals # prepare for conversion to Python 3
from __future__ import absolute_import # prepare for conversion to Python 3

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

from . import DataCache
from . import Services
from . import ExtendedVersionHandlers
from . import IModel
from . import Models_2D
from . import Models_3D

dataConvertorService = Services.DataConverterService.DataConverterService
solverService = Services.SolverService.SolverService
outputSourceCodeService = Services.OutputSourceCodeService.OutputSourceCodeService
dataCache = DataCache.DataCache.DataCache