# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')

setup(
    name='deployer-lite-agent',
    version='0.0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    url='https://github.com/harnash/deployer-lite-agent',
    license='Apache 2.0',
    author='Łukasz Harasimowicz',
    author_email='dev@harnash.eu',
    description='',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Clustering',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',

        'License :: OSI Approved :: :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'deployer-agent = agent.commands:register',
        ],
    },
    tests_require=[
        'nose==1.3.7',
        'coverage==4.0b1',
    ],
    install_requires=[
        'pyzmq==14.7.0',
        'click==5.1',
    ]
)
