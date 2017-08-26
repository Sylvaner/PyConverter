__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

from datetime import datetime

class date_format():
    def action(input_data, params, current_row, current_index):
        """Convert date from a specified format to another format
        :param input_data: String of the date to convert
        :param params: dict with 2 keys: 
         - input: Format of the input date (Example: %Y-%m-%d)
         - output: Format of the output date (Example: %Y/%m/%d)
        :param current_row: Not used
        :param current_index: Not used
        
        :return: Input date converted
        :rtype: str
        """
        if isinstance(input_data, str) and isinstance(params, dict) and input_data is not "":
            if 'input' in params and 'output' in params:
                try:
                    d = datetime.strptime(input_data, params['input'])
                    return d.strftime(params['output'])
                except ValueError:
                    return input_data
        return input_data
