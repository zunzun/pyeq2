#    Version info: $Id$

import unittest
import Test_IndividualPolyFunctions
import Test_OutputSourceCodeService
import Test_DataConverterService
import Test_DataCache
import Test_SolverService
import Test_CalculateCoefficientAndFitStatistics
import Test_ModelSolveMethods
import Test_ExtendedVersionHandlers
import Test_Equations


# see http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml#loaders-runners-and-all-that-stuff

loader = unittest.TestLoader()

suite =        loader.loadTestsFromModule(Test_CalculateCoefficientAndFitStatistics)
suite.addTests(loader.loadTestsFromModule(Test_DataCache))
suite.addTests(loader.loadTestsFromModule(Test_DataConverterService))
suite.addTests(loader.loadTestsFromModule(Test_ExtendedVersionHandlers))
suite.addTests(loader.loadTestsFromModule(Test_IndividualPolyFunctions))
suite.addTests(loader.loadTestsFromModule(Test_ModelSolveMethods))
suite.addTests(loader.loadTestsFromModule(Test_OutputSourceCodeService))
suite.addTests(loader.loadTestsFromModule(Test_SolverService))
suite.addTests(loader.loadTestsFromModule(Test_Equations))

runner = unittest.TextTestRunner(verbosity=2)

result = runner.run(suite)
