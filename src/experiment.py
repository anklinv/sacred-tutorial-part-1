import os
from data.make_dataset import create_dataset
from models.train_model import train_svc
from models.predict_model import test_model
from sacred import Experiment

ex = Experiment("iris")

@ex.config
def default():
    data_path = os.path.join("..", "data")  # Path of the data
    model_path = os.path.join("..", "models")  # Path of the saved model and results
    kernel = "linear"
    C = 2

@ex.command
def create_dataset(data_path: str):
    '''Generate dataset'''
    create_dataset(data_path, ex.add_artifact)

@ex.command
def test(data_path, model_path):
    '''Test Model'''
    results = test_model(data_path, model_path)
    ex.add_config(accuracy=results['accuracy'],
                  precision=results['weighted avg']['precision'],
                  recall=results['weighted avg']['recall'],
                  f1_score=results['weighted avg']['f1-score']
                 )

@ex.automain
def train(data_path, model_path, kernel, C):
    '''Train SVC model'''
    train_svc(data_path, model_path, kernel, C)
