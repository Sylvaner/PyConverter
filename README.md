# PyConverter

This python script was written for convert spreadsheet file to another format (XLS, XLSX, CSV) and transform the data if necessary during the process.

It can be used as a python module or directly from command line.

It's possible to simply add transforms for your usage.

# Installation
<pre>
git clone https://github.com/Sylvaner/PyConverter
</pre>

# Basic usage
## Convert XLS to CSV
### Command line
```
python pyconvert.py input.xls output.csv
```

### Python script
```python
from pyconvert import Convert

convert = Convert()
convert.start('test.xls', 'test.csv')
```

## Switch column 1 and 2, keep the third column from CSV to XLS
### Command line
```
python pyconvert.py test.csv test.xls "{\"moves\": [{\"from\": 1, \"to\": 2},{\"from\": 2, \"to\": 1},{\"from\": 3, \"to\": 3}]}"
```

### Python script
```python
from pyconvert import Convert

convert = Convert()
convert.start('test.xls', 'test.csv', '{"moves": [ {"from": 1, "to": 2}, {"from": 2, "to": 1}, {"from": 3, "to": 3}]}')
```

## Use config file for convert XLS to XLSX and change the order of four columns
Create config file named __config.json__ : 
```json
{
  "moves": [
    {"from": 4, "to": 1},
    {"from": 3, "to": 2},
    {"from": 2, "to": 3},
    {"from": 1, "to": 4}
  ]
}
```

And call it : 

### Command line
```
python pyconvert.py input.xls output.xlsx config.json
```

### Python script
```python
from pyconvert import Convert

convert = Convert()
convert.start('test.xls', 'test.csv', 'config.json')
```

# Advanced usage
Only the config file will be showed in next examples

## Add row index and remove header row
```json
{
  "ignore_first_line_header": true,
  "moves": [
    {"from": 0, "to": 1, "action": {"set_row_index": 0}},
    {"from": 1, "to": 2},
    {"from": 2, "to": 3},
    {"from": 3, "to": 4}
  ]
}
```

### Input
<table>
  <tr>
    <th>Lastname</th>
    <th>Firstname</th>
    <th>ID</th>
    <th>Gender</th>
  </tr>
  <tr>
    <td>Peregrin</td>
    <td>Touc</td>
    <td>3434342</td>
    <td>Male</td>
  </tr>
    <td>brandibouc</td>
    <td>meriadoc</td>
    <td>2369127</td>
    <td>&nbsp;&nbsp;Male&nbsp;&nbsp;</td>
  </tr>
    <td>Chaumine</td>
    <td>Rose</td>
    <td>320988</td>
    <td>&nbsp;Female</td>
  </tr>
    <td>Sacquet</td>
    <td>bilbo</td>
    <td>239820</td>
    <td>&nbsp;&nbsp;Male</td>
  </tr>
    <td>SACQUET</td>
    <td>FRODO</td>
    <td>29399</td>
    <td>&nbsp;Male&nbsp;&nbsp;</td>
</table>

### Output

<table>
  <tr>
    <td>1</td>
    <td>Peregrin</td>
    <td>Touc</td>
    <td>3434342</td>
  </tr>
    <td>2</td>
    <td>brandibouc</td>
    <td>meriadoc</td>
    <td>2369127</td>
  </tr>
    <td>3</td>
    <td>Chaumine</td>
    <td>Rose</td>
    <td>320988</td>
  </tr>
    <td>4</td>
    <td>Sacquet</td>
    <td>bilbo</td>
    <td>239820</td>
  </tr>
    <td>5</td>
    <td>SACQUET</td>
    <td>FRODO</td>
    <td>29399</td>
</table>

## Capitalize first column, Capitalize first letter on second column, trim third column

```json
{
  "moves": [
    {"from": 1, "to": 1, "transform": "to_upper"},
    {"from": 2, "to": 2, "transform": "up_first_letter"},
    {"from": 4, "to": 3, "transform": "trim"}
  ]
}
```

### Input

<table>
  <tr>
    <th>Lastname</th>
    <th>Firstname</th>
    <th>ID</th>
    <th>Gender</th>
  </tr>
  <tr>
    <td>Peregrin</td>
    <td>Touc</td>
    <td>3434342</td>
    <td>Male</td>
  </tr>
    <td>brandibouc</td>
    <td>meriadoc</td>
    <td>2369127</td>
    <td>&nbsp;&nbsp;Male&nbsp;&nbsp;</td>
  </tr>
    <td>Chaumine</td>
    <td>Rose</td>
    <td>320988</td>
    <td>&nbsp;Female</td>
  </tr>
    <td>Sacquet</td>
    <td>bilbo</td>
    <td>239820</td>
    <td>&nbsp;&nbsp;Male</td>
  </tr>
    <td>SACQUET</td>
    <td>FRODO</td>
    <td>29399</td>
    <td>&nbsp;Male&nbsp;&nbsp;</td>
