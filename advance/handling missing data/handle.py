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


# we can use df.dropna  methode 
# if our  column is   not importnat than we can  use  this method

# it wii remove the colum from our dataFrame.

df.dropna(inplace=True)
print(df)



