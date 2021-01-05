import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
data = pd.read_csv('data/pokemon.csv')

data= data.set_index("#")
data.head()
print(data["HP"][1])
print(data.HP[1])
print(data.loc[1,["HP"]])
print(data[["HP","Attack"]])

#INDEX OBJECTS AND LABELED DATA
# our index name is this:
print(data.index.name)
# lets change it
data.index.name = "index_name"
print(data.head())

# first copy of our data to data3 then change index
data3 = data.copy()
# lets make index start from 100. It is not remarkable change but it is just example
data3.index = range(100,900,1)
print(data3.head())

#HIERARCHICAL INDEXING
data1 = data.set_index(["Type 1","Type 2"])
print(data1.head(100))

#slicing
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

# Slicing and indexing series
print(data.loc[1:10,"HP":"Defense"])   # 10 and "Defense" are inclusive

# Reverse slicing
print(data.loc[10:1:-1,"HP":"Defense"])

# From something to end
print(data.loc[1:10,"Speed":])

#FILTERING DATA FRAMES
# Creating boolean series
boolean = data.HP > 200
print(data[boolean])

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
print(data[first_filter & second_filter])

# Filtering column based others
print(data.HP[data.Speed<15])