import xmlrunner
import unittest

import os

import sys
sys.path.insert(0, '.')

if __name__ == "__main__":
    ## Create test suite
    suite = unittest.TestSuite()

    ## Add All test cases
    folder = os.path.dirname(os.path.realpath(__file__))
    all_test_cases = unittest.defaultTestLoader.discover(folder, 'test_*.py')
    for test_case in all_test_cases:
        suite.addTest(test_case)

    ## Run tests
    runner = xmlrunner.XMLTestRunner(output='report')
    runner.run(suite)
