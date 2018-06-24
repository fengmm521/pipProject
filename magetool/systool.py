#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-09 22:36:40
# @Author  : mage
# @Link    : http://woodcol.com
# @market. : https://fengmm521.taobao.com
# @Version : $Id$

from sys import version_info  
import pickle

def pythonVersion():
    return version_info.major,version_info.minor

#保存python对象到文件
def saveObjToFile(obj,fPth):
    f = open(fpth,'wb')
    pickle.dump(obj, f)
    f.close()

#从文件加载一个对象
def loadObjFromFile(fpth):
    f = open(fpth,'rb')
    obj = pickle.load(f)
    f.close()
    return obj

if __name__ == '__main__':
    print(pythonVersion())

