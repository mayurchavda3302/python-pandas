import pandas as pd



data = {
        'employee_id': [101, 102, 103, 104, 105, 106, 107],
        'name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David'],
        'age': [25, 28, 35, 32, 27, 31, 29],
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
        'salary': [45000, 68000, 72000, 65000, 48000, 75000, 70000],
        'is_manager': [False, True, True, False, False, True, False]
    }



df=pd.read_excel('/home/mayur_chavda/python/pandas/advance/Financial Sample.xlsx')
# df=pd.DataFrame()
print("old  data frame")
print(df.head())


#   we use the .loc[]   for update the value
# df.lock[row_index,"column_name"]= new_value

df.loc[0,"Country"]="india"

print("new  data frame")
print(df.head())


print()




print("update all the country name to india")

df['Country']="india"
print(df.head())


print("last 5 data :---")
print(df.tail())


