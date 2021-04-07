import pandas as pd
import numpy as np

class ImHelping(self, df):
    def null_count(col):
    return col.isnull().value_counts().sum()


    def train_test_split(df, train_size= 0.8):
    arr_rand = np.random.rand(X.shape[0])
    target = arr_rand < np.percentile(arr_rand, 80)

    X_train = X[target]
    y_train = y[target]
    X_test =  X[~target]
    y_test = y[~target]

    # print (len(X_Train), len(y_Train), len(X_Test), len(y_Test))
    return (X_train, y_train, X_test, y_test)