from xgboost import XGBClassifier
from  sklearn.model_selection import GridSearchCV

import os
import pickle


def run_xgboost(df, target):
    params = {
        'n_estimators': [10, 20, 30, 40, 50, 100, 250, 500, 1000],
        'max_depth': [1, 3, 5],
        'learning_rate': [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.08, 0.09, 0.1, 0.3, 0.5, 0.7, 1],
        'reg_alpha': [0, 0.001, 0.1, 0.5, 1, 2, 5],
        'reg_lambda': [0, 0.001, 0.1, 1, 2, 5],
        'n_jobs': [-1]

    }
    model = XGBClassifier()
    grid = GridSearchCV(estimator=model, param_grid=params, cv=5, verbose=3, scoring='accuracy')
    
    grid.fit(df, target)
    print(grid.best_params_)
    with open('Data/pickles/xgboost_model', 'wb') as file:
        pickle.dump(grid, file)
    
    

