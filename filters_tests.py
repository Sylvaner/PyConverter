#!/usr/bin/env python3
"""
Test filters modules.
"""
__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

import os
import sys
import unittest

class FiltersTest(unittest.TestCase):
################################################################################
# Tests is_empty filter                                                        #
################################################################################
    def test_is_empty(self):
        from filters.is_empty import is_empty
        self.assertEqual(True, is_empty.test_filter(1, ['', 'Test'], 0))
        self.assertEqual(True, is_empty.test_filter(2, ['Test', '', 'Coucou'], 0))
    
    def test_is_empty_false(self):
        from filters.is_empty import is_empty
        self.assertEqual(False, is_empty.test_filter(2, ['', 'Test'], 0))
        self.assertEqual(False, is_empty.test_filter(1, ['Test', '', 'Coucou'], 0))
    
################################################################################
# Tests is_value filter                                                     #
################################################################################
    def test_is_value(self):
        from filters.is_value import is_value
        self.assertEqual(True, is_value.test_filter({'Test': '2'}, ['', 'Test'], 0))
        self.assertEqual(True, is_value.test_filter({'Coucou': '3'}, ['Test', '', 'Coucou'], 0))
    
    def test_is_value_false(self):
        from filters.is_value import is_value
        self.assertEqual(False, is_value.test_filter({'Test': '1'}, ['', 'Test'], 0))
        self.assertEqual(False, is_value.test_filter({'Coucou': '1'}, ['Test', '', 'Coucou'], 0))
        self.assertEqual(False, is_value.test_filter({'Coucou': '2}, ['Test', '', 'Coucou'], 0))
    

if __name__ == '__main__':
    unittest.main()
