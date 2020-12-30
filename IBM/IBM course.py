import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)

url = "C:/Users/TN90072/Documents/Python Scripts/imports-85.data"
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

df1=df.replace('?',np.NaN)

mean = pd.to_numeric(df1['normalized-losses'], errors='coerce').mean()
df = df1['normalized-losses'].replace(np.NaN, mean)
df.head(20)


df['city-mpg'] = 235/df['city-mpg']
df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)

df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# normalization
df['length'] = df['length']/df['length'].max() # simple feature scaling
df['length'] = (df['length']-df['length'].min())/(df['length'].max()-df['length'].min()) # minmax method
df['length'] = (df['length']-df['length'].mean())/df['length'].std() #z-score method

# Binning
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["Low","Medium","High"]
df["price-binned"] = pd.cut(df["price"], bins,labels = group_names,include_lowest=True)
















































