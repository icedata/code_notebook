#使用gzip读取pkl格式的文件
import _pickle as cPickle
import gzip

with gzip.open(dire+"/"+filename+".pkl", 'rb', compresslevel=1) as file_object:
    raw_data = file_object.read()
data = cPickle.loads(raw_data)

#使用jupyter画图时，时间作为x轴进行的转化处理对比（测试版本python3.6.4）
date_list = ['20151202','20151203','20151204','20151207','20151208','20151209','20151210','20151211','20151214','20151215']
result = [1500,1200,1300,1400,1250,1490,1900,1400,1340,1520]

import pandas as pd
import numpy as np
format_dates1 = np.array([pd.to_datetime(d) for d in date_list]).tolist()

from datetime import datetime
format_dates2 = [datetime.strptime(d,'%Y%m%d') for d in date_list]

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(date_list,result)	#很坐标不会自动缩减，日期会叠起来
plt.plot(format_dates1,result)  #TypeError: float() argument must be a string or a number, not 'Timestamp'
plt.plot(format_dates2,result) #横坐标会自动缩减，日期可能叠起来，如果叠加，请对x标签进行旋转，加入代码：plt.xticks(rotation=50)
