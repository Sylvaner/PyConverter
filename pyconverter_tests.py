#!/usr/bin/env python3
"""
Test pyconverter.Convert class.
"""
__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

import os
import sys
import json
import unittest
import xlrd
import openpyxl
import csv
from odf.table import TableRow, TableCell
from odf.opendocument import load as odf_load
from odf.text import P
from pyconverter import Convert

class ConvertTest(unittest.TestCase):
    # Base tests data
    TESTS_DATA = [
            ['Activated', 'Money', 'Name', 'Birthdate'],
            ['Yes', '24', 'Marc ASSIN', '02/10/1970'],
            ['Yes', '89', 'John SMITH', '31/01/1988'],
            ['No', '0', 'Karl DO', '14/07/1972'],
            ['Yes', '69', 'Jean-Luc PASDIDEE', '06/07/1977']
        ]
    # Directory where test files will be create
    TEST_DIRECTORY = 'tmp'
    # File for tests
    CSV_TEST_FILENAME = 'test.csv'
    # Full path of the test file
    CSV_TEST_FILE_PATH = ''
    # Base name of the output test file
    OUTPUT_BASE_FILENAME = 'output'
    # Full base path of the output test file
    OUTPUT_BASE_FILE_PATH = ''
    # self.convert object
    convert = None

    @classmethod
    def setUpClass(cls):
        """Set up configuration for tests
        """
        if not os.path.exists(cls.TEST_DIRECTORY):
            os.mkdir(cls.TEST_DIRECTORY)
        for file in os.listdir(cls.TEST_DIRECTORY):
            os.remove(cls.TEST_DIRECTORY+os.path.sep+file)
        cls.CSV_TEST_FILE_PATH = cls.TEST_DIRECTORY+os.path.sep+cls.CSV_TEST_FILENAME
        cls.OUTPUT_BASE_FILE_PATH = cls.TEST_DIRECTORY+os.path.sep+cls.OUTPUT_BASE_FILENAME

    @classmethod
    def tearDownClass(cls):
        """Remove test directory at the end of tests
        """
        os.rmdir(cls.TEST_DIRECTORY)

    def setUp(self):
        """Initialise self.convert class and create the test file
        """
        self.convert = Convert()
        self.create_csv_test_file(self.TESTS_DATA)
        
    def tearDown(self):
        """Remove all files after each test
        """
        for file in os.listdir(self.TEST_DIRECTORY):
            os.remove(self.TEST_DIRECTORY+os.path.sep+file)

    def get_cell_in_xls(self, filename, row, col, sheet = None):
        """Get cell value of old Excel file

        :param row: Row of the cell
        :param col: Column of the cell
        :param sheet: Sheet in Excel workbook
        """
        workbook = xlrd.open_workbook(filename = filename)
        worksheet = None
        if sheet is None:
            worksheet = workbook.sheet_by_index(0)
        else:
            worksheet = workbook.sheet_by_name(sheet)
        return worksheet.cell_value(row - 1, col - 1)

    def get_cell_in_xlsx(self, filename, row, col, sheet = None):
        """Get cell value of new Excel file

        :param row: Row of the cell
        :param col: Column of the cell
        :param sheet: Sheet in Excel workbook
        """
        workbook = openpyxl.load_workbook(filename)
        worksheet = None
        if sheet is None:
            worksheet = workbook.worksheets[0]
        else:
            worksheet = workbook.get_sheet_by_name(sheet)
        return worksheet.cell(row = row, column = col).value

    def get_cell_in_ods(self, filename, row_index, col_index, sheet = None):
        """Get cell value of ods file

        :param row: Row of the cell
        :param col: Column of the cell
        :param sheet: Sheet name
        """
        ods_file = odf_load(filename)
        spreadsheet = ods_file.spreadsheet

        rows = list(spreadsheet.getElementsByType(TableRow))
        cells = list(rows[row_index - 1].getElementsByType(TableCell))
        cell_data = list(cells[col_index - 1].getElementsByType(P))
        return str(cell_data[0])

    def create_csv_test_file(self, filecsv_data, delimiter = ';'):
        """Create the CSV test file

        :param filecsv_data: Data of the CSV file
        :param delimiter: CSV column delimiter
        """
        with open(self.CSV_TEST_FILE_PATH, 'w', newline = '') as test_file:
            writer = csv.writer(test_file, delimiter = delimiter)
            for row in filecsv_data:
                writer.writerow(row)
            test_file.close()

