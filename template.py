# Create folder structure of the project
# Generic template for folder structure.
import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO , format='[%(asctime)s] : %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
            ".github/workflows/.gitkeep" , #Github won't allow you to make a empty folder, that's why we are making a .gitkeep(Can be any file) which is of no use in project.
            f"src/{project_name}/__init__.py",  #This folder will contain all components of this project.If i have to add/delete something , i'll do with this folder(src).
            f"src/{project_name}/components/__init__.py",
            # f"src/{project_name}/components/data_ingestion.py",
            # f"src/{project_name}/components/data_transformation.py",
            # f"src/{project_name}/components/model_tranier.py",
            # f"src/{project_name}/components/model_monitering.py",
            f"src/{project_name}/pipeline/__init__.py",
            # f"src/{project_name}/pipelines/training_pipeline.py",
            # f"src/{project_name}/pipelines/prediction_pipeline.py",
            # f"src/{project_name}/exception.py",
            # f"src/{project_name}/logger.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/constants/__init__.py",
            "main.py",
            "config/config.yaml",
            "dvc.yaml",
            "params.yaml",
            "app.py",
            "Dockerfile",
            "requirements.txt",
            "setup.py",
            "research/trials.ipynb",
            "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) #Windows uses '\' instead of '/',so we change this using pathlib library.
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f'{filename} already exists')