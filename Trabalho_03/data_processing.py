import pandas as pd
from msilib.schema import Feature
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.utils import shuffle

def get_data(file):
    df = pd.read_excel(file)
    df = df.dropna(axis=1)

    x = np.array(df['Entrada'], dtype= int)
    y = np.array(df['Saída'], dtype= int)

    return x, y

def normalize_and_shuffle(x,y):
    # x_scaler = MinMaxScaler(feature_range=(0,1))
    # y_scaler = MinMaxScaler(feature_range=(0,1))

    # normalized_x = x_scaler.fit_transform(x.reshape(-1,1))
    # normalized_y = y_scaler.fit_transform(y.reshape(-1,1))

    normalized_x = x/max(x)
    normalized_y = y/max(y)

    shuffled_x, shuffled_y = shuffle(normalized_x, normalized_y)

    return normalized_x, normalized_y, shuffled_x, shuffled_y