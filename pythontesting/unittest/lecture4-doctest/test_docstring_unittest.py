import shape_area_docstring_placement as shape_area

import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shape_area))
    return tests

# to run execute: pyhton -m unittest test_docstring_unittest.py -v