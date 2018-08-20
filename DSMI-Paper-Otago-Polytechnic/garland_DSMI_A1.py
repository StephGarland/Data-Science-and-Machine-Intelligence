# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 08:05:17 2016

@author: Stephanie
"""
import pandas as pd
data = pd.read_csv('crime.csv', index_col=0)

import numpy as np
from sklearn.utils import shuffle
feature_cols = ['Education','Police','Income','Inequality']
target = ['Crime']
X = np.array(data[feature_cols])
y = np.array(data[target])
X, y = shuffle(X, y, random_state=1)

assignmentQuestion = ["1. Plot the Education predictor/feature variable against Crime (the predictor should be on the x axis and crime on the y axis).",
                      "2. Plot the Police predictor/feature variable against Crime",
                      "3. Plot the Income predictor/feature variable against Crime.",
                      "4. Plot the Inequality predictor/feature variable against Crime.",
                      "5. Is the education variable positively or negatively correlated with crime?",
                      "6. Is the police variable positively or negatively correlated with crime?",
                      "7. Split the data in 2 halves: training set and test set",
                      "8. Fit a multivariate linear regression model on the training data using all the features available",
                      "9. What are the intercept (θ0) and coefficients (θ1, θ2, θ3 and θ4) of the model?",
                      "10. What is the R2 score for the training data? and for the test data?",
                      "11. Given the following imaginary cities with the provided values for the predictors education, police, income and inequality, which city should have the highest level of crime according to your model?",
                      "12. Re-instantiate your linear regression model with the parameter fit_intercept set to False and rerun your analysis on the entire feature matrix X. Output the coefficients you get for θ1...θ4.]",
                      "13. Calculate the coefficients for θ1...θ4 using the analytical/close form solution of linear regression. Use the matrix algebra functionality provided by the numpy library to find the optimal vector θ."]
                       
featureLabel = ["Education: \n Mean years of schooling of population aged 25 years or over",
                "Police: \nPer capita expenditure on police protection",
                "Income: \nAverage per capita monthly income", 
                "Inequality: \nPercentage of families earning below half the median income"]
                
targetLabel = "Crime: \nNumber of offenses per 100,000 population"

import pylab as plt
#plots each feature individually against crime:
for i in range(0, len(X[0])): #iterate over each feature
    print("---------------------------------------------------")
    print(assignmentQuestion[i]) #print the assignment question
    plt.scatter(X[:,i], y) #plot the current feature against crime
    plt.xlabel(featureLabel[i]) #attach current feature's label
    plt.ylabel(targetLabel) #attach crime label
    plt.show()

print("---------------------------------------------------")
#5. Is the education variable positively or negatively correlated with crime?
print(assignmentQuestion[4]) 
print()
print("Education, as shown in the first graph, negatively correlates with crime.\nThat is, as education values increase, crime values decrease.")
print()
#6. Is the police variable positively or negatively correlated with crime?
print(assignmentQuestion[5]) 
print()
print("The police variable, as shown in the second graph, positively correlates with crime.\nThis means that as expenditure on police protection increased, so too did criminal offences.")

#7. Split the data in 2 halves: training set and test set"
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

#8. Fit a multivariate linear regression model on the training data using all the features available
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train);

print("---------------------------------------------------")
#9. What are the intercept (θ0θ0) and coefficients (θ1, θ2, θ3 and θ4) of the model?
print(assignmentQuestion[8]) 
print("\nIntercept: ", model.intercept_)
print("Coefficients: ", model.coef_)
print("---------------------------------------------------")
#10. What is the R2 score (i.e. the coefficient of determination that measures the proportion of the outcomes variation explained by the model) for the training data? and for the test data?
print(assignmentQuestion[9])
print("\nTraining data R2 = ", model.score(X_train, y_train))
print("Test data R2 = ", model.score(X_test, y_test))
print("---------------------------------------------------")
#11. Given the following imaginary cities with the provided values for the predictors education, police, income and inequality, which city should have the highest level of crime according to your model?
print(assignmentQuestion[10])
print()
X_pretendCities = [[10, 5, 6000, 16], #City 1
                   [8, 11, 4500, 25], #City 2
                   [6, 8, 3780, 17],  #City 3
                   [12, 6, 5634, 22]] #City 4
                   
print("Levels of crime in each given city:\n", model.predict(X_pretendCities))                
print("\nMy model predicts that City 2 would have the highest level of crime.")

print("---------------------------------------------------")
#12. Re-instantiate your linear regression model with the parameter fit_intercept set to False and rerun your analysis on the entire feature matrix X. 
    #Output the coefficients you get for θ1...θ4.
print(assignmentQuestion[11]) 
model_noIntercept = linear_model.LinearRegression(fit_intercept=False)
model_noIntercept.fit(X_train, y_train);
print("\nCoefficients: ", model_noIntercept.coef_)

print("---------------------------------------------------")
#13. Calculate the coefficients for θ1...θ4 using the analytical/close form solution of linear regression. Use the matrix algebra functionality provided by the numpy library to find the optimal vector θ.
print(assignmentQuestion[12])
print()
#Couldn't remember how to do this. Thought I was meant to figure out a least square model, but couldn't quite pull off how to do it.
"""
cf = np.linalg.lstsq(X_train.T.dot(x_train) + 1 * X_train.shape[1], X_train.T.dot(y_train))[0]
print("\nCoefficients: ",cf)
"""

















