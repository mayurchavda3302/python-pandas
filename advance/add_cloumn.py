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



#  add new  column 


#  Sqauure braces df["colun name"]=some data
# here this wii add the new data at the end of the dic...
print(df)
df["bonus"]=df["salary"] * 0.1

print(df['bonus'])
print(df)


# we can use insert method for the  insert new data at the specife  index


# df.insert(loc,"Column",some_dataa)

df.insert(0,"id",[1,2,3,4,5,6,7])
print()
print()
print()
print()
print(df)
# print(df.info())
