import tushare as ts

indices = ['sh000001', 'sh000016', 'sh000300', 'sz399006', 'sh000905', 'sz399001']


def get5mData():
    for index in indices:
        df = ts.get_hist_data(index, ktype='5', start='2019-01-01')
        df1 = df[['open', 'high', 'low', 'close']].sort_values(['date'])
        print("5m", index)
        df1.to_csv('/home/l/chinaData/' + index + "_5m.csv", mode='w', header='False')


def getDayData():
    for index in indices:
        df = ts.get_hist_data(index, ktype='D', start='2017-12-30')
        df1 = df[['open', 'high', 'low', 'close']].sort_values(['date'])
        print("get Day ", index)
        df1.to_csv('/home/l/chinaData/' + index + "_day.csv", mode='w', header='False')



get5mData();
getDayData();

