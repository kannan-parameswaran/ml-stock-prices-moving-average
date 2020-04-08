#import packages
import pandas as pd
from datetime import datetime
from numpy import mean
import matplotlib.pyplot as plt

# to plot within jupyter notebook
#%matplotlib inline

# Quandl API Key
api_key = ''

# ticker, Quandl database and dataset
ticker = 'AAPL'
database_code = 'WIKI'
dataset_code = database_code + '/' + ticker

# mode for dataset file is taken from 'local' or Quandl API on 'internet'
mode = 'local'
#mode = 'internet'

# date range
start_date = datetime(2018, 1, 2)
end_date = datetime(2018, 1, 31)

# uncomment this for getting all avalibale dataset
#start_date = ''
#end_date = ''

# read and load the metadata to get information about the dataset
url_metadata = 'https://www.quandl.com/api/v3/datasets/' + dataset_code + '/metadata.json'
try:
	stock_metadata = pd.read_json(url_metadata)
except Exception as e:
	print('Error in reading', url_metadata)
	print(e)
	exit(-1)

# read and load the dataset file
if mode == 'internet':
	if start_date and end_date:
	# Quandl API FREE url for date range dataset available
		url_dataset = 'https://www.quandl.com/api/v3/datasets/' + dataset_code + '.csv?column_index=11&order=asc&start_date=' + start_date.strftime('%Y-%m-%d') + '&end_date=' + end_date.strftime('%Y-%m-%d')
	else:
	# Quandl API FREE url for complete dataset available
		url_dataset = 'https://www.quandl.com/api/v3/datasets/' + dataset_code + '.csv?column_index=11&order=asc'
else:
	# local dataset file
	url_dataset = 'data/' + database_code + '-' + ticker + '.csv'

try:
	df = pd.read_csv(url_dataset,header=0, index_col=0, usecols=['Date','Adj. Close'])
except Exception as e:
	print('Error in reading', url_dataset)
	print(e)
	exit(-1)
	
# reset column index
df = df.reset_index()

#setting index as date
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']

if mode == 'local':
	# sorting
	df = df.sort_index(ascending=True, axis=0)
	#filter data to a small set
	df = df.loc[start_date.strftime('%Y-%m-%d') : end_date.strftime('%Y-%m-%d')]

# set dates to the available from dataset
start_date = df['Date'][0]
end_date = df['Date'][-1]

# construct title from metadata
title = stock_metadata.dataset['name'] + ' ( ' + start_date.strftime('%m/%d/%Y') + ' - ' + end_date.strftime('%m/%d/%Y') + ' )'

# print
print('Total rows : ', df.size)
print('Columns    : ', df.columns)
print(df.head(10))

# plot dataset
plt.figure(figsize=(16,8))
plt.title(title)
plt.plot(df['Adj. Close'], label='Adj. Close Price')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()

# moving average
rolling_mean = df['Adj. Close'].rolling(window=3).mean()
print(rolling_mean.head(10))

# plot moving average
plt.figure(figsize=(16,8))
plt.title(title + ' - Moving Average' )
plt.plot(rolling_mean, label='Moving Average Price')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()

# making prediction

# convert pandas dataframe to numpy.ndarray
stock_data_ndarray = df.values

# moving average from 3 historical data
window = 3

# test data
test_data_ndarray = stock_data_ndarray[:len(stock_data_ndarray)]
predictions_list = list()
error_squareds_list = list()

# analyze steps in test_data_ndarray

#print the header
print('%12s %9s %11s %5s %12s' % ('Date', 'Predicted', 'Observation', 'Error','Error squared'))
print('-' * 58)

for t in range(len(test_data_ndarray)):
	if (t < window - 1 ):
		print('%12s %9s %11.2f %5s %13s' % (test_data_ndarray[t,0].strftime('%Y-%m-%d') , 'NaN', test_data_ndarray[t,1], 'NaN', 'NaN'))
	else:
		ma = mean(test_data_ndarray[(t+1)-window:(t+1),1])
		predictions_list.append(ma)
		es = (test_data_ndarray[t,1] - ma) ** 2
		error_squareds_list.append(es)
		print('%12s %9.2f %11.2f %5.2f %13.2f' % (test_data_ndarray[t,0].strftime('%Y-%m-%d') , ma, test_data_ndarray[t,1], (test_data_ndarray[t,1] - ma), es ))

# print summary
print('Summary' + '-' * 13)
print('Test Mean : %7.3f' % mean(test_data_ndarray[2:,1]))
print('Test SSE  : %7.3f' % sum(error_squareds_list))
print('Test MSE  : %7.3f' % (sum(error_squareds_list) / len(error_squareds_list)))
print('-' * 20)

# plot the obervation and predicted
plt.figure(figsize=(16,8))
plt.title(title)
plt.plot(test_data_ndarray[:,0], test_data_ndarray[:,1], label='Adj. Close')
plt.plot(test_data_ndarray[2:,0], predictions_list,label='Mean Average Price', color='red')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()


