import os
import json
import logging
from joblib import load
import numpy as np
from sklearn.metrics import classification_report

data_path = os.path.join("..", "data")
model_path = os.path.join("..", "models")

X_raw = np.load(os.path.join(data_path, 'X_test.npy'))
y = np.load(os.path.join(data_path, 'y_test.npy'))

# Scale the features
scaler = load(os.path.join(model_path, "scaler.joblib"))
X = scaler.transform(X_raw)

# Load model
model = load(os.path.join(model_path, "model.joblib"))

# Predict test data
y_pred = model.predict(X)

# Generate classification report
print(classification_report(y_true=y, y_pred=y_pred))
