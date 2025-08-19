import pandas as pd
data = pd.read_csv('./KDDTrain+.csv', header=None)
print(data.shape)
print(data.head())