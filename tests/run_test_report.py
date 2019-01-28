import xmlrunner
import unittest

if __name__ == "__main__":
    import os
    testsFolder = os.path.dirname(os.path.realpath(__file__))
    packageFolder = os.path.abspath(os.path.join(testsFolder, os.pardir))

    import sys
    sys.path.insert(0, packageFolder)

    ## Create test suite
    suite = unittest.TestSuite()

    ## Add All test cases
    all_test_cases = unittest.defaultTestLoader.discover(testsFolder, 'test_*.py')
    for test_case in all_test_cases:
        suite.addTest(test_case)

    ## Run tests
    runner = xmlrunner.XMLTestRunner(output=os.path.join(packageFolder, 'report'))
    runner.run(suite)
