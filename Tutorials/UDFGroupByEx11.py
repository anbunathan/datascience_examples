import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
data = pd.read_csv('data/pokemon.csv')

# Plain python functions
def div(n):
    return n/2
data.HP.apply(div)

# Or we can use lambda function
data.HP.apply(lambda n : n/2)

# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()

#GroupBy
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
print(df)
print(df.groupby("treatment").mean())   # mean is aggregation / reduction method
print(df.groupby("treatment").age.max())
print(df.groupby("treatment")[["age","response"]].min())

print(df.info())
