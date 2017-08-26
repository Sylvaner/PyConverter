__author__ = "Sylvain Dangin"
__licence__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sylvain Dangin"
__email__ = "sylvain.dangin@gmail.com"
__status__ = "Development"

class concat():
    def action(input_data, params, current_row, current_index):
        """Concat multiple columns in the cell.
        :param input_data: Not used.
        :param params: Dict with following keys: 
          - col_list: List of columns to concat in the cell.
          - separator (optional): Separator to put between columns.
        :param current_row: Not used
        :param current_index: Not used
        
        :return: Value to set.
        :rtype: str
        """
        if isinstance(params, dict):
            col_list = []
            if 'col_list' in params:
                for col in params['col_list']:
                    col_list.append(current_row[col - 1])
                if 'separator' in params:
                    return params['separator'].join(col_list)
                else:
                    return ''.join(col_list)
        return input_data
