import pandas as pd
import numpy as np

class ImHelping:
    def __init__(self):
    
    
        def null_count(df):
            return df.isnull().sum().sum()
        
        def remove_hcc(df, cutoff= 50):
            hcc = [col for col in df.select_dtypes('object').columns
             if df[col].nunique() > cutoff]
            df.drop(columns= hcc, inplace= True)

if __name__ == "__main__":
        def train_test_split(df, train_size= 0.8):
            arr_rand = np.random.rand(X.shape[0])
            target = arr_rand < np.percentile(arr_rand, 80)

            X_train = X[target]
            y_train = y[target]
            X_test =  X[~target]
            y_test = y[~target]

            print (len(X_train), len(y_train), len(X_test), len(y_test))
            return (X_train, y_train, X_test, y_test)
        
        



### IN style_example.py FILE###

#what would you say if you were working with someone and this is the code they gave you?

import math
import sys

def exampl1():
  ### THIS IS A LONG COMMENT AND should be wrapped to fit within a 72 character limit
  some_tuple =(1, 2, 3, 'a')
  some_variable={
      "long":'LONG CODE LINES should be wrapped within 79 character to prevent page cutoff stuff', 
      'other':[math.pi, 100,200, 300, 9999292929292,"This IS a long string that looks gross and goes beyond what it should"], 
      "more": {"inner": "THIS whole logical line should be wrapped"},
      "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]}
    return (some_tuple, some_variable)
def example_2(): 
    return {"has_key() is deprecated": True}

class Example3(object):
    
    
    def __init__   (self, bar):
        
        if bar: bar+= 1: 
            bar=bar*bar
            return bar
        else:
            some_string = """INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented,THIS IS MORE CODE"""
            return (sys.path, some_string)