#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='async-kucoin-python',
    version='v2.0.1',
    packages=find_packages(),
    license="MIT",
    author='Igor',
    author_email="igor.kucoin@pm.me",
    url='https://github.com/Kucoin/async-kucoin-python-sdk',
    description="kucoin-api-sdk",
    install_requires=['requests', 'websockets', 'aiohttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
