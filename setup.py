#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Terminals",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: General",
]

setup(
    name="rangeen",
    version="0.0.1",
    maintainer="Shanu Khera",
    maintainer_email="kherashanu@gmail.com",
    author="Shanu Khera",
    author_email="kherashanu@gmail.com",
    url="https://github.com/khera-shanu/rangeen",
    license="MIT",
    platforms=["any"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="An unicode and ascii colour, emotes, art and loader library for terminals.",
    classifiers=classifiers,
    long_description="""A python package to help developers create terminal tools in python
using multi-color text and unicode emotes.Rangeen also provides ASCII and Unicode art for cool 
branding of command line tools. Except all this rangeen also provides ASCII loaders"""
)
