from setuptools import find_packages,setup
from typing import List

HYPEN_EDOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function wil return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_EDOT in requirements:
            requirements.remove(HYPEN_EDOT)

    return requirements


setup (
   name="mlproject",
   author="Srikanta",
   author_email="sree.panigrahi@gmail.com",
   version="0.0.1" ,
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
   )
