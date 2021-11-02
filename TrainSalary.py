# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from joblib import dump




df = pd.read_csv("Cleandf.csv")

# Train Test Split

# Choosing the features in the model
X = df[['PTS','PER','TOV','WS','VORP']]
# Target Column ie what we want to predict
y = df['%SalaryCap']

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Create a LR pipeline
model1 = make_pipeline(StandardScaler(), LinearRegression())
model1.fit(X_train, y_train)
dump(model1, 'model/lr.joblib')

pred1 = model1.predict(X_test)

print("MSE:", metrics.mean_squared_error(y_test,pred1))
print("MAE:", metrics.mean_absolute_error(y_test, pred1))