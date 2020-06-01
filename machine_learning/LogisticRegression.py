from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score



import os
import pickle
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
warnings.filterwarnings('ignore')


def train(x_train, y_train):
    plt.clf()
    
    style.use('seaborn-poster')
    param_grid = {
        'penalty': ['l2', 'none'],
        'C': [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 10, 100],
        'fit_intercept': [True, False],
        'n_jobs': [-1]
    }

    grid = GridSearchCV(LogisticRegression(), param_grid, verbose=3, cv=5)

    grid.fit(x_train, y_train)

    with open('Data/pickles/logit_model', 'wb') as file:
        pickle.dump(grid, file)


def predict(x_test, y_test):
    style.use('seaborn-poster')
    with open('Data/pickles/logit_model', 'rb') as file:
        grid = pickle.load(file)

    print(grid.best_params_)

    model = grid.best_estimator_

    y_pred = model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    return confusion_matrix(y_test, y_pred)
