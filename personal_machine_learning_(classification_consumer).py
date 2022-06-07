# -*- coding: utf-8 -*-
"""Personal: Machine Learning (Classification: Consumer).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aln5blD5hofYqgm9Ql2OMuxolY4Q86b3
"""

# Binary Classification of Consumption Prediction
# Classifiers Tested: Logistic Regression, Random Forest, Support Vector Machine
# Highest Accuracy: 95%, Random Forest

# Installations
import csv
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from os import XATTR_REPLACE
# Data Manipulation
# Data: https://www.kaggle.com/datasets/jahnveenarang/cvdcvd-vd
# Data Columns:
  # 0: User ID (ID actually does make a difference, so include)
  # 1: Gender (0 = male, 1 = female)
  # 2: Age (years)
  # 3: Estimated Salary
  # 4: Purchased (0 = did not click, 1 = did click)

data = open("//content//drive//MyDrive//Coding//Personal Projects//3: Machine Learning//Resources//ConsumptionPrediction.csv")
csvreader = csv.reader(data)

x = []
y = []

header = True
for row in csvreader:
  if header:
    header = False
    continue
  else:
    input_values = []
    input_values.append(row[0])
    if row[1] == "Male":
      input_values.append(0)
    else:
      input_values.append(1)
    input_values.append(row[2])
    input_values.append(row[3])
    x.append(input_values)
    y.append(row[4])

standardizer = StandardScaler()
x = standardizer.fit_transform(x)

# Test Model: Logistic Regression
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size = 0.2, random_state = 0)
model = LogisticRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

cm = confusion_matrix(y_test, predictions)
TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()
accuracy =  (TP+TN) /(TP+FP+TN+FN)
accuracy = accuracy * 100
print("Accuracy:", accuracy, "%")

# Test Model: Random Forest
model = RandomForestClassifier(n_estimators = 60, random_state = 0)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

cm = confusion_matrix(y_test, predictions)
TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()
accuracy =  (TP+TN) /(TP+FP+TN+FN)
accuracy = accuracy * 100
print("Accuracy:", accuracy, "%")

# Test Model: Support Vector Machine
model = svm.LinearSVC()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

cm = confusion_matrix(y_test, predictions)
TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()
accuracy =  (TP+TN) /(TP+FP+TN+FN)
accuracy = accuracy * 100
print("Accuracy:", accuracy, "%")