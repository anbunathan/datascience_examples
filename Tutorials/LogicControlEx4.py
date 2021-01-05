import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
data = pd.read_csv('data/pokemon.csv')

x = data['Defense']>200     # There are only 3 pokemons who have higher defense value than 200
print(data[x])

print(data[np.logical_and(data['Defense']>200, data['Attack']>100 )])

print(data[(data['Defense']>200) & (data['Attack']>100)])