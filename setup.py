from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ="-e ."
def get_requiremet(file_path:str)->List[str]:
    '''
    a function that returns requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sibaprasad',
author_email='sibap865@gmail.com',
packages=find_packages(),
install_requires=get_requiremet('requirements.txt')
)