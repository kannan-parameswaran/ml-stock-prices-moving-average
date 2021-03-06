# **Moving average with Time Series in Python**

Simple very effective technique in time series, can be used for data preparation, visualization, smoothing, forecasting and making predictions.

In this project, we'll see how to use moving average technique for time series forecasting with Python using stock prices for Apple Inc.(AAPL).

### What You Will build
You will build a Python application that loads Apple Inc.(AAPL) stock prices from Quandl library, sort, filter, plot graphs and make stock prediction on historical dates.

### What You need

- A favorite text editor
- Python 3.7 or later
- You can also import the code straight into your IDE:
  - [Visual Studio Code](https://code.visualstudio.com) - Integrated development environment
  - [Jupyter Notebook](https://jupyter.org) - Interactive environment
  
### How to complete this project.
You can start from scratch and complete each step or you can bypass basic setup steps that are already familiar to you. Either way, you end up with complete code.

To start from scratch, move on to What are Moving Average or Smoothing Techniques?

To skip the basics, do the following:

[Download](https://codeload.github.com/kannan-parameswaran/ml-stock-prices-moving-average/zip/master) and unzip the source repository for this project, or clone it using Git: 
```
   git clone https://github.com/kannan-parameswaran/ml-stock-prices-moving-average.git**
```
cd into **ml-stock-prices-moving-average**

Jump ahead to Running this application

### What are Moving Average or Smoothing Techniques?
[Taking a moving average is a smoothing process](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc42.htm).

### Python code
Open python interpreter as below or use your preferred method
```
    $ python3.7
    Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
```

First we import the libraries we will use
```
    >>> import pandas as pd
    >>> from datetime import datetime
    >>> from numpy import mean
    >>> from sklearn.metrics import mean_squared_error
    >>> import matplotlib.pyplot as plt
    >>> 
```

```
    To be finished
```

### Running this application.
```bash
    $ python3.7 stock_prices_ma.py
```

### See Also

- [Moving Average](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc42.htm)
- [Python Documentation](https://docs.python.org/3/)
- [Quandl API Documentation](https://docs.quandl.co)

