from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score

import os
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style


def train(x_train, y_train):
    param_grid = {

        'C': [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50, 70, 100],
        'gamma': ['scale', 'auto'],
        'kernel': ['rbf', 'poly', 'sigmoid'],
        'degree': [1, 2, 3, 4, 5],

    }

    grid = GridSearchCV(SVC(), param_grid=param_grid, verbose=3, cv=5)

    grid.fit(x_train, y_train)

    with open('Data/pickles/svc', 'wb') as file:
        pickle.dump(grid, file)


def predict(x_test, y_test):
    with open('Data/pickles/svc', 'rb') as file:
        grid = pickle.load(file)

    model = grid.best_estimator_

    y_pred = model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    return confusion_matrix(y_test, y_pred)