################################################################################
# Tests for file functions                                                     #
################################################################################
    def test_create_csv_test_file(self):
        """Test creation of test file
        """
        with open(self.CSV_TEST_FILE_PATH, 'r') as test_file:
            data_to_test = test_file.readlines()
            self.assertEqual(len(data_to_test),len(self.TESTS_DATA))
            self.assertEqual('Karl DO', data_to_test[3].split(';')[2])
            self.assertIn('06/07/1977', data_to_test[4])
            test_file.close()

    def test_csv_copy(self):
        """Test self.convert to CSV without parameters (copy)
        """
        self.convert.start(self.CSV_TEST_FILE_PATH, self.OUTPUT_BASE_FILE_PATH+'.csv')
        with open(self.OUTPUT_BASE_FILE_PATH+'.csv', 'r') as test_file:
            data_to_test = test_file.readlines()
            self.assertEqual(len(data_to_test),len(self.TESTS_DATA))
            self.assertEqual('Karl DO', data_to_test[3].split(';')[2])
            self.assertIn('06/07/1977', data_to_test[4])
            test_file.close()

    def test_xls_copy(self):
        """Test self.convert to old Excel without parameters (copy)
        """
        test_file = self.OUTPUT_BASE_FILE_PATH+'.xls'
        self.convert.start(self.CSV_TEST_FILE_PATH, test_file)
        # First data
        self.assertEqual('Activated', self.get_cell_in_xls(test_file, 1, 1))
        # Last data
        self.assertEqual('06/07/1977', self.get_cell_in_xls(test_file, 5, 4))
        # Mid data
        self.assertEqual('John SMITH', self.get_cell_in_xls(test_file, 3, 3))

    def test_xlsx_copy(self):
        """Test self.convert to new Excel without parameters (copy)
        """
        test_file = self.OUTPUT_BASE_FILE_PATH+'.xlsx'
        self.convert.start(self.CSV_TEST_FILE_PATH, test_file)
        # First data
        self.assertEqual('Activated', self.get_cell_in_xlsx(test_file, 1, 1))
        # Last data
        self.assertEqual('06/07/1977', self.get_cell_in_xlsx(test_file, 5, 4))
        # Mid data
        self.assertEqual('John SMITH', self.get_cell_in_xlsx(test_file, 3, 3))

    def test_ods_copy(self):
        """Test self.convert to ods without parameters (copy)
        """
        test_file = self.OUTPUT_BASE_FILE_PATH+'.ods'
        self.convert.start(self.CSV_TEST_FILE_PATH, test_file)
        # First data
        self.assertEqual('Activated', self.get_cell_in_ods(test_file, 1, 1))
        # Last data
        self.assertEqual('06/07/1977', self.get_cell_in_ods(test_file, 5, 4))
        # Mid data
        self.assertEqual('John SMITH', self.get_cell_in_ods(test_file, 3, 3))
        
    def test_bad_file_extension(self):
        """Test input with extension without standard name
        """
        test_file = self.TEST_DIRECTORY+os.path.sep+'test.txt'
        # Rename CSV in TXT
        os.rename(self.TEST_DIRECTORY+os.path.sep+self.CSV_TEST_FILENAME,
                self.TEST_DIRECTORY+os.path.sep+'test.txt')
        with self.assertRaises(Exception):
            self.convert.start(test_file, self.OUTPUT_BASE_FILE_PATH)

    def test_missing_input_file(self):
        """Test exception if input file is missing
        """
        with self.assertRaises(Exception):
            self.convert.start('zapezapoeiopizeapoeia.ezaopeia', self.OUTPUT_BASE_FILE_PATH)

################################################################################
# Tests private methods                                                       #
################################################################################
    def test_get_file_by_ext_csv(self):
        """Test if .csv file name is recognized as CSV
        """
        file_type = self.convert.get_file_type_by_ext('test.csv')
        self.assertEqual(self.convert.CSV_FILE, file_type)
                         
    def test_get_file_by_ext_xls(self):
        """Test if .xls file name is recognized as old Excel
        """
        file_type = self.convert.get_file_type_by_ext('test.xls')
        self.assertEqual(self.convert.OLD_EXCEL_FILE, file_type)
                         
    def test_get_file_by_ext_xlsx(self):
        """Test if .xlsx file name is recognized as new Excel
        """
        file_type = self.convert.get_file_type_by_ext('test.xlsx')
        self.assertEqual(self.convert.NEW_EXCEL_FILE, file_type)
                         
    def test_get_file_by_ext_ods(self):
        """Test if .ods file name is recognized as ODS
        """
        file_type = self.convert.get_file_type_by_ext('test.ods')
        self.assertEqual(self.convert.ODS_FILE, file_type)
                         
    def test_get_file_by_ext_bad_type(self):
        """Test if unknow file format is recognized as unknow file
        """
        no_file_type = self.convert.get_file_type_by_ext('test')
        self.assertEqual(self.convert.UNKNOWN_FILE, no_file_type)
        backup_file_type = self.convert.get_file_type_by_ext('test.xls.bak')
        self.assertEqual(self.convert.UNKNOWN_FILE, backup_file_type)

    def test_convert_index_with_header(self):
        """Test if index is right
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                           self.OUTPUT_BASE_FILE_PATH+'.csv',
                           '{"moves": [{"from": "3", "to": "2"},{"from": "0", "to": "1", "action": {"set_row_index": "0"}}]}')
        self.assertEqual(2, self.convert.output_data[2][0])
                           
    def test_convert_index_without_header(self):
        """Test if index is right
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                           self.OUTPUT_BASE_FILE_PATH+'.csv',
                           '{"ignore_first_line_header": true, "moves": [{"from": "3", "to": "2"},{"from": "0", "to": "1", "action": {"set_row_index": "0"}}]}')
        self.assertEqual(2, self.convert.output_data[1][0])
                           
