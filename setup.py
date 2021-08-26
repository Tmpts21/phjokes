# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()  

VERSION = "0.0.1"  

setup(
    name='phjokes',
    version=VERSION,
    description='A python package that generates pinoy jokes  ',
    long_description=README ,  
    author='Ian Vincent A. Tampos ',
    author_email='mivatampos@tip.edu.ph', 
    url='https://github.com/Tmpts21/phjokes',
    license='MIT',
    packages=find_packages(),
    keywords=['jokes' , 'filipino' , 'pinoy' , 'tagalog' , 'bisaya'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
