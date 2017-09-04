__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class is_empty():
    def test_filter(params, current_row, current_index):
        """Test if a column is empty.

        :param params: Column to test
        :param current_row: Data of the current row
        :param current_index: Current index of the row
        
        :return: True if the column is empty.
        :rtype: Boolean
        """
        if isinstance(params, str):
            params = int(str)
        if isinstance(params, int):
            if current_row[params - 1] == '':
                return True
        return False
