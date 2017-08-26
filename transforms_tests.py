#!/usr/bin/env python3
"""
Test transforms modules.
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

class TransformsTest(unittest.TestCase):
################################################################################
# Tests first_char transform                                                   #
################################################################################
    def test_first_char_word(self):
        from transforms.first_char import first_char
        self.assertEqual('H', first_char.transform('Hello'))
    
    def test_first_char_sentence(self):
        from transforms.first_char import first_char
        self.assertEqual('H', first_char.transform('Hello the world!!!'))
    
    def test_first_char_only_space(self):
        from transforms.first_char import first_char
        self.assertEqual(' ', first_char.transform('          '))
    
    def test_first_char_empty_string(self):
        from transforms.first_char import first_char
        self.assertEqual('', first_char.transform(''))
    
    def test_first_char_not_a_string(self):
        from transforms.first_char import first_char
        self.assertIsInstance(first_char.transform(['Hello', 'the', 'world']), list)
    
################################################################################
# Tests first_word transform                                                   #
################################################################################
    def test_first_word_one_word(self):
        from transforms.first_word import first_word
        self.assertEqual('Hello', first_word.transform('Hello'))
    
    def test_first_word_sentence(self):
        from transforms.first_word import first_word
        self.assertEqual('Hello', first_word.transform('Hello the world!!!'))
    
    def test_first_word_multiple_spaces(self):
        from transforms.first_word import first_word
        self.assertEqual('Hello', first_word.transform('Hello  the  world!!!'))
    
    def test_first_word_only_spaces(self):
        from transforms.first_word import first_word
        self.assertEqual('', first_word.transform('     '))
    
    def test_first_word_empty_string(self):
        from transforms.first_word import first_word
        self.assertEqual('', first_word.transform(''))
    
    def test_first_word_not_a_string(self):
        from transforms.first_word import first_word
        self.assertIsInstance(first_word.transform(['Hello', 'the', 'world']), list)
    
################################################################################
# Tests last_word transform                                                   #
################################################################################
    def test_last_word_one_word(self):
        from transforms.last_word import last_word
        self.assertEqual('Hello', last_word.transform('Hello'))
    
    def test_last_word_sentence(self):
        from transforms.last_word import last_word
        self.assertEqual('world', last_word.transform('Hello the world'))
    
    def test_last_word_sentence_with_ponctuation(self):
        from transforms.last_word import last_word
        self.assertEqual('world', last_word.transform('Hello the world!!!'))
        self.assertEqual('world', last_word.transform('Hello the world!'))
        self.assertEqual('world', last_word.transform('Hello the world !'))
        self.assertEqual('world', last_word.transform('Hello the world ?'))
        self.assertEqual('world', last_word.transform('Hello the world.'))
        self.assertEqual('world', last_word.transform('Hello the world,'))
        self.assertEqual('world', last_word.transform('Hello the world, ?'))
    
    def test_last_word_multiple_spaces(self):
        from transforms.last_word import last_word
        self.assertEqual('world', last_word.transform('Hello  the  world'))
    
    def test_last_word_only_spaces(self):
        from transforms.last_word import last_word
        self.assertEqual('', last_word.transform('     '))
    
    def test_last_word_empty_string(self):
        from transforms.last_word import last_word
        self.assertEqual('', last_word.transform(''))
    
    def test_last_word_not_a_string(self):
        from transforms.last_word import last_word
        self.assertIsInstance(last_word.transform(['Hello', 'the', 'world']), list)
    
################################################################################
# Tests remove_digits transform                                                #
################################################################################
    def test_remove_digits(self):
        from transforms.remove_digits import remove_digits
        self.assertEqual('Hell te wrd', remove_digits.transform('Hell0 t4e w0r1d'))
        self.assertEqual('efa', remove_digits.transform('23e99f00a'))
        self.assertEqual('', remove_digits.transform('329840912'))
    
    def test_remove_digits_without_digits(self):
        from transforms.remove_digits import remove_digits
        self.assertEqual('Hello the world', remove_digits.transform('Hello the world'))
    
    def test_remove_digits_only_spaces(self):
        from transforms.remove_digits import remove_digits
        self.assertEqual('     ', remove_digits.transform('     '))
    
    def test_remove_digits_empty_string(self):
        from transforms.remove_digits import remove_digits
        self.assertEqual('', remove_digits.transform(''))
    
    def test_remove_digits_not_a_string(self):
        from transforms.remove_digits import remove_digits
        self.assertIsInstance(remove_digits.transform(['Hello', 'the', 'world']), list)
    
################################################################################
# Tests remove_last_word transform                                             #
################################################################################
    def test_remove_last_word(self):
        from transforms.remove_last_word import remove_last_word
        self.assertEqual('Hello the', remove_last_word.transform('Hello the world'))

    def test_remove_last_word_one_word(self):
        from transforms.remove_last_word import remove_last_word
        self.assertEqual('', remove_last_word.transform('Hello'))

    def test_remove_last_word_with_extra_space(self):
        from transforms.remove_last_word import remove_last_word
        self.assertEqual('Hello the', remove_last_word.transform('Hello the world '))
        self.assertEqual('', remove_last_word.transform('Hello '))

    def test_remove_last_word_only_spaces(self):
        from transforms.remove_last_word import remove_last_word
        self.assertEqual('', remove_last_word.transform('     '))

    def test_remove_last_word_empty_string(self):
        from transforms.remove_last_word import remove_last_word
        self.assertEqual('', remove_last_word.transform(''))
    
    def test_remove_last_word_not_a_string(self):
        from transforms.remove_last_word import remove_last_word
        self.assertIsInstance(remove_last_word.transform(['Hello', 'the', 'world']), list)
    
################################################################################
# Tests to_lower transform                                                     #
################################################################################
    def test_to_lower(self):
        from transforms.to_lower import to_lower
        self.assertEqual('hello the world', to_lower.transform('Hello the World'))

    def test_to_lower_one_word(self):
        from transforms.to_lower import to_lower
        self.assertEqual('hello', to_lower.transform('Hello'))

    def test_to_lower_already_done(self):
        from transforms.to_lower import to_lower
        self.assertEqual('hello the world', to_lower.transform('hello the world'))

    def test_to_lower_only_spaces(self):
        from transforms.to_lower import to_lower
        self.assertEqual('     ', to_lower.transform('     '))

    def test_to_lower_empty_string(self):
        from transforms.to_lower import to_lower
        self.assertEqual('', to_lower.transform(''))
    
    def test_to_lower_not_a_string(self):
        from transforms.to_lower import to_lower
        self.assertIsInstance(to_lower.transform(['Hello', 'the', 'world']), list)

################################################################################
# Tests to_upper transform                                                     #
################################################################################
    def test_to_upper(self):
        from transforms.to_upper import to_upper
        self.assertEqual('HELLO THE WORLD', to_upper.transform('Hello the World'))

    def test_to_upper_one_word(self):
        from transforms.to_upper import to_upper
        self.assertEqual('HELLO', to_upper.transform('Hello'))

    def test_to_upper_already_done(self):
        from transforms.to_upper import to_upper
        self.assertEqual('HELLO THE WORLD', to_upper.transform('HELLO THE WORLD'))

    def test_to_upper_only_spaces(self):
        from transforms.to_upper import to_upper
        self.assertEqual('     ', to_upper.transform('     '))

    def test_to_upper_empty_string(self):
        from transforms.to_upper import to_upper
        self.assertEqual('', to_upper.transform(''))
    
    def test_to_upper_not_a_string(self):
        from transforms.to_upper import to_upper
        self.assertIsInstance(to_upper.transform(['Hello', 'the', 'world']), list)

################################################################################
# Tests trim transform                                                         #
################################################################################
    def test_trim(self):
        from transforms.trim import trim
        self.assertEqual('Hello the World', trim.transform('    Hello the World   '))

    def test_trim_one_word(self):
        from transforms.trim import trim
        self.assertEqual('Hello', trim.transform(' Hello  '))

    def test_trim_already_done(self):
        from transforms.trim import trim
        self.assertEqual('hello the world', trim.transform('hello the world'))

    def test_trim_only_spaces(self):
        from transforms.trim import trim
        self.assertEqual('', trim.transform('     '))

    def test_trim_empty_string(self):
        from transforms.trim import trim
        self.assertEqual('', trim.transform(''))
    
    def test_trim_not_a_string(self):
        from transforms.trim import trim
        self.assertIsInstance(trim.transform(['Hello', 'the', 'world']), list)

################################################################################
# Tests up_all_first_letters transform                                         #
################################################################################
    def test_up_all_first_letters(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertEqual('Hello The World', up_all_first_letters.transform('hello the world'))
        self.assertEqual('Hello The World', up_all_first_letters.transform('Hello the world'))
    
    def test_up_all_first_letters_one_word(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertEqual('Hello', up_all_first_letters.transform('hello'))

    def test_up_all_first_letters_already_done(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertEqual('Hello The World', up_all_first_letters.transform('Hello The World'))

    def test_up_all_first_letters_only_spaces(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertEqual('     ', up_all_first_letters.transform('     '))

    def test_up_all_first_letters_empty_string(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertEqual('', up_all_first_letters.transform(''))
    
    def test_up_all_first_letters_not_a_string(self):
        from transforms.up_all_first_letters import up_all_first_letters
        self.assertIsInstance(up_all_first_letters.transform(['Hello', 'the', 'world']), list)

################################################################################
# Tests up_first_letter transform                                              #
################################################################################
    def test_up_first_letter(self):
        from transforms.up_first_letter import up_first_letter
        self.assertEqual('Hello the world', up_first_letter.transform('hello the world'))
        self.assertEqual('Hello the world', up_first_letter.transform('Hello the world'))
    
    def test_up_first_letter_one_word(self):
        from transforms.up_first_letter import up_first_letter
        self.assertEqual('Hello', up_first_letter.transform('hello'))

    def test_up_first_letter_already_done(self):
        from transforms.up_first_letter import up_first_letter
        self.assertEqual('Hello the world', up_first_letter.transform('hello the world'))

    def test_up_first_letter_only_spaces(self):
        from transforms.up_first_letter import up_first_letter
        self.assertEqual('     ', up_first_letter.transform('     '))

    def test_up_first_letter_empty_string(self):
        from transforms.up_first_letter import up_first_letter
        self.assertEqual('', up_first_letter.transform(''))
    
    def test_up_first_letter_not_a_string(self):
        from transforms.up_first_letter import up_first_letter
        self.assertIsInstance(up_first_letter.transform(['Hello', 'the', 'world']), list)

if __name__ == '__main__':
    unittest.main()
