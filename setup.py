from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='sensor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    author="Amartya Vishwakarma",
)