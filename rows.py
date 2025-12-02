"""
This script demonstrates how to inspect and view data in a pandas DataFrame.
It shows how to display the first and last few rows of a dataset.
"""

import pandas as pd
import os

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} was not found.")
    
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading the file: {e}")
        raise

def display_data_head_tail(df, num_rows=10):
    """
    Display the first and last few rows of a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to display
        num_rows (int): Number of rows to display from head and tail
    """
    # Display header
    print("\n" + "="*50)
    print(f"First {num_rows} rows of the dataset:")
    print("="*50)
    print(df.head(num_rows))
    
    # Display separator
    print("\n" + "="*50)
    print(f"Last {num_rows} rows of the dataset:")
    print("="*50)
    print(df.tail(num_rows))
    
    # Display dataset information
    print("\n" + "="*50)
    print("Dataset Information:")
    print("="*50)
    print(f"Total Rows: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    print("\nColumn Names:", ", ".join(df.columns))

def main():
    """Main function to demonstrate data inspection."""
    # File path - using a relative path from the script location
    data_file = 'annual-enterprise-survey-2024-financial-year-provisional.csv'
    
    try:
        # Load the data
        print(f"Loading data from {data_file}...")
        df = load_data(data_file)
        
        # Display data
        display_data_head_tail(df, num_rows=10)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
