# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researcher to generate visualisations and statistical summaries of NASA's extravehicular activity datasets

## Features
Key features of Spacewalks:

- generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show cumulative duration of spacewalks over time

## Prerequisites

Spacewalks was developed in Python version 3.12

To install and run Spacewalks you will need to have Python >=3.12
You will also need the following libraries
- [NumPy](https://www.numpy.org) >=2.0.0 - Spacewalks test suite uses Numpy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >= 3.0.0 - Spacewalks uses Matplotlib to make plots.
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0 - Spacewalks uses Pytest for its test suite
- [pandas](https://pandas.pydata.org) >=2.2.0 - Spacewalks uses Pandas for data frame manipulation and loading/saving data

## Installation instructions
+ Clone the repository using Git.  
If you don't have Git installed, you can download it from the official Git website

```
git clone https://github.com/your-repository-url/spacewalks.git
cd spacewalks
```
+ Install the necessary dependencies:
```
python3 -m pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
``` 
+ To ensure everything is working correctly, run the tests using pytest.

```
python3 -m pytest
``` 


## Example usage
python3 eva_data_analysys_py input.json output.csv graph.png

where input.json file is a JSON file in the local directory data
output.csv is a CSV file to be written in the local directory results
graph.png is a PNG to be written in the local directory results