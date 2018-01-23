#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from magetool import pathtool
from magetool import timetool


print timetool.getNowDate()

print pathtool.getAllExtFile('.','.py')