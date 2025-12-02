# Pandas Learning Repository

This repository contains various Python scripts demonstrating different functionalities of the Pandas library for data manipulation and analysis.

## Files Overview

1. **save.py** - Demonstrates saving DataFrames to different file formats (CSV, Excel, JSON)
2. **rows.py** - Shows how to view data using head() and tail() methods
3. **desription.py** - Contains examples of statistical analysis with describe()
4. **info.py** - Demonstrates getting DataFrame information with info()
5. **specifice.py** - Shows column selection, row filtering, and combining multiple conditions
6. **topic.py** - Basic DataFrame operations including shape and columns attributes
7. **app.py** - Examples of reading different file formats (CSV, Excel) with encoding options

## Pandas Methods Used

### DataFrame Creation
- `pd.DataFrame(data)` - Creates a DataFrame from a dictionary

### Data Input/Output
- `pd.read_csv('filename.csv', encoding='utf-8')` - Reads data from a CSV file into a DataFrame (use encoding parameter for special characters)
- `pd.read_excel('filename.xlsx')` - Reads data from an Excel file
- `df.to_csv('output.csv', index=False)` - Saves DataFrame to CSV file
- `df.to_excel('output.xlsx', index=False)` - Saves DataFrame to Excel file (requires openpyxl)
- `df.to_json('output.json', index=False)` - Saves DataFrame to JSON format

### Data Inspection
- `df.head(n)` - Returns first n rows (default 5)
- `df.tail(n)` - Returns last n rows (default 5)
- `df.info()` - Prints concise summary of a DataFrame
- `df.describe()` - Generates descriptive statistics
- `df.shape` - Returns a tuple representing the dimensionality of the DataFrame
- `df.columns` - Returns the column labels of the DataFrame

## Key Pandas Concepts

### DataFrame
A 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.

### Series
A one-dimensional labeled array capable of holding any data type.

### Indexing and Selection
- `df['column_name']` - Select a single column
- `df[['col1', 'col2']]` - Select multiple columns
- `df.loc[]` - Label-based indexing
- `df.iloc[]` - Integer position-based indexing

### Data Cleaning
- `df.dropna()` - Remove missing values
- `df.fillna(value)` - Fill missing values
- `df.rename(columns={'old':'new'})` - Rename columns

### Data Selection and Filtering
- `df['column']` - Select a single column (returns Series)
- `df[['col1', 'col2']]` - Select multiple columns (returns DataFrame)
- `df[df['column'] > value]` - Filter rows based on condition
- `df[(condition1) & (condition2)]` - Combine multiple conditions

### Data Aggregation
- `df.groupby('column').mean()` - Group data and calculate mean
- `df.pivot_table(values, index, columns, aggfunc)` - Create pivot tables

## Requirements
- Python 3.x
- pandas
- openpyxl (for Excel support)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
Run any of the Python scripts to see examples of different pandas functionalities:
```bash
python save.py
python rows.py
python desription.py
python info.py
```

## Data Files
- `Financial Sample.xlsx` - Sample financial data
- `annual-enterprise-survey-2024-financial-year-provisional.csv` - Enterprise survey data

## Additional Resources
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
