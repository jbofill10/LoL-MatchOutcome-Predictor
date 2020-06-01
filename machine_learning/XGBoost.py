from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score


import os
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style


def train(x_train, y_train):
    params = {
        'n_estimators': [500],
        'max_depth': [1, 3, 5],
        'learning_rate': [0.09],
        'reg_alpha': [0],
        'reg_lambda': [0],
        'n_jobs': [-1]

    }

    model = XGBClassifier(tree_method='gpu_hist')
    grid = GridSearchCV(estimator=model, param_grid=params, cv=5, verbose=3, scoring='accuracy')

    grid.fit(x_train, y_train)

    with open('Data/pickles/xgboost_model', 'wb') as file:
        pickle.dump(grid, file)


def predict(x_test, y_test):
    with open('Data/pickles/xgboost_model', 'rb') as file:
        grid = pickle.load(file)

    model = grid.best_estimator_

    y_pred = model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    return confusion_matrix(y_test, y_pred)