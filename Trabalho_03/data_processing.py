import pandas as pd
import numpy as np
from sklearn.utils import shuffle

def get_data(file):
    df = pd.read_excel(file)
    df = df.dropna(axis=1)

    x = np.array(df['Entrada'], dtype= int)
    y = np.array(df['Saída'], dtype= int)

    return x, y

def normalize_and_shuffle(x,y):
    normalized_x = x/max(x)
    normalized_y = y/max(y)

    shuffled_x, shuffled_y = shuffle(normalized_x, normalized_y)

    return normalized_x, normalized_y, shuffled_x, shuffled_y