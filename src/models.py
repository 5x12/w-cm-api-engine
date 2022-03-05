import pickle
import os

def prepare_predictions(features: list, model: str) -> list:
    filename = f'../models/{model}.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    preds = loaded_model.predict_proba([features])[:, 1]
    return preds