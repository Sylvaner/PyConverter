#!/usr/bin/env python3
"""
Test actions modules.
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

class ActionsTest(unittest.TestCase):
################################################################################
# Tests concat action                                                          #
################################################################################
    def test_concat_with_separator(self):
        from actions.concat import concat
        self.assertEqual('A B C', concat.action('PLOUF', {'col_list': [1, 2, 3], 'separator': ' '}, ['A', 'B', 'C', 'D'], 0))
        self.assertEqual('D;G;E', concat.action('PLOUF', {'col_list': [1, 4, 2], 'separator': ';'}, ['D', 'E', 'F', 'G'], 0))
        self.assertEqual('ZoXz', concat.action('PLOUF', {'col_list': [1, 2], 'separator': ''}, ['Zo', 'Xz', 'Yf', 'Wb'], 0))
    
    def test_concat_without_separator(self):
        from actions.concat import concat
        self.assertEqual('ABC', concat.action('PLOUF', {'col_list': [1, 2, 3]}, ['A', 'B', 'C', 'D'], 0))
        self.assertEqual('DGE', concat.action('PLOUF', {'col_list': [1, 4, 2]}, ['D', 'E', 'F', 'G'], 0))
    
################################################################################
# Tests date_format action                                                     #
################################################################################
    def test_date_format(self):
        from actions.date_format import date_format
        self.assertEqual('01/12/1999', date_format.action('1999/12/01', {'input': '%Y/%m/%d', 'output': '%d/%m/%Y'}, 0, 0))
        self.assertEqual('01/12/1999', date_format.action('1999-12-01', {'input': '%Y-%m-%d', 'output': '%d/%m/%Y'}, 0, 0))
    
    def test_first_char_sentence(self):
        from actions.date_format import date_format
        self.assertEqual('Hello', date_format.action('Hello', {'input': '%Y/%m/%d', 'output': '%d/%m/%Y'}, 0, 0))
    
    def test_first_char_only_space(self):
        from actions.date_format import date_format
        self.assertEqual('     ', date_format.action('     ', {'input': '%Y/%m/%d', 'output': '%d/%m/%Y'}, 0, 0))
    
    def test_first_char_empty_string(self):
        from actions.date_format import date_format
        self.assertEqual('', date_format.action('', {'input': '%Y/%m/%d', 'output': '%d/%m/%Y'}, 0, 0))
    
    def test_first_char_not_a_string(self):
        from actions.date_format import date_format
        self.assertEqual(['Hello', 'the', 'world'], date_format.action(['Hello', 'the', 'world'], {'input': '%Y/%m/%d', 'output': '%d/%m/%Y'}, 0, 0))
    
    def test_first_char_no_params(self):
        from actions.date_format import date_format
        self.assertEqual('1999/12/01', date_format.action('1999/12/01', None, 0, 0))
    
################################################################################
# Tests replace action                                                         #
################################################################################
    def test_replace(self):
        from actions.replace import replace
        self.assertEqual('Hello X Test', replace.action('Hello The World', {'The': 'X', 'World': 'Test'}, 0, 0))
        self.assertEqual('Hell0 The W0rld', replace.action('Hello The World', {'o': '0'}, 0, 0))
    
    def test_replace_only_space(self):
        from actions.replace import replace
        self.assertEqual('     ', replace.action('     ', {'Yes': 'No'}, 0, 0))
    
    def test_replace_empty_string(self):
        from actions.replace import replace
        self.assertEqual('', replace.action('', {'Yes': 'No'}, 0, 0))
    
    def test_replace_not_a_string(self):
        from actions.replace import replace
        self.assertEqual(['Hello', 'the', 'world'], replace.action(['Hello', 'the', 'world'], {'Yes': 'No'}, 0, 0))
    
    def test_replace_no_params(self):
        from actions.replace import replace
        self.assertEqual('1999/12/01', replace.action('1999/12/01', None, 0, 0))
    
################################################################################
# Tests set_row_index action                                                   #
################################################################################
    def test_set_row_index(self):
        from actions.set_row_index import set_row_index
        self.assertEqual(1, set_row_index.action('Hello The World', None, None, 1))
        self.assertEqual(2, set_row_index.action('Hello The World', {'Somthing': 'Thing'}, None, 2))
    
    def test_set_row_index_with_start_index(self):
        from actions.set_row_index import set_row_index
        self.assertEqual(3, set_row_index.action('Hello The World', 2, None, 1))
    
################################################################################
# Tests set_value action                                                       #
################################################################################
    def test_set_value(self):
        from actions.set_value import set_value
        self.assertEqual('Test', set_value.action('Hello The World', 'Test', 0, 0))
    
    def test_set_value_bad_params(self):
        from actions.set_value import set_value
        self.assertEqual('Hello The World', set_value.action('Hello The World', ['Test'], 0, 0))
    
################################################################################
# Tests slice action                                                           #
################################################################################
    def test_slice_start(self):
        from actions.slice import slice
        self.assertEqual('lo The World', slice.action('Hello The World', {'start': 3}, 0, 0))
    
    def test_slice_end(self):
        from actions.slice import slice
        self.assertEqual('Hel', slice.action('Hello The World', {'end': 3}, 0, 0))
        self.assertEqual('Hello The Wo', slice.action('Hello The World', {'end': -3}, 0, 0))
    
    def test_slice_start_end(self):
        from actions.slice import slice
        self.assertEqual('lo The Wo', slice.action('Hello The World', {'start': 3, 'end': -3}, 0, 0))
    
    def test_slice_bad_params(self):
        from actions.slice import slice
        self.assertEqual('Hello The World', slice.action('Hello The World', {'Test'}, 0, 0))
        self.assertEqual('Hello The World', slice.action('Hello The World', 'Test', 0, 0))
    
if __name__ == '__main__':
    unittest.main()
