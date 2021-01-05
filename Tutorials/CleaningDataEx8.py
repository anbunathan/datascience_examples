import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
data = pd.read_csv('data/pokemon.csv')

print(data.head())  # head shows first 5 rows
print(data.tail())
print(data.columns)
print(data.shape)
print(data.info())

print(data['Type 1'].value_counts(dropna =False))  # if there are nan values that also
data.describe() #ignore null entries
data.boxplot(column='Attack',by = 'Legendary')

#Tidy Data
data_new = data.head()    # I only take 5 rows into new data
data_new
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
print(melted)

#pivot
print(melted.pivot(index = 'Name', columns = 'variable',values='value'))

#concatenate
data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
print(conc_data_row)

data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 0 : adds dataframes in row
print(conc_data_col)

#Data types
# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')

# As you can see Type 1 is converted from object to categorical
# And Speed ,s converted from int to float
print(data.dtypes)

#MISSING DATA and TESTING WITH ASSERT
# Lets look at does pokemon data have nan value
# As you can see there are 800 entries. However Type 2 has 414 non-null object so it has 386 null object.
print(data.info())

# Lets chech Type 2
print(data["Type 2"].value_counts(dropna =False))
# As you can see, there are 386 NAN value

# Lets drop nan values
data1=data   # also we will use data to fill missing value so I assign it to data1 variable
data1["Type 2"].dropna(inplace = True)  # inplace = True means we do not assign it to new variable. Changes automatically assigned to data
# So does it work ?
assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values
data["Type 2"].fillna('empty',inplace = True)
assert  data['Type 2'].notnull().all() # returns nothing because we do not have nan val


