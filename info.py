"""
This script demonstrates how to get detailed information about a pandas DataFrame
using the info() method. It shows both basic and advanced usage with different data types.
"""

import pandas as pd
import numpy as np

def create_sample_dataframe():
    """
    Create a sample DataFrame with various data types to demonstrate info() functionality.
    
    Returns:
        pd.DataFrame: A DataFrame with different data types for demonstration.
    """
    data = {
        'name': ['ram', 'shyam', 'dhanshaym', 'sita', 'gita'],
        'age': [25, 30, 35, 28, 32],
        'city': ['nagpur', 'jaipur', 'gujarat', 'mumbai', 'delhi'],
        'salary': [50000.50, 75000.75, 90000.25, 60000.00, 85000.50],
        'join_date': pd.date_range('20230101', periods=5),
        'is_active': [True, True, False, True, False],
        'rating': pd.Series([4.5, 3.8, 4.2, 3.9, 4.1], dtype='float64'),
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
        'bonus': [1000, 1500, 2000, None, 1800]  # Include a None value to show null handling
    }
    
    return pd.DataFrame(data)

def display_dataframe_info(df, description="Dataset"):
    """
    Display comprehensive information about a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
        description (str): Description of the dataset being analyzed
    """
    print("\n" + "="*70)
    print(f"{description} - Detailed Information:")
    print("="*70)
    
    # Basic info using pandas' info()
    print("\nBasic Information (df.info()):")
    print("-" * 40)
    df.info()
    
    # Data types summary
    print("\n\nData Types Summary:")
    print("-" * 40)
    print(df.dtypes)
    
    # Memory usage
    print("\n\nMemory Usage:")
    print("-" * 40)
    print(f"Total memory usage: {df.memory_usage(deep=True).sum() / (1024 * 1024):.2f} MB")
    
    # Display first few rows
    print("\n\nFirst few rows:")
    print("-" * 40)
    print(df.head())

def main():
    """Main function to demonstrate DataFrame information methods."""
    try:
        # Create and display information about sample data
        print("Creating sample DataFrame...")
        sample_df = create_sample_dataframe()
        display_dataframe_info(sample_df, "Sample Employee Data")
        
        # Example with a larger dataset if available
        print("\n" + "="*120)
        print("Trying to load enterprise survey data...")
        survey_file = 'annual-enterprise-survey-2024-financial-year-provisional.csv'
        
        try:
            survey_df = pd.read_csv(survey_file)
            display_dataframe_info(survey_df, "Enterprise Survey Data")
        except FileNotFoundError:
            print(f"\nNote: {survey_file} not found. Skipping large dataset example.")
            print("Make sure the file is in the same directory as this script.")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()