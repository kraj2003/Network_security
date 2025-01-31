"""
The setup.py file is a vital file in a Python project because it defines the project's metadata and dependencies. 
It also provides the command line interface for packaging tasks
"""

from setuptools import find_packages,setup

from typing import List

def get_requirements():
    '''
    this function will return list of requirments
    '''
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            # read line fron the file
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore the empty line
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file nit found")

print(get_requirements())

setup(
    name="Network_security",
    version="0.0.1",
    author="Khushi Rajpurohit",
    author_email="khushirajpurohit617@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements()
)