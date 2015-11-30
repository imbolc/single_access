#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages


def read(filename):
    with open(filename, 'rt') as f:
        return f.read()


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)


setup(
    name='single_access',
    version='0.0.5',

    description='Single access to run a python script',
    long_description=read('README.rst'),

    classifiers=[
        'License :: OSI Approved :: ISC License (ISCL)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    author='Imbolc',
    author_email='imbolc@imbolc.name',
    license='ISC',
    url='https://github.com/imbolc/single_access',

    packages=find_packages(),
)
