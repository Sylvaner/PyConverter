__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class first_char():
    def transform(input_data):
        """Get the first character of a string.
        
        :param input_data: String with some characters.
        
        :return: The first character of the string
        :rtype: str or type of the input data if not a string
        """
        if isinstance(input_data, str):
            if len(input_data) > 0:
                return input_data[0]
        return input_data
