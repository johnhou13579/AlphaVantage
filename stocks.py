from alpha_vantage.timeseries import TimeSeries
# Your key here
key = 'I8TTHGPZJU2EPWDJ'
ts = TimeSeries(key)
aapl, meta = ts.get_daily(symbol='AAPL')
print(aapl['2020-02-19'])