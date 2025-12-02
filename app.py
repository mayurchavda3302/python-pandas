import pandas as pd

# df=pd.read_csv('/home/mayur_chavda/python/pandas/annual-enterprise-survey-2024-financial-year-provisional.csv',encoding="utf-8")
df=pd.read_excel('/home/mayur_chavda/python/pandas/Financial Sample.xlsx')


"""
read_csv   :- read csv data if get error use   encoding utf-8 or latint 1.

read_excel:- read data from excel

read_json - read data from json

use gcsfs libray for the read data from  the cloud..

"""


print(df)