from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score

import os
import pickle


def train(x_train, y_train):
    param_grid = {
        'n_estimators': [10, 50, 100, 300, 500],
        'max_depth': [1, 3, 5],
        'bootstrap': [True, False],
        'max_features': ['auto', 'sqrt'],
        'min_samples_leaf': [1, 2, 4],
        'min_samples_split': [2, 5, 10],
        'oob_score': [True, False]
    }

    grid = GridSearchCV(RandomForestClassifier(), param_grid, verbose=3, cv=5)

    grid.fit(x_train, y_train)

    with open('Data/pickles/rf', 'wb') as file:
        pickle.dump(grid, file)


def predict(x_test, y_test):
    with open('Data/pickles/rf', 'rb') as file:
        grid = pickle.load(file)

    print(grid.best_params_)

    model = grid.best_estimator_

    y_pred = model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))