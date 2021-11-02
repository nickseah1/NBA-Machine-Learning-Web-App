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


# Load in the Data
df_20 = pd.read_csv('stats.csv',header = 1).drop(['RANK','TEAM','POS','AGE','GP','FTA','2PA','3PA'],axis = 1)
df_19 = pd.read_csv('2019-2020.csv',header = 1).drop(['RANK','TEAM','POS','AGE','GP','FTA','2PA','3PA'],axis = 1)
df_20.columns = ['Name','MPG','MIN%','USG%','TO%','FT%','2P%','3P%','eFG%','TS%','PPG','RPG','TRB%','APG','AST%','SPG','BPG','TOPG','VI','ORTG','DRTG']
df_19.columns = ['Name','MPG','MIN%','USG%','TO%','FT%','2P%','3P%','eFG%','TS%','PPG','RPG','TRB%','APG','AST%','SPG','BPG','TOPG','VI','ORTG','DRTG']

# Preprocessing
df_20.sort_values(['PPG','APG'],ascending= False)
df_20.dropna(subset = ['ORTG','DRTG','eFG%','TO%','TS%'], inplace = True)
df_19.sort_values(['PPG','APG'],ascending= False)
df_19.dropna(subset = ['ORTG','DRTG','eFG%','TO%','TS%'], inplace = True)

df_20 = df_20.groupby('Name',as_index=False).agg(np.mean)

# List with all stars
all_stars_20 =['Kevin Durant','Bradley Beal','Kyrie Irving','Kawhi Leonard','Jayson Tatum','Zion Williamson','Mike Conley','James Harden','Zach LaVine','Donovan Mitchell','Julius Randle','Nikola Vucevic','Devin Booker','Anthony Davis','Joel Embiid','LeBron James','Giannis Antetokounmpo','Stephen Curry','Luka Doncic','Nikola Jokic','Jaylen Brown','Paul George','Rudy Gobert','Damian Lillard','Domantas Sabonis','Chris Paul','Ben Simmons']
all_stars_19 = ['Kemba Walker','Trae Young','Giannis Antetokounmpo', 'Pascal Siakam','Joel Embiid','Kyle Lowry','Ben Simmons','Jimmy Butler','Khris Middleton','Bam Adebayo','Jayson Tatum','Domantas Sabonis','James Harden','Luka Doncic','LeBron James','Kawhi Leonard','Anthony Davis','Chris Paul','Russell Westbrook','Damian Lillard','Donovan Mitchell','Brandon Ingram', 'Nikola Jokic','Rudy Gobert','Devin Booker']
# Creating an All star Column
df_20['Allstar'] = df_20.apply(lambda x: x['Name'] in all_stars_20, axis = 1)
df_19['Allstar'] = df_19.apply(lambda x: x['Name'] in all_stars_19, axis = 1)

# Encoding target column, 1 = all star 0 = not
df_20['Allstar'] = df_20['Allstar'].astype(int)
df_19['Allstar'] = df_19['Allstar'].astype(int)


# Initial Guess at most important features
X = df_20[['PPG','RPG','APG','eFG%','ORTG','DRTG']]
# Target Column is all star since that is what we want to predict
y = df_20['Allstar']

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 42,test_size = 0.3)

# Parameters

# Trees
n_estimators = [1,50,1000]
# Features to consider
max_features = ['auto', 'sqrt', 'log2', None]
# Bootstrap or not
bootstrap = [True, False]
# Random State
random_state = [1, 40, 500]

# Create a param grid
param_grid = {'n_estimators':n_estimators,
              'max_features':max_features,
              'bootstrap':bootstrap,
             'random_state': random_state}

grid = GridSearchCV(estimator = RandomForestClassifier(),param_grid = param_grid, cv = 3, n_jobs = -1, scoring = 'accuracy')
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)

clf=RandomForestClassifier(random_state = 40).set_params(**grid.best_params_)
clf.fit(X_train,y_train)
