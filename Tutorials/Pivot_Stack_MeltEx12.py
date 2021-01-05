import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
data = pd.read_csv('data/pokemon.csv')

dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
print(df)
print(df.pivot(index="treatment",columns = "gender",values="response"))

# STACKING and UNSTACKING DATAFRAME
df1 = df.set_index(["treatment","gender"])
print(df1)
print(df1.unstack(level=0))
print(df1.unstack(level=1))
df2 = df1.swaplevel(0,1)
print(df2)

#Melting
print(df)
print(pd.melt(df,id_vars="treatment",value_vars=["age","response"]))
