#!/usr/bin/env python

from distutils.core import setup

setup(
    name="dutchdomains",
    version="0.01",
    description="Simple web API for Dutch domain categorization",
    author="Wouter van Atteveldt",
    author_email="wouter@vanatteveldt.com",
    packages=["dutchdomains"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "Flask",
        "peewee",
    ],
)
