#根据df某几列进行逻辑判断（横向比较）生成新列作为交易信号
def signal_ma(a,b):
    if a > b:
        return 1
    else:
        return 0

pk_df['temp'] = pk_df.apply(lambda x: signal_ma(x.ma5,x.ma10), axis = 1)

#对df纵向比较生成交易信号
#在df的index为时间列时，纵向处理为时间维度上的信号生成，横向处理为空间维度上的信号生成
