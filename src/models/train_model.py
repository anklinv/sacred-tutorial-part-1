import os
import logging
from joblib import dump
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

data_path = os.path.join("..", "data")
model_path = os.path.join("..", "models")

X_raw = np.load(os.path.join(data_path, 'X_train.npy'))
y = np.load(os.path.join(data_path, 'y_train.npy'))

scaler = StandardScaler()
X = scaler.fit_transform(X_raw)

scaler_path = os.path.join(model_path, "scaler.joblib")
dump(scaler, scaler_path)

kernel = "linear"
gamma = 0.01
C = 0.002

model = SVC(kernel=kernel, gamma=gamma, C=C)
model.fit(X=X, y=y)

model_path = os.path.join(model_path, "model.joblib")
dump(model, model_path)