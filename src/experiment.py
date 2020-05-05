import os
from data.make_dataset import create_dataset
from models.train_model import train_svc
from models.predict_model import test_model
from sacred import Experiment
from sacred.observers import MongoObserver

ex = Experiment("iris")
ex.observers.append(MongoObserver('mongodb://mongo_user:mongo_password@localhost:27017/sacred?authSource=admin'))

@ex.config
def default():
    data_path = os.path.join("..", "data")  # Path of the data
    model_path = os.path.join("..", "models")  # Path of the saved model and results
    kernel = "linear"
    C = 2

@ex.command
def dataset(data_path: str):
    '''Generate dataset'''
    create_dataset(data_path, ex.add_artifact)

@ex.command
def test(data_path, model_path):
    '''Test Model'''
    results = test_model(data_path, model_path)
    ex.log_scalar('accuracy', value=results['accuracy'])
    ex.log_scalar('precision', value=results['weighted avg']['precision'])
    ex.log_scalar('recall', value=results['weighted avg']['recall'])
    ex.log_scalar('f1_score', value=results['weighted avg']['f1-score'])

@ex.automain
def train(data_path, model_path, kernel, C):
    '''Train SVC model'''
    train_svc(data_path, model_path, kernel, C)
    test()
