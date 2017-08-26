__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class up_all_first_letters():
    def transform(input_data):
        """Up the firsts letters of all words.
        
        :param input_data: String with the text to transform.
        
        :return: String capitalized
        :rtype: str
        """
        if isinstance(input_data, str):
            return input_data.title()
        return input_data
