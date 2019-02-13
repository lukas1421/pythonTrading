import tushare as ts
import datetime as dt

indices = ['sh000001', 'sh000016', 'sh000300', 'sz399006', 'sh000905', 'sz399001']

# indices = ['sh000001']
startDate = dt.datetime.now() + dt.timedelta(days=-3)
startDateStr = startDate.strftime('%Y-%m-%d')
endDate = dt.datetime.now() + dt.timedelta(days=+1)
endDateStr = endDate.strftime('%Y-%m-%d')
dateFormat = '%Y-%m-%d'


def get5mData():
    for index in indices:
        print('***********************', index)
        df = ts.get_hist_data(index, ktype='5', start=startDateStr, end=endDateStr)
        df['time'] = df.index
        df['time'] = df['time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        df1 = df[['time', 'open', 'high', 'low', 'close']].sort_values(['date'])
        date = df1['time'].dt.date.tail(1).values[0]
        df2 = df1[df1['time'].dt.date == date]

        pmOpen = df2['open'][df2['time'].dt.time > dt.time(12, 0, 0)].values[0]
        pmClose = df2['close'].tail(1).values[0]
        dayHigh = df2['high'].max()
        dayLow = df2['low'].min()

        print('index', index)
        print(list(
            [date.strftime(dateFormat), 'pmChg%', str(round((pmClose / pmOpen - 1) * 10000.0) / 100.0) + '%',
             'closingP', str(round(10000.0 * (pmClose - dayLow) / (dayHigh - dayLow)) / 100.0) + '%']))


def getDayData():
    for index in indices:
        df = ts.get_hist_data(index, ktype='D', start=startDateStr)
        df1 = df[['open', 'high', 'low', 'close']].sort_values(['date'])
        print('index', df1)


get5mData();
# getDayData();
