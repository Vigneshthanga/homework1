#!/usr/bin/python
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample
from sklearn.metrics import accuracy_score
import numpy as np
rows = []
fields = []

data = pd.read_csv("/Users/vigneshkumarthangarajan/Documents/255-Data-Mining/homework-1/file.txt")

data['Class'] = data['Class'].map({'malignant': 1, 'benign': 0})

#check the datatypes of all columns
print(data.dtypes)

#Drop the ID column
data = data.drop('Id', 1)

#Sampling the training data in 70% - Train, 30% - Test 
train=data.sample(frac=0.7,random_state=200)
test=data.drop(train.index)

# Separate majority and minority classes
train_maj = train[train.Class==0]
train_min = train[train.Class==1]

# Upsample minority class
train_minority_upsampled = resample(train_min,
                                 replace=True,     # sample with replacement
                                 n_samples=312,    # to match majority class
                                 random_state=200) # reproducible results

# Combine majority class with upsampled minority class
train_upsampled = pd.concat([train_maj, train_minority_upsampled])

# Display new class counts
print(train_upsampled['Class'].value_counts())

# Separate input features (X) and target variable (y)
y = train_upsampled.Class
X = train_upsampled.drop('Class', axis=1)

ty = test.Class
tx = test.drop('Class', axis=1)

clf_2 = LogisticRegression().fit(X, y)

pred_y_2 = clf_2.predict(tx)

#pred_y_2.Class.unique()
unique, counts = np.unique(pred_y_2, return_counts=True)
print(np.asarray((unique, counts)).T)

print(accuracy_score(ty, pred_y_2))

# Upsample minority class
train_majority_dsampled = resample(train_maj,
                                 replace=True,     # sample with replacement
                                 n_samples=166,    # to match majority class
                                 random_state=200) # reproducible results

# Combine majority class with upsampled minority class
train_dsampled = pd.concat([train_min, train_majority_dsampled])

# Display new class counts
print(train_dsampled['Class'].value_counts())

# Separate input features (X) and target variable (y)
y = train_dsampled.Class
X = train_dsampled.drop(['Marg.adhesion','Epith.c.size','Bare.nuclei','Bl.cromatin','Normal.nucleoli','Mitoses', 'Class'] , axis='columns')
tx = test.drop(['Marg.adhesion','Epith.c.size','Bare.nuclei','Bl.cromatin','Normal.nucleoli','Mitoses', 'Class'] , axis='columns')

clf_2 = LogisticRegression().fit(X, y)

pred_y_2 = clf_2.predict(tx)

unique, counts = np.unique(pred_y_2, return_counts=True)
print(np.asarray((unique, counts)).T)

print(accuracy_score(ty, pred_y_2))
