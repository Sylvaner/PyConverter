__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

import re

class remove_digits():
    def transform(input_data):
        """Remove all digits of a string.
        
        :param input_data: Text with digits.
        
        :return: String without digits.
        :rtype: str
        """
        if isinstance(input_data, str):
            return re.sub('\\d+', '', input_data)
        return input_data