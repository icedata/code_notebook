#使用gzip读取pkl格式的文件
import _pickle as cPickle
import gzip

with gzip.open(dire+"/"+filename+".pkl", 'rb', compresslevel=1) as file_object:
    raw_data = file_object.read()
data = cPickle.loads(raw_data)
