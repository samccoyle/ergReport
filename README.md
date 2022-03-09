# ergReport

## What is it?
- ergReport takes in the `.json` files that the Concept2 ErgRace program exports and converts it into an `.xlsx` file
- It replaces the now deprecated functionality found in ErgRace

## Features
- Importing `.json` files that ErgRace produces and converting them into `.xlsx` files
- Combining multiple events `.json` files into one `.xlsx` file
- Converting time data into a format useable in Excel and Google sheets
- Importing athlete weight data for automatic time correction
- Removing extra data from the `.json` file using a configuration file    

## Setup
### Requirements:
- Python3
- pip3
- Internet connection for missing libraries

### Installation:
1. Download the repository to your computer 
2. Using terminal/powershell:
 - In the downloaded folder run: `pip3 install -r requirements.txt`

### Customizing your setup
#### Weight
- Using weight data requires a `Weights.xlsx` file to be in the main folder
 - See `Weights.xlsx` in the example folder for formatting guidelines
 - Any athlete missing weight data will be skipped
 - Athlete names must appear exactly as they are entered in the ErgRace program

#### Customizing exported columns
- `columns_ignore.txt` contains all of the columns to be ignored
- Any column that contains the word in the list will be ignored
 - Ex: `serial` in `columns_ignore.txt` will ignore the column `serial_number` 

## Running an example
1. In the terminal run `python3 ergReport.py -e`
2. A new file named `results.xlsx` will be created
3. A new file named `results.xlsx` will be created
Any changes made in the `Example` folder will not effect the `ergReport` folder

## Running with your data
1. Add your `.json` file(s) for the `ergReport` folder
 - Optionally add your `Weights.xlsx` file to the `ergReport` folder
2. In the terminal run `python3 ergReport.py`
3. A new file named `results.xlsx` will be created
Re running the program will overwrite the `results.xlsx` file

## TODO 
- Add graphed data export to pdf 
- Cross compile for windows and linux