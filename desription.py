"""
This script demonstrates how to generate statistical summaries of pandas DataFrames
using the describe() method. It shows examples with both small sample data and a larger dataset.
"""

import pandas as pd
import os

def create_sample_dataframe():
    """
    Create a sample DataFrame with employee information.
    
    Returns:
        pd.DataFrame: A DataFrame containing sample employee data.
    """
    # Sample employee data
    data = {
        "name": ["mayur", "shyam", "dhanshayam"],
        "age": [12, 2323, 3224],
        "salary": [2500, 23000, 322]
    }
    
    return pd.DataFrame(data)

def load_large_dataset(file_path):
    """
    Load a larger dataset from a CSV file.
    
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

def display_statistical_summary(df, description="Dataset"):
    """
    Display statistical summary of a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
        description (str): Description of the dataset being analyzed
    """
    print("\n" + "="*70)
    print(f"{description} - Statistical Summary:")
    print("="*70)
    
    # Basic information
    print(f"\nShape: {df.shape} (rows, columns)")
    print(f"\nColumn Names: {', '.join(df.columns)}\n")
    
    # Display the first few rows
    print("First few rows:")
    print(df.head())
    
    # Display statistical summary
    print("\nStatistical Summary:")
    print(df.describe())
    
    # Additional statistics for non-numeric columns
    print("\nNon-numeric columns summary:")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"\nColumn: {col}")
        print(f"Unique values: {df[col].nunique()}")
        print(f"Top value: {df[col].mode().values[0]}")

def main():
    """Main function to demonstrate statistical summaries."""
    try:
        # Example 1: Small sample data
        print("Analyzing sample employee data...")
        employee_df = create_sample_dataframe()
        display_statistical_summary(employee_df, "Employee Sample Data")
        
        # Example 2: Larger dataset
        print("\n" + "="*120)
        print("Analyzing enterprise survey data...")
        survey_file = 'annual-enterprise-survey-2024-financial-year-provisional.csv'
        if os.path.exists(survey_file):
            survey_df = load_large_dataset(survey_file)
            display_statistical_summary(survey_df, "Enterprise Survey Data")
        else:
            print(f"\nNote: {survey_file} not found. Skipping large dataset example.")
            print("Make sure the file is in the same directory as this script.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
