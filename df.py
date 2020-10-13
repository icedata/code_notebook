#根据df某几列进行逻辑判断（横向比较）生成新列作为交易信号
def signal_ma(a,b):
    if a > b:
        return 1
    else:
        return 0

pk_df['temp'] = pk_df.apply(lambda x: signal_ma(x.ma5,x.ma10), axis = 1)

#对df纵向比较生成交易信号
#在df的index为时间列时，纵向处理为时间维度上的信号生成，横向处理为空间维度上的信号生成

#20201013练习代码
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
s = pd.Series(np.random.rand(20)*100)
df = pd.DataFrame(np.random.rand(6,4)*100,columns = ['a','b','c','d'])

#结果为Series
df.a
#结果为DataFrame
df[['a']]

#均值及标准差计算
meani = s.rolling(n).mean()
stdi = s.rolling(n).std()
meanu = meani + 2*stdi
meanl = meani - 2*stdi

#绘图
s.plot()
meani.show()
meanu.show()
meanl.show()
plt.show()

#横向（空间）判断，返回结果
np.where((df.a > df.b),1,0)

#纵向（时间）计算
#移位
s.shift(n) 
#均值
s.rolling(n).mean()
#方差
s.rolling(n).std()
