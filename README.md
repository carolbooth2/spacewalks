# Spacewalks

## Overview
Spacewalks is a python analysis tool for generating visualisations and 
statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity and crew sizes

- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites
Spacewalks was developed using Python 3.12

To install and run Spacewalks you will need to have Python >=3.12 installed. You will also need the following libraries:

- [Numpy](https://www.numpy.org/)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [pytest](https://docs.pytest.org/)
- [pandas](https://pandas.pydata.org/)

## Installation instructions
Clone the repository to your local machine using git:

`git clone git@github.com:carolbooth2/spacewalks.git`

Create a virtual environment:
`python -m venv venv_spacewalks`

Activate it:
`source venv_spacewalks/Scripts/activate` (Windows)

`source venv_spacewalks/bin/activate` (unix)

Install dependencies:
`python -m pip install -r requirements.txt`

## Usage

Run the main analysis code in a bash terminal with:
`python eva_data_analyis.py`
with optional command line arguments for data input and csv output name:
`python eva_data_analyis.py <input> <output>`

