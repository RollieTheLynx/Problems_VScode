import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)

url = "imports-85.data"
df = pd.read_csv(url, header=None)

df.head(5)

headers = ['symboling', 'normalized-losses', 'make', 'fuel', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 
           'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 
           'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 
           'highway-mpg', 'price']
df.columns = headers

df.dtypes  # check data types

df.describe()  # None (default) : The result will include all numeric columns.
df.describe(include='all')

df.info()

df['normalized-losses'].replace('?', np.nan)
mean = df['normalized-losses'].mean()
df['normalized-losses'].replace(np.nan, mean)

df['city-mpg'] = 235/df['city-mpg']
df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)

df['price'].replace('?', np.nan)
df.dropna(subset=['price'], axis=0, inplace=True)
df['price'] = df['price'].astype('int')
