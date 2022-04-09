from sklearn import datasets
import pandas as pd
import numpy as np

def get_iris() -> pd.DataFrame:
    """ """
    iris = datasets.load_iris()
    df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
    return df