#import packages

import pandas as pd
from datetime import datetime

from numpy import mean
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

# to plot within jupyter notebook
#%matplotlib inline

# date range
start_date = datetime(2017, 1, 1)
end_date = datetime(2017, 1, 10)

# read the file

# Quandl API FREE url for complete dataset available
url_complete='https://www.quandl.com/api/v3/datasets/WIKI/AAPL/data.csv'

# Quandl API FREE url for date range dataset available
url_date_range = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv?column_index=11&order=asc&start_date=' + start_date.strftime('%Y-%m-%d') + '&end_date=' + end_date.strftime('%Y-%m-%d')

# local dataset file
url_local = 'data/WIKI-AAPL.csv'

# load dataset file
df = pd.read_csv(url_date_range,header=0, index_col=0, usecols=['Date','Adj. Close'])

# sorting
#df = df.sort_index(ascending=True, axis=0)

#filter data to a small set
#df = df.loc[start_date.strftime('%Y-%m-%d') : end_date.strftime('%Y-%m-%d')]

# print
print('Total rows : ', df.size)
print('Columns    : ', df.columns)
print(df.head(10))

# plot original dataset
plt.figure(figsize=(10,10))
plt.title('Apple Inc.)AAPL) Stock Price ' + start_date.strftime('%m/%d/%Y') + ' - ' + end_date.strftime('%m/%d/%Y') )
plt.plot(df.index, df['Adj. Close'])
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()

# rolling mean
rolling_mean = df.rolling(window=3).mean()
print(rolling_mean.head(10))

# plot rolling mean
plt.figure(figsize=(10,10))
plt.title('Apple Inc.)AAPL) Stock Price ( Rolling Mean ) ' + start_date.strftime('%m/%d/%Y') + ' - ' + end_date.strftime('%m/%d/%Y') )
plt.plot(rolling_mean.index, rolling_mean['Adj. Close'])
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()

