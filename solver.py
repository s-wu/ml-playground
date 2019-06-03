import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegressionCV
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

l = []
MAX_TRAIN = 100000  # The maximum number of training samples to use in the model. For performance purposes


def last_bit(ind):
    """Idea: look for correlations between consecutive bits.
    Returns the bit prior to the one we are trying to predict"""
    res = []
    if ind - 1 < 0:
        res.append(0.5)
    else:
        res.append(l[ind - 1])
    return res


feature_functions = [last_bit]  # Create feature functions that take a single variable ind and add them to this list


def get_features(ind):
    """Get features to predict the bit at index ind. Runs each of the functions listed in feature_functions"""
    features = []
    for func in feature_functions:
        features.extend(func(ind))
    return features


def get_predictions(X_pred, Y_pred, X_train, Y_train):
    model = LinearRegression()
    model.fit(X_train, Y_train)
    model_preds = model.predict(X_pred)

    res = []
    for pred in model_preds:
        # Guess bit 1 if the model produced a prediction greater than 0.5, and 0 otherwise.
        pr = 1 if pred > 0.5 else 0
        res.append(pr)
    return res


def answer(s):
    """The main function that is called by runner.py. You shouldn't need to change anything here"""
    global l
    l = []
    for c in s:
        l.append(ord(c) - ord('0'))

    X_pred = []
    Y_pred = []
    X_train = []
    Y_train = []

    for i in range(len(l)):
        if l[i] == 2:
            X_pred.append(get_features(i))
            Y_pred.append(l[i])
        elif len(X_train) < MAX_TRAIN:
            X_train.append(get_features(i))
            Y_train.append(l[i])

    preds = get_predictions(X_pred, Y_pred, X_train, Y_train)
    res = "".join(str(x) for x in preds)
    return res
