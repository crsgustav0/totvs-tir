import unittest

from MATA030.MATA030TESTCASE import MATA030

suite = unittest.TestSuite()

suite.addTest(MATA030('test_MATA030_CT133'))
suite.addTest(MATA030('test_MATA030_CT133_1'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)