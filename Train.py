import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import seaborn as sns

plt.style.use('classic')
from sklearn.model_selection import train_test_split

sns.set_style()
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from joblib import dump

# Read In Cleaned Dataset
df = pd.read_csv('Clean_df.csv')

# Train Test Split
X = df[['PPG', 'RPG', 'APG', 'SPG', 'BPG']]
# Target Column is all star since that is what we want to predict
y = df['Allstar']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

# Parameters

# Trees
n_estimators = [1, 10, 100, 1000]
# Features to consider
max_features = ['auto', 'sqrt', 'log2', None]
# Bootstrap or not
bootstrap = [True, False]

# Create a param grid
param_grid = {'n_estimators': n_estimators,
              'max_features': max_features,
              'bootstrap': bootstrap, }

grid = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)

clf = RandomForestClassifier(random_state=40).set_params(**grid.best_params_)
clf.fit(X_train, y_train)
dump(clf, 'model/rfclf.joblib')
y_pred = clf.predict(X_test)

#

print("RF Accuracy:", metrics.accuracy_score(y_test, y_pred))