</table>

### Output

<table>
  <tr>
    <th>Lastname</th>
    <th>Firstname</th>
    <th>Gender</th>
  </tr>
  <tr>
    <td>PEREGRIN</td>
    <td>Touc</td>
    <td>Male</td>
  </tr>
    <td>BRANDIBOUC</td>
    <td>Meriadoc</td>
    <td>Male</td>
  </tr>
    <td>CHAUMINE</td>
    <td>Rose</td>
    <td>Female</td>
  </tr>
    <td>SACQUET</td>
    <td>Bilbo</td>
    <td>Male</td>
  </tr>
    <td>SACQUET</td>
    <td>Frodo</td>
    <td>Male</td>
</table>

# Documentation
## Configuration
The configuration file use JSON format. You can configure all parameters of the conversion in this file.
### input\_file\_type 
Format of the input file. Must be used if the input file have a not standard extension.
__String__ : csv, xls, xlsx
### output\_file\_type
Format of the output file. Must be used if the output file have a not standard extension.

__String__ : csv, xls, xlsx
### input\_csv\_delimiter
CSV column delimiter character of the input file. 

__String__ : Default __";"__
### output\_csv\_delimiter
CSV column delimiter character of the output file.

__String__ : Default __";"__
### input\_first\_line\_header
Indicate if the first line is a header

__Boolean__ : Default __true__
### ignore\_first\_line\_header
Remove first line header in output 

__Boolean__ : Default __false__
### input_xls_sheet_name: 
Title of the sheet for Excel input

__String__ : Default __first worksheet__
### output\_xls\_sheet\_name: Title of the sheet for Excel output 
Title of the sheet for Excel input

__String__ : Default __"export"__
### input\_encoding
Encoding using in CSV input file

__String__ : Default Windows __iso-8859-1__, Others __utf-8__
### output\_encoding
Encoding using in CSV output file

__String__ : Default Windows __iso-8859-1__, Others __utf-8__
### moves
List of columns moves and changes

This is the most important key. Each move must be stored in an array with 2 keys : __from__ and __to__. The first column is 1.
```json
{
  "moves": [
    {"from": 0, "to": 1, "action": {"set_row_index": 2}},
    {"from": 3, "to": 1, "transform": ["last_word", "to_upper"]},
    {"from": 4, "to": 4, "transform": "first_char"},
    {"from": 2, "to": 3, "transform": "trim", "action": {"replace": {"Yes": "Y", "No": "N"}}}
  ]
}
```

All transforms or actions must be specify in a move. It's possible to add multiple transforms/actions in one move.

# Transformations
## first\_char
Get the first char of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "first_char"}
  ]
}
```
## first\_word
Get the first word of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "first_word"}
  ]
}
```
## last\_word
Get the last word of the cell. Work with punctuation.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "last_word"}
  ]
}
```
## remove\_digits
Remove all digits in the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "remove_digits"}
  ]
}
```
## remove\_last\_word
Remove last word of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "remove_last_word"}
  ]
}
```
## to\_lower
Lower all character in the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "to_lower"}
  ]
}
```
## to\_upper
Capitalize all character in the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "to_upper"}
  ]
}
```
## trim
Remove extra spaces at the begin and the end of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "trim"}
  ]
}
```
## up\_all\_first\_letters
Capitalize first letter of all words of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "up_all_first_letters"}
  ]
}
```
## up\_first\_letter
Capitalize the first letter of the cell.
```json
{
  "moves": [
    {"from": 1, "to": 2, "transform": "up_first_letter"}
  ]
}
```

## Create a transformation
If you need to create transformations for you project, add a python file with the name of the transformation in the directory transforms.

Transformation is a class with the name of the transformation and a static method called transform with the data of the cell in param.

This method must return the data of the cell after the transformation.

Example with the _to\_lower_ transformation : 
```python
class to_lower():
    def transform(input_data):
        return input_data.lower()
```

# Actions
## concat
Concat multiple columns in the cell. Parameters must have a key called __col\_list__ with an array of columns to concat (First column index is 1). It's possible to specify the separator with the key __separator__ and a string in the value.
## date\_format
Change the format of the date in the cell. Parameters of the action must have 2 keys, the input format and the output format.
## replace
Replace strings in the cell. Parameters must be a JSON objects where the key have the string to change and the value the 
## set\_row\_index
Set the current row index in the cell. Useful for Id. Parameters must be an integer that represent the start index.
## set\_value
Set a value in the cell. Parameters must be a string with the value to set.

## Create an action
If you need to create actions for you project, add a python file with the name of the action in the directory actions.

Action is a class with the name of the action and a static method called action with 4 params : 
 - Data of the cell,
 - Parameters of the action,
 - Data of the current row,
 - Current index.

This method must return the data of the cell after the action.

```python
class concat_first_col():
    def action(input_data, params, current_row, current_index):
        return current_row[0]+input_data
```


