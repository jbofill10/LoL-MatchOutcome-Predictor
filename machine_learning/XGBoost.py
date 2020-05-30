from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score

import os
import pickle


def run_xgboost(x_train, y_train, x_test, y_test):
    if not os.path.isfile('Data/pickles/xgboost_model'):
        params = {
            'n_estimators': [10, 20, 50, 100, 250, 500, 1000],
            'max_depth': [1, 3, 5],
            'learning_rate': [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.08, 0.09, 0.1],
            'reg_alpha': [0, 0.001, 0.1, 0.5, 1],
            'reg_lambda': [0, 0.001, 0.1, 1],
            'n_jobs': [-1]

        }

        model = XGBClassifier(tree_method='gpu_hist')
        grid = GridSearchCV(estimator=model, param_grid=params, cv=5, verbose=3, scoring='accuracy')

        grid.fit(x_train, y_train)
        print(grid.best_params_)
        with open('Data/pickles/xgboost_model', 'wb') as file:
            pickle.dump(grid, file)
    else:
        with open('Data/pickles/xgboost_model', 'rb') as file:
            grid = pickle.load(file)
    
    model = grid.best_estimator_

    y_pred = model.predict(x_test)

    print(confusion_matrix(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

