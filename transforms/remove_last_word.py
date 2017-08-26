__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class remove_last_word():
    def transform(input_data):
        """Remove last word of a string with more than one word.
        
        :param input_data: Text with more than one word.
        
        :return: String without the last word.
        :rtype: str
        """
        if isinstance(input_data, str):
            if ' ' in input_data:
                parts = input_data.split(' ')
                while parts[len(parts) - 1] == '' and len(parts) > 1:
                    parts = parts[:-1]
                return ' '.join(parts[:-1])
            # Remove the single world
            else:
                return ''
        return input_data
