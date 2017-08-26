__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class trim():
    def transform(input_data):
        """Remove the spaces at the start and the end of the string
        
        :param input_data: String with spaces to remove.
        
        :return: String without useless spaces
        :rtype: str
        """
        if isinstance(input_data, str):
            return input_data.strip()
        return input_data
