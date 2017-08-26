__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class first_word():
    def transform(input_data):
        """Get the first word of a string with more than one word.
        
        :param input_data: Text with more than one word.
        
        :return: The first word of the input string.
        :rtype: str or type of the input data if not a string
        """
        if isinstance(input_data, str):
            if ' ' in input_data:
                return input_data.split(' ')[0]
        return input_data
