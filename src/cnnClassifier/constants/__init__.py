'''
 We created this folder because we need to read yaml files.
 This project consists of 2 YAML files:
 1.config.yaml
 2.params.yaml

 We will use paths(Remains unchanged throught the project) to 
 read these files.Those paths are provided here.
 
 '''
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml") 
