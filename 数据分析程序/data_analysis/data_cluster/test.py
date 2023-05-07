import numpy as np
import pandas as pd

a = [12.42,134.13,1349.52]
sse_values = list(map(int,a))
print(sse_values)


labels = [0,3,4,1,2,0,1,2]
labels = np.array(labels)
index = np.nonzero(labels==0)[0]
print(type(index))
print(index)

arr = np.arange(12).reshape(4,3)
print(arr)
mean = arr.mean(axis=0)
print(mean)

data1 = {"id":[1,2],"name":['张三','李四']}
data2 = {"id":[3,4],"name":['王五','黄6']}

data_df = pd.DataFrame(data1,columns=["id","name"])
data_df = data_df.set_index("id")

print(data_df)


