from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="sensor_fault_detection"
VERSION="0.0.1"
AUTHOR="Linkan Kumar Sahu"
DESCRIPTION="A sensor based fault detection using machine learning approach."
REQUIREMENT_FILE="requirements.txt"
AUTHOR_EMAIL="sahulinkan7@gmail.com"

def get_requirements_list()->List[str]:
    '''
    file returns the list of requirement packages mentioned 
    in requirement.txt file

    '''
    with open(REQUIREMENT_FILE) as file:
        requirement_list=file.readlines()
        requirement_list=[ item.replace("\n","") for item in requirement_list]
        if "-e ." in requirement_list:
            requirement_list.remove('-e .')
    return requirement_list

setup(name=PROJECT_NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      description=DESCRIPTION,
      install_requires=get_requirements_list())
    #   requires=get_requirements_list()