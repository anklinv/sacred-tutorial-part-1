# -*- coding: utf-8 -*-
import os
import logging
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

def save_data(data, path, add_to_sacred):
    np.save(path, data)
    add_to_sacred(path)

def create_dataset(data_path, add_to_sacred):
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
    save_data(X_train, os.path.join(data_path, "X_train.npy"), add_to_sacred)
    save_data(X_test, os.path.join(data_path, "X_test.npy"), add_to_sacred)
    save_data(y_train, os.path.join(data_path, "y_train.npy"), add_to_sacred)
    save_data(y_test, os.path.join(data_path, "y_test.npy"), add_to_sacred)
