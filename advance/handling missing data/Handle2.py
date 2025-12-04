# in this we wii fill the  missing  values to   t

# we can use  .fillna(value,inplace=True)

# here our  value can be made the default for  all   the missing values
import pandas as pd

data={
    
    "age":[23434,34545445,34333,4344],
    "name":['mayur','jay','nit','has'],
    "performance_score":[85,None,43,33]
}

df=pd.DataFrame(data)
print(df)   
print()

# here we have used the fillna
# print(" we use  fillna:--")
# print()
# df.fillna(0,inplace=True)

# print(df)
# print()


# here that wii fill 0 in all but we can  do it by passing the   calulated value so we can get more perfect data Frame..

# print("mean:-",df['performance_score'].mean())
mean=df['performance_score'].mean()
print(mean)
df['performance_score']=df['performance_score'].fillna(mean)
print()
print(df)