# -*- coding: utf-8 -*-
import os
import logging
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_path = os.path.join("..", "data")
iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
np.save(os.path.join(data_path, "X_train.npy"), X_train)
np.save(os.path.join(data_path, "X_test.npy"), X_test)
np.save(os.path.join(data_path, "y_train.npy"), y_train)
np.save(os.path.join(data_path, "y_test.npy"), y_test)