import time
from sacred import Experiment
from sacred.run import Run
from sacred.observers import MongoObserver

ex = Experiment('configtest')
#ex.observers.append(MongoObserver('mongodb://mongo_user:mongo_password@localhost:27017/sacred?authSource=admin'))

@ex.config
def basic_config():
    a = 10  # You can comment like this

@ex.config
def advanced_config(a):
    foo = {
        'a_squared': a**2,
        'bar': 'my_string%d' % a
    }
    if a > 8:
        # You can also write it above
        e = a/2

@ex.automain
def main():
    # Either do this
    with open('config.json', mode='r') as f:
        print(f.read())
    ex.add_resource('config.json')

    # Or even easier this
    with ex.open_resource('config.json', mode='r') as f:
        print(f.read())

    ex.add_package_dependency('flake8', '3.7.9')
    