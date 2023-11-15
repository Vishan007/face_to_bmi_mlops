from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """This function will return requirements list for running the python package
    
    Args:
        file_path (str): path of the requirements.txt file

    Returns:
        List[str]: list of packages to be installed
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n",'') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name = "fact-to-BMI",
    version = "0.0.1",
    author='Vishal Gaikwad',
    packages= find_packages(),
    install_requires = get_requirements('./requirements.txt')
)

