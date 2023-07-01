import os
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name = "Template maker"

list_of_files = [
    ".github/workflows/.gitkeep",
    # "src/__init__.py",

    # "src/components/__init__.py",
    # "src/components/data_ingestion.py",
    # "src/components/data_transformation.py",
    # "src/components/model_trainer.py",

    # "src/pipeline/__init__.py",
    # "src/pipeline/predict_pipeline.py",
    # "src/pipeline/train_pipeline.py",

    "exception.py",
    "logger.py",

    # "src/utils.py",

    # "src/config/__init__.py",
    # "src/config/configuration.py",

    "notebook/data",
    "notebook/EDA.ipynb",
    "notebook/model_training.ipynb",

    "requirements.txt",
    # "research/trials.ipynb",

    "templates/index.html",
    "templates/home.html",

    "setup.py",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")