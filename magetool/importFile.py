#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import types
# import pyctest
#http://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p11_load_modules_from_remote_machine_by_hooks.html

def loadModeFromFile(fname = 'pyctest.py',modeName = 'pyctest'):
    f = open(fname,'r')
    pycode = f.read()
    f.close()
    m = types.ModuleType(modeName)
    exec pycode in m.__dict__
    m = sys.modules.setdefault(modeName, m)
    # print pyctest
    # print sys.modules['pyctest'].__name__
    # # print sys.modules['pyctest'].__file__
    # print sys.modules['pyctest'].__package__
    return m

def main():
    # print sys.modules
    # print sys.modules.keys()
    
    # print sys.modules['pyctest'].__path__
    # print sys.modules['pyctest'].__loader__

    m = loadModeFromFile()
    print(m.pyctest())
    print(m.xxx)

    testobj = m.TESTObj('hahaha')
    testobj.showP()


if __name__ == '__main__':
    main()