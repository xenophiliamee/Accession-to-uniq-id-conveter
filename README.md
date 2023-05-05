# Accession Number to Unique ID Converter

This script is designed to take a list of NCBI accession numbers and search for the corresponding unique identifiers using the NCBI website.
It then saves the results to a text file.

## Prerequisites 
 This script requires the following libraries to be installed:

- *requests*
- *beautifulsoup4*

These can be installed using pip: 

> pip install requests

> pip install beautifulsoup4

## Usage

To use this script, you will need to create a file called **accession_numbers.txt** in the same directory as the script. This file should contain one NCBI accession number per line


Once you have created the input file, you can run the script by executing the following command in your terminal:


> python accession_to_unique_id.py

The script will search for each accession number on the NCBI website and extract the corresponding unique identifier. The results will be saved to a file called **unique_ids.txt.**

## Output Format
The output file **(unique_ids.txt)** will contain two columns separated by a tab character **(\t).** The first column will contain the accession number, and the second column will contain the corresponding unique identifier. If a unique identifier could not be found for an accession number, the second column will be blank.

## License
This script is licensed under the **MIT License.** Feel free to modify and distribute it as you see fit.
