"""
This script demonstrates various data selection and filtering techniques in pandas,
including column selection, row filtering, and combining multiple conditions.
"""

import pandas as pd

def create_sample_dataframe():
    """
    Create a sample DataFrame with employee data for demonstration.
    
    Returns:
        pd.DataFrame: A sample employee dataset
    """
    data = {
        'employee_id': [101, 102, 103, 104, 105, 106, 107],
        'name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David'],
        'age': [25, 28, 35, 32, 27, 31, 29],
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
        'salary': [45000, 68000, 72000, 65000, 48000, 75000, 70000],
        'join_date': pd.to_datetime(['2020-01-15', '2019-05-22', '2018-11-10', 
                                   '2021-02-05', '2022-03-18', '2019-08-30', '2020-07-12']),
        'is_manager': [False, True, True, False, False, True, False]
    }
    return pd.DataFrame(data)

def demonstrate_column_selection(df):
    """
    Demonstrate different ways to select columns in a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to work with
    """
    print("\n" + "="*70)
    print("COLUMN SELECTION EXAMPLES")
    print("="*70)
    
    # 1. Select a single column (returns Series)
    print("\n1. Selecting a single column (returns Series):")
    names = df['name']
    print(f"Type: {type(names)}\n{names}")
    
    # 2. Select multiple columns (returns DataFrame)
    print("\n2. Selecting multiple columns (returns DataFrame):")
    name_age = df[['name', 'age']]
    print(f"Type: {type(name_age)}\n{name_age}")
    
    # 3. Using dot notation (only works with valid Python identifiers)
    print("\n3. Using dot notation (for valid column names):")
    salaries = df.salary
    print(f"Type: {type(salaries)}\n{salaries}")

def demonstrate_row_filtering(df):
    """
    Demonstrate different ways to filter rows in a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to work with
    """
    print("\n" + "="*70)
    print("ROW FILTERING EXAMPLES")
    print("="*70)
    
    # 1. Simple condition
    print("\n1. Employees with salary > 50000:")
    high_earners = df[df['salary'] > 50000]
    print(high_earners[['name', 'salary']])
    
    # 2. Multiple conditions with & (AND)
    print("\n2. IT department employees with salary > 60000:")
    it_high_earners = df[(df['department'] == 'IT') & (df['salary'] > 60000)]
    print(it_high_earners[['name', 'department', 'salary']])
    
    # 3. Using | (OR) condition
    print("\n3. Employees in HR or Finance departments:")
    hr_finance = df[df['department'].isin(['HR', 'Finance'])]
    print(hr_finance[['name', 'department']])
    
    # 4. Using ~ (NOT) operator
    print("\n4. Employees who are not managers:")
    non_managers = df[~df['is_manager']]
    print(non_managers[['name', 'is_manager']])

def demonstrate_advanced_filtering(df):
    """
    Demonstrate more advanced filtering techniques.
    
    Args:
        df (pd.DataFrame): The DataFrame to work with
    """
    print("\n" + "="*70)
    print("ADVANCED FILTERING EXAMPLES")
    print("="*70)
    
    # 1. Using query() method
    print("\n1. Using query() method:")
    result = df.query('age > 30 and salary > 65000')
    print(result[['name', 'age', 'salary']])
    
    # 2. Using str methods for string filtering
    print("\n2. Using string methods (names starting with 'J' or 'A'):")
    name_filter = df[df['name'].str.startswith(('J', 'A'))]
    print(name_filter[['name']])
    
    # 3. Filtering by date
    print("\n3. Employees who joined before 2021:")
    before_2021 = df[df['join_date'] < '2021-01-01']
    print(before_2021[['name', 'join_date']])

def main():
    """Main function to demonstrate pandas selection and filtering."""
    try:
        # Create sample data
        print("Creating sample employee data...")
        df = create_sample_dataframe()
        
        # Display the complete dataset
        print("\nCOMPLETE DATASET:")
        print("-" * 70)
        print(df)
        
        # Demonstrate different techniques
        demonstrate_column_selection(df)
        demonstrate_row_filtering(df)
        demonstrate_advanced_filtering(df)
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()


print("filer multiple:-")


print(df[(df["salary"] > 2500) & (df["age"] > 12)])
