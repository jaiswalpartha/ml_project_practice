from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="pj"
DESCRIPTION="Project Demo"
PACKAGES=find_packages()
REQUIREMENTS_FILE = "requirements.txt"

def get_install_requires()->List[str]:
    with open(REQUIREMENTS_FILE) as requirement_file_list:
        return [line for line in requirement_file_list.readlines() if line != "-e .\n"]
    
    


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
INSTALL_REQUIRES = get_install_requires()
)
