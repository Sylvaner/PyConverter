__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class is_value():
    def test_filter(params, current_row, current_index):
        """Test if a column is a specific value.

        :param params: Dict -> {"Value": "Column number"}
        :param current_row: Data of the current row
        :param current_index: Current index of the row
        
        :return: True if the value is found.
        :rtype: Boolean
        """
        if isinstance(params, dict):
            for key in params:
                index = params[key]
                if isinstance(index, str):
                    index = int(index)
                if current_row[index - 1] == key:
                    return True
        return False
