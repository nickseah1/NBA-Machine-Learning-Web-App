# NBA Machine Learning Web App

Hello! This repository contains all of the files used to build the interactive NBA Machine Learning Web App. This application was built using Dash and was hosted using Heroku.

**View the app here:** https://nbamlapp.herokuapp.com/

This website contains 3 Applications

1) Predicting NBA All-Stars

This application predicts if a hypothetical player will be an NBA All-Star using a Random Forest Algorithm. We chose the Random Forest algorithm because it is a highly accurate algorithm and out performed the SVM Algorithm. The model was able to correctly predict if a player was an all-star with 97% Accuracy. This model could be improved by training the model with more data as the model was trained using NBA Player Data from 2017-2020. 



2) Predicting NBA Salary

This application predicts the expected percentage of an NBA Team's salary cap based on different statistics. We used a Linear Regression model for this as it outperformed the Random Forest Agorithm and achieved a mean squared error (MSE) of 0.0038. This model could be improved with a cleaner dataset. There were a large number of missing values that were mostly dropped but and some were filled using the mean. We could also try the XGBoost algorithm which has been known to be highly accurate for regression problems.

3) Visualize Diversity in the NBA

This application is an interactive graph that plots the total number of NBA players from a given country over time. The interactive graph was made using Plotly.



