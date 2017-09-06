__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class slice():
    def action(input_data, params, current_row, current_index):
        """Slice a string
        :param input_data: String with text to slice
        :param params: dict with 'start' and 'end' key. One of them is optionnal
        :param current_row: Not used
        :param current_index: Not used
        
        :return: Input sliced string
        :rtype: str
        """
        if isinstance(params, dict):
            if 'start' in params:
                if 'end' in params:
                    return input_data[params['start']:params['end']]
                else:
                    return input_data[params['start']:]
            elif 'end' in params:
                return input_data[:params['end']]
        return input_data
