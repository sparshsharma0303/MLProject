from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return list of requirements 
#     '''
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements

def get_requirements(file_path: str)-> List[str]:
    '''this function will return list of requirements'''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Sparsh',
    author_email = 'sparshsharma0303@gmail.com',
    packages = find_packages(),## auto detects all the packages, looks for folder with __init__ file
    install_requires = get_requirements('requirements.txt') 
)
