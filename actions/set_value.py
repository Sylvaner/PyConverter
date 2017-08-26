__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class set_value():
    def action(input_data, params, current_row, current_index):
        """Set a fixed value
        :param input_data: Not used
        :param params: Value to return.
        :param current_row: Not used
        :param current_index: Not used
        
        :return: Value to set.
        :rtype: str
        """
        if isinstance(params, str):
            return params
        return input_data
