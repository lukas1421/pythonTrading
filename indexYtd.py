import tushare as ts
import datetime as dt

indices = ['sh000001', 'sh000016', 'sh000300', 'sz399006', 'sh000905', 'sz399001']


# indices = ['sh000001']


def get5mData():
    for index in indices:
        print('***********************', index)
        df = ts.get_hist_data(index, ktype='5', start='2019-02-12')
        df1 = df[['open', 'high', 'low', 'close']].sort_values(['date'])
        df1['time'] = df1.index
        df1['time'] = df1['time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        pmOpen = df1['open'][df1['time'].dt.time > dt.time(12, 0, 0)].values[0]
        pmClose = df1['close'].tail(1).values[0]
        dayHigh = df1['high'].max()
        dayLow = df1['low'].min()
        date = df1['time'].dt.date.tail(1).values[0]

        print('index', index)
        print(list([date, 'pmChg%', str(round((pmClose / pmOpen - 1) * 10000.0) / 100.0) + '%', 'closingP',
                    str(round(10000.0 * (pmClose - dayLow) / (dayHigh - dayLow)) / 100.0) + '%']));

    def getDayData():
        for index in indices:
            df = ts.get_hist_data(index, ktype='D', start='2019-02-12')
            df1 = df[['open', 'high', 'low', 'close']].sort_values(['date'])
            print('index', df1)


get5mData();
# getDayData();
