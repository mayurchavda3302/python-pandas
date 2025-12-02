

"""
This script demonstrates how to create a pandas DataFrame and save it to different file formats.
It shows basic data export functionality including CSV, Excel, and JSON formats.
"""

import pandas as pd

def create_sample_dataframe():
    """
    Creates a sample DataFrame with employee information.
    
    Returns:
        pd.DataFrame: A DataFrame containing sample employee data.
    """
    # Sample employee data as a dictionary
    employee_data = {
        "name": ['ram', 'shyam', 'dhanshaym'],
        "age": [10, 20, 30],
        "city": ['nagpur', 'jaipur', 'gujarat']
    }
    
    # Create DataFrame from the dictionary
    return pd.DataFrame(employee_data)

def save_dataframe_formats():
    """
    Demonstrates saving a DataFrame to different file formats.
    Saves the data in CSV, Excel, and JSON formats.
    """
    # Create sample data
    df = create_sample_dataframe()
    
    # Save to CSV format
    csv_file = 'output.csv'
    df.to_csv(csv_file, index=False)
    print(f"Data saved to {csv_file}")
    
    # Save to Excel format
    excel_file = 'output-ex.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")
    
    # Save to JSON format
    json_file = 'output-json.json'
    df.to_json(json_file, index=False)
    print(f"Data saved to {json_file}")

if __name__ == "__main__":
    save_dataframe_formats()
