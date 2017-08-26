__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class to_upper():
    def transform(input_data):
        """Up all letters of a string.
        
        :param input_data: String to up.
        
        :return: String upped.
        :rtype: str
        """
        if isinstance(input_data, str):
            return input_data.upper()
        return input_data
