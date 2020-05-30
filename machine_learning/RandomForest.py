from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score

import os
import pickle


def run_rf(x_train, y_train, x_test, y_test):
    param_grid = {
        'n_estimators': [10, 50, 100, 300, 500, 700, 1000, 1500, 2000],
        'max_depth': [1, 3, 5],
        'bootstrap': [True, False],
        'max_features': ['auto', 'sqrt'],
        'min_samples_leaf': [1, 2, 4],
        'min_samples_split': [2, 5, 10],
        'oob_score': [True, False]
    }

    grid = GridSearchCV(RandomForestClassifier(), param_grid, verbose=3, cv=5)

    grid.fit(x_train, y_train)

    with open('Data/pickles/logit_model', 'wb') as file:
        pickle.dump(grid, file)