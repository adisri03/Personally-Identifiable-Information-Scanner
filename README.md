# PII-Scanner


## Introduction
This Python script uses the `Faker` library to generate fake Personally Identifiable Information (PII) data and creates both an Excel file and a PDF document containing this fake data. It can be helpful for testing and development purposes without using real sensitive information.

## Overview
The script consists of functions to generate fake PII data, create an Excel file with the generated data, and create a PDF document with the same fake data.

## Installation
To run this script, you need to have Python installed on your machine. Additionally, you'll need to install the required libraries using the following command:

```bash
pip install faker reportlab pandas
```

## How to Run
Clone or download the repository to your local machine.

Open a terminal and navigate to the project directory.

Run the script using the following command:

```bash
python createFakeData.py
```
The script will generate fake PII data, create an Excel file (fake_pii_data.xlsx), and a PDF file (fake_pii_data.pdf) in the current working directory.

Then run the script to identify PII data using the following command:
```bash
python Scanner.py
```



Feel free to customize the script parameters (e.g., number of records, output file names) by modifying the relevant variables in the script.
