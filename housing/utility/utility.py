import yaml
from housing.exception import HousingException
import os

def read_yaml_file(file_path:str)->dict:
    """
    Reads YAML file and returns its contents as dict.
    file_path: string
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e) from e