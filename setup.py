#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "magetool",
    version = "0.1.0",
    keywords = ("pip", "datacanvas", "eds", "xiaoh"),
    description = "eds sdk",
    long_description = "eds sdk for python",
    license = "MIT Licence",

    url = "http://xiaoh.me",
    author = "mage",
    author_email = "mage@woodcol.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)