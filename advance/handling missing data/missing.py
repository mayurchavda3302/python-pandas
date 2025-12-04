import pandas as pd



data={
    "age":[23434,34545445,34333,4344],
    "name":['mayur','jay','nit','has'],
    "perfomance_score":[85,None,43,33]
}


df=pd.DataFrame(data)
print(df)

print()
print()

print(df.isnull())

''''


# Output:-
     age   name  perfomance_score
0  False  False             False
1  False  False              True
2  False  False             False
3  False  False             False


Here in the True data is misssig
'''




# it wii return the missing vales count by the column names
print(df.isnull().sum())

'''
out put:-

age                 0
name                0
perfomance_score    1
dtype: int64
'''

print()


    