################################################################################
# Tests for config type                                                       #
################################################################################
    def test_string_config(self):
        """Test config from string
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                           self.OUTPUT_BASE_FILE_PATH+'.xls',
                           '{"moves": {"from": "2", "to": "1"}}')
        self.assertEqual('Money', self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))

    def test_json_config(self):
        """Test config from JSON
        """
        config = json.loads('{"moves": {"from": "2", "to": "1"}}')
        self.convert.start(self.CSV_TEST_FILE_PATH,
                           self.OUTPUT_BASE_FILE_PATH+'.xls',
                           config)
        self.assertEqual('Money', self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))

    def test_config_path_file(self):
        """Test config from JSON
        """
        # Create config file
        with open(self.TEST_DIRECTORY+os.path.sep+'config.json', 'w') as config_file:
            config_file.write('{"moves": {"from": "2", "to": "1"}}')
            config_file.close()
        # Open config file
        self.convert.start(self.CSV_TEST_FILE_PATH,
                           self.OUTPUT_BASE_FILE_PATH+'.xls',
                           self.TEST_DIRECTORY+os.path.sep+'config.json')
        self.assertEqual('Money', self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))

    def test_config_file(self):
        """Test config from JSON
        """
        # Create config file
        with open(self.TEST_DIRECTORY+os.path.sep+'config.json', 'w') as config_file:
            config_file.write('{"moves": {"from": "2", "to": "1"}}')
            config_file.close()
        # Open config file
        with open(self.TEST_DIRECTORY+os.path.sep+'config.json', 'r') as config_file:
            self.convert.start(self.CSV_TEST_FILE_PATH,
                               self.OUTPUT_BASE_FILE_PATH+'.xls',
                               config_file)
            config_file.close()
        self.assertEqual('Money', self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))

################################################################################
# Tests for config params                                                      #
################################################################################

    def test_input_file_type_specified(self):
        """Test input with extension without standard name
        """
        test_file = self.TEST_DIRECTORY+os.path.sep+'test.txt'
        # Rename CSV in TXT
        os.rename(self.TEST_DIRECTORY+os.path.sep+self.CSV_TEST_FILENAME,
                self.TEST_DIRECTORY+os.path.sep+'test.txt')
        self.convert.start(test_file, self.OUTPUT_BASE_FILE_PATH+'.xls', '{"input_file_type": "csv"}')
        self.assertEqual(self.TESTS_DATA[3][2],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 4, 3))

    def test_output_file_type_specified(self):
        """Test output with extension without standard name
        """
        self.convert.start(self.CSV_TEST_FILE_PATH, self.OUTPUT_BASE_FILE_PATH+'.txt', '{"output_file_type": "xls"}')
        self.assertEqual(self.TESTS_DATA[3][2],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.txt', 4, 3))

    def test_input_csv_delimiter(self):
        """Test input CSV file with different column delimiter
        """
        self.create_csv_test_file(self.TESTS_DATA, '|')
        self.convert.start(self.CSV_TEST_FILE_PATH, self.OUTPUT_BASE_FILE_PATH+'.xls', '{"input_csv_delimiter": "|"}')
        self.assertEqual(self.TESTS_DATA[0][2],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 3))
        
    def test_output_csv_delimiter(self):
        """Test output CSV file with different column delimiter
        """
        self.convert.start(self.CSV_TEST_FILE_PATH, self.OUTPUT_BASE_FILE_PATH+'.csv', '{"output_csv_delimiter": "|"}')
        with open(self.OUTPUT_BASE_FILE_PATH+'.csv', 'r') as test_file:
            test_file_content = test_file.readlines()
            self.assertIn(self.TESTS_DATA[3][0]+'|', test_file_content[3])
            self.assertEqual(len(self.TESTS_DATA[2]) - 1, test_file_content[2].count('|'))
            test_file.close()

    def test_input_first_line_header(self):
        """Test if first line is the header (no transformation)
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"input_first_line_header": true, "moves": {"from": "3", "to": "1", "transform": "to_lower"}}')
        self.assertEqual(self.TESTS_DATA[0][2], self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))
        self.assertEqual(self.TESTS_DATA[1][2].lower(), self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 2, 1))
        
    def test_input_no_first_line_header(self):
        """Test if first line is not the header (apply transformation)
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"input_first_line_header": false, "moves": {"from": "3", "to": "1", "transform": "to_upper"}}')
        self.assertEqual(self.TESTS_DATA[0][2].upper(), self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))
        self.assertEqual(self.TESTS_DATA[1][2].upper(), self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 2, 1))
        
    def test_input_ignore_first_line_header_csv(self):
        """Test removed first line in CSV files
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.csv',
                      '{"ignore_first_line_header": true}')
        with open(self.OUTPUT_BASE_FILE_PATH+'.csv', 'r') as test_file:
            data_to_test = test_file.readlines()
            self.assertNotEqual('Activated', data_to_test[0][0])

    def test_input_ignore_first_line_header_xls(self):
        """Test removed first line in old Excel files
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"ignore_first_line_header": true}')
        self.assertEqual(self.TESTS_DATA[1][0], self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))

    def test_input_ignore_first_line_header_xlsx(self):
        """Test removed first line in new Excel files
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xlsx',
                      '{"ignore_first_line_header": true}')
        self.assertEqual(self.TESTS_DATA[1][0], self.get_cell_in_xlsx(self.OUTPUT_BASE_FILE_PATH+'.xlsx', 1, 1))

    def test_input_xls_sheet_name(self):
        """Test if the name of the output sheet is specified in config
        """
        second_test_file = self.TEST_DIRECTORY+os.path.sep+'second.xls'
        # Create Excel file
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      second_test_file,
                      '{"output_sheet_name": "just_a_test"}')
        self.convert.start(second_test_file,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"input_sheet_name": "just_a_test"}')
        self.assertEqual(self.TESTS_DATA[1][2], self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 2, 3))
        
    def test_output_xls_sheet_name(self):
        """Test if the name of the input sheet is specified in config
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"output_sheet_name": "just_a_test"}')
        self.assertEqual(self.TESTS_DATA[1][2], self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 2, 3, 'just_a_test'))

    def test_input_ods_sheet_name(self):
        """Test if the name of the output sheet is specified in config
        """
        second_test_file = self.TEST_DIRECTORY+os.path.sep+'second.ods'
        # Create Excel file
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      second_test_file,
                      '{"output_sheet_name": "just_a_test"}')
        self.convert.start(second_test_file,
                      self.OUTPUT_BASE_FILE_PATH+'.ods',
                      '{"input_sheet_name": "just_a_test"}')
        self.assertEqual(self.TESTS_DATA[1][2], self.get_cell_in_ods(self.OUTPUT_BASE_FILE_PATH+'.ods', 2, 3))
        
    def test_output_ods_sheet_name(self):
        """Test if the name of the input sheet is specified in config
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.ods',
                      '{"output_sheet_name": "just_a_test"}')
        self.assertEqual(self.TESTS_DATA[1][2], self.get_cell_in_ods(self.OUTPUT_BASE_FILE_PATH+'.ods', 2, 3, 'just_a_test'))

    def test_one_move(self):
        """Test some moves
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"moves": {"from": "2", "to": "1"}}')
        self.assertEqual(self.TESTS_DATA[0][1],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 1, 1))
        self.assertEqual(self.TESTS_DATA[3][1],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 4, 1))
        # Out of range
        with self.assertRaises(IndexError):
            self.assertEqual('',
                             self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 4, 2))
        
    def test_multiple_moves(self):
        """Test some moves
        """
        self.convert.start(self.CSV_TEST_FILE_PATH,
                      self.OUTPUT_BASE_FILE_PATH+'.xls',
                      '{"moves": [{"from": "1", "to": "1"}, {"from": "2", "to": "3"}, {"from": "3", "to": "2"}]}')
        self.assertEqual(self.TESTS_DATA[2][0],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 3, 1))
        self.assertEqual(self.TESTS_DATA[3][1],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 4, 3))
        self.assertEqual(self.TESTS_DATA[1][2],
                         self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 2, 2))
        # Out of range
        with self.assertRaises(IndexError):
            self.assertEqual('',
                             self.get_cell_in_xls(self.OUTPUT_BASE_FILE_PATH+'.xls', 4, 4))
    
if __name__ == '__main__':
    unittest.main()
