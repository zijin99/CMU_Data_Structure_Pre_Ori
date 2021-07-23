import numpy as np

data = np.loadtxt('10.in', dtype=np.int32, skiprows=1)
data = np.sort(data, axis=0)
record = np.zeros(data.shape[0], dtype=np.int32)
total_len, min_len, record[0] = [data[0][1] - data[0][0]]*3

for i in range(0, record.size-1):
    record[i+1] = data[i+1][1] - data[i+1][0]
    mini = np.minimum(record[i+1], data[i][1]-data[i+1][0])
    overlap = np.maximum(0, mini)
    record[i] -= overlap
    record[i+1] -= overlap
    total_len += record[i+1]
    min_len = np.minimum(min_len, record[i])

out = total_len - np.maximum(0,np.minimum(min_len,record[-1]))

with open('10.out', 'w') as f:
    f.write(str(out))
    f.close()