# setup.py

from setuptools import setup, find_packages

setup(
    name='simple_crud',
    version='1.0.0',
    author='Lindokuhle',
    author_email='lindokuhlerajuili@gmail.com',
    description='''A simple database package that creates a table, 
                   adds records in a table, 
                   deletes a record from a table and also updates info''',
    packages=find_packages(),
    
)
