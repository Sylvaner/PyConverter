__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class up_first_letter():
    def transform(input_data):
        """Up only the first letter of the string.
        
        :param input_data: String with the text to transform.
        
        :return: String capitalized
        :rtype: str
        """
        if isinstance(input_data, str):
            return input_data.capitalize()
        return input_data
