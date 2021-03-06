__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class set_row_index():
    def action(input_data, params, current_row, current_index):
        """Set the current index of the row
        :param input_data: Not used
        :param params: Base index
        :param current_row: Not used
        :param current_index: Index to return
        
        :return: Index of the row
        :rtype: str
        """
        if isinstance(params, int):
            return current_index + params
        elif isinstance(params, str):
            return current_index + int(params)
        return current_index
