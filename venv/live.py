import tushare as ts


def getIndexLive():
    df = ts.get_realtime_quotes(['sh000001', 'sh000016', 'sh000300', 'sz399001', 'sz399006', 'sh000905'])
    df['Ret'] = ((df['price'].astype('float') / df['pre_close'].astype('float') - 1) * 100) \
        .apply(lambda x: round(x, 2))
    print(df.iloc[:, [0, 2, 3, 30, 31, 32, 33]])


getIndexLive()
