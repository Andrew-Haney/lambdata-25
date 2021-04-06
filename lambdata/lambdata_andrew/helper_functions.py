import pandas as pd
import numpy as np

def null_count(df):
    print(df.isnull().value_counts().sum())
    
def train_test_split(df, train_size= 0.8, test_size= 0.2):
    train = df.drop(test)
    test = df.drop(train)
    return (df)