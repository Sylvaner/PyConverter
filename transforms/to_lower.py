__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class to_lower():
    def transform(input_data):
        """Low all the letters of a string
        
        :param input_data: String with the text to transform.
        
        :return: String lowed
        :rtype: str
        """
        if isinstance(input_data, str):
            return input_data.lower()
        return input_data
