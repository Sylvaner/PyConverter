__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class replace():
    def action(input_data, params, current_row, current_index):
        """Replace strings with others
        :param input_data: String with text to replace
        :param params: dict with array of items to replace (Example: {"Yes": "Y", "No", "N"}
        :param current_row: Not used
        :param current_index: Not used
        
        :return: Input with replaced strings
        :rtype: str
        """
        if isinstance(input_data, str) and isinstance(params, dict):
            for item in params:
                input_data = input_data.replace(item, params[item])
        return input_data
