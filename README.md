sacred-tutorial-part-1
==============================

Tutorial part of the sacred workshop on simple iris dataset

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data               <- Data directory (not on GitHub)
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        └── models         <- Scripts to train models and then use trained models to make
            │                 predictions
            ├── predict_model.py
            └── train_model.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
