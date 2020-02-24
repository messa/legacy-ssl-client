#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='legacy-ssl-client',
    version='0.0.2',
    description='Requests Session object configured for servers with historical SSL configuration',
    author='Petr Messner',
    author_email='petr.messner@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['doc', 'tests*']),
    install_requires=[])
