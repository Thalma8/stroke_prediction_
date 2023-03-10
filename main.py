# -*- coding: utf-8 -*-
"""stroke Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vg8q9vCJOMWgrtIxrmPe5lszzmvoB6c_
"""

import pandas as pd

datafile = pd.read_csv('healthcare-dataset-stroke-data.csv')
print("the data looks like this")
print(datafile.head)
print("to see if there are some Null values")
print(datafile.isnull())
print("the data shape")
print(datafile.shape)
#
stroke = datafile[datafile["stroke"] == 1]
no_stroke = datafile[datafile["stroke"] == 0]
print('The shape of the model before reshaping is')
print("stroke - ", stroke.shape)
print("no stroke-", no_stroke.shape)

from sklearn.utils import resample

no_stroke = resample(no_stroke,
                     replace=True,
                     n_samples=len(stroke),
                     random_state=42)

print('The shape of the model after reshaping is')
print("stroke - ", stroke.shape)
print("no stroke-", no_stroke.shape)

datafile = pd.concat([stroke, no_stroke])
print('the general shape of entire final data is', datafile.shape)

datafile['gender'] = datafile['gender'].map({'Male': 0, 'Female': 1})

datafile['Residence_type'] = datafile['Residence_type'].map({'Rural': 0, 'Urban': 1})

datafile['ever_married'] = datafile['ever_married'].map({'No': 0, 'Yes': 1})

datafile['smoking_status'] = datafile['smoking_status'].map(
    {'formerly smoked': 2, 'smokes': 1, 'never smoked': 0, 'Unknown': 3})

print(datafile.head(20))

datafile.isnull().sum()

datafile = datafile.dropna()
datafile.isnull().sum()

datafile.shape

X = datafile[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'Residence_type', 'smoking_status']]

y = datafile.stroke

X.shape

y.shape

"""now thw model building stage"""

from sklearn.model_selection import train_test_split

x_train, x_cv, y_train, y_cv = train_test_split(X, y, test_size=0.2, random_state=10)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(max_depth=4, random_state=10)
model.fit(x_train, y_train)

"""checking accuracy on the validation set"""

from sklearn.metrics import accuracy_score

pred_cv = model.predict(x_cv)
accur_score = accuracy_score(y_cv, pred_cv)
print("the accuracy score on the validation set is", accur_score)
"""checking accuracy on the training set"""

pred_train = model.predict(x_train)
accu_score = accuracy_score(y_train, pred_train)
print("the accuracy on the training set", accu_score)

# saving the model
import pickle

pickle_out = open("classifier.pkl", mode="wb")
pickle.dump(model, pickle_out)
pickle_out.close()
print('The model has been created and saved successfully')
