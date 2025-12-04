import pandas as pd



data = {
        'employee_id': [101, 102, 103, 104, 105, 106, 107],
        'name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David'],
        'age': [25, 28, 35, 32, 27, 31, 29],
        'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
        'salary': [45000, 68000, 72000, 65000, 48000, 75000, 70000],
        'is_manager': [False, True, True, False, False, True, False]
    }



df=pd.DataFrame(data)


# for drop the  column we use the df.drop


# syntax

#  here the inplace wii direclty update or delete from  our data frame.
# if we made it falst it wii  retun a new Frame...
# df.drop(column= ["columnname"],inplace=True)

print(df)
print()
print()
#  remove single column

# that wii remove the  is_manger colun from datta
df.drop(columns=["is_manager","salary"],inplace=True)

print(df)

#  if we need to create the new   data frame without those  columns we can do it like ...
# df2=df.drop(columns=["age"],inplace=False)

# print(df2)


