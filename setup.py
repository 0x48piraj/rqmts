#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup, find_packages

"""Setup script for rqmts"""

pwd = os.path.abspath(os.path.dirname(__file__))
# README file
with open(os.path.join(pwd, "README.md")) as f:
    README = f.read()
    f.close()

# call to setup()
setup(
    name="rqmts",
    version="1.0.0",
    description="Generates pip requirements.txt file for any project by analysing package imports",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/0x48piraj/rqmts",
    author="Piyush Raj <0x48piraj>",
    author_email="piyush@linuxmail.org",
    license="BSD-3",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["rqmts=rqmts.__main__:main"]},
)