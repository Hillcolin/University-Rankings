# University Ranking Information Tool

## Description
This Python program takes two input CSV files (`TopUni.csv` and `capitals.csv`) and performs various tasks related to university rankings and country data. It generates a set of statistics and information, which are written to an output file (`output.txt`).

### Features:
- Counts the total number of universities in the top 100 rankings.
- Lists the available countries and continents in the top 100.
- Finds the ranking of a selected university (highest rank in the chosen country).
- Provides the top university in the selected country.
- Calculates the average score of universities in the selected country.
- Compares the selected country’s score to the top university score in its continent.
- Retrieves the capital city of the selected country.
- Lists universities that contain the capital city name in their title.

## Input Files:
1. **TopUni.csv**: Contains university ranking information (including country and score).
2. **capitals.csv**: Contains country capitals and continent data.

## Output:
- The program writes the output to a file named `output.txt`. The output includes:
  - Total number of universities in the top 100.
  - List of available countries and continents.
  - Information about the selected country’s top university and ranking.
  - The average score in the selected country.
  - The relative score of the selected country compared to its continent’s highest-ranking university.
  - The capital city of the selected country.
  - A list of universities with the capital city in their name.

## Usage:
1. The user is prompted to input a country name.
2. The program will then process the input and generate the required information.
3. All the results will be written to `output.txt`.


## How It Works:
- The `getInformation()` function integrates the various features, calling other helper functions to gather information based on the selected country.
- The program uses CSV reading and data processing with pandas and standard Python libraries.

## Notes:
- The input files must be in CSV format and properly formatted.
- The program is designed to handle countries present in the provided CSV files.
- This tool was created in 2021.
