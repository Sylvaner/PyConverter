__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class last_word():
    def transform(input_data):
        """Get the last word of a string with more than one word.
        
        :param input_data: Text with more than one word.
        
        :return: The last word of the input string.
        :rtype: str
        """
        if isinstance(input_data, str):
            if ' ' in input_data:
                # Remove punctuation
                find_punctuation = True
                punctuations = ['.', '?', '!', ',']
                while find_punctuation:
                    find_punctuation = False
                    for punctuation in punctuations:
                        if punctuation == input_data[len(input_data) - 1]:
                            find_punctuation = True
                            input_data = input_data[:-1]
                            # Remove space before punctuation
                            if input_data[len(input_data) - 1] == ' ':
                                input_data = input_data[:-1]
                            break
                parts = input_data.split(' ')
                return parts[len(parts) - 1]
        return input_data
