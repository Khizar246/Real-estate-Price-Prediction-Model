import pickle
import numpy as np
import json
import pandas as pd

with open('mk/banglore_home_prices_model.pickle', 'rb') as f:
    lr_clf = pickle.load(f)


f = open("mk/columns.json","r")
data = json.loads(f.read())


def predict_price(location,sqft,bath,bhk):
    x1 = np.zeros(len(data['data_columns']))
    loc_index = np.where(pd.Index(data['data_columns'])==location.lower())[0][0]
    x1[0] = sqft
    x1[1] = bath
    x1[2] = bhk
    if loc_index >= 0:
        x1[loc_index] = 1
    return lr_clf.predict([x1])[0]
