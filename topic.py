import pandas as pd

data={
    "name":["mayur","shyam","dhanshayam"],
    "age":[12,2323,3224],
    "salary":[2500,23000,322]
}




df=pd.DataFrame(data)
"""

mainly use for large data to get the qulick data

"""
print("df.shape:",df.shape)
print("df.columns",df.columns)



