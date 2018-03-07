#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################

import os
def getNowVersionLineNumber(lines):
    for n in range(len(lines)):
        l = lines[n]
        if l.find('version = "') != -1:
            return n
    return None


def getNewVersion(vercode):
    ns = vercode.split('.')
    n1 = int(ns[0])
    n2 = int(ns[1])
    n3 = int(ns[2])
    newcode = str(n1) + '.' + str(n2) + '.' + str(int(n3) + 1)
    return newcode


def createNewStrFromLines(lines):
    outstr = ''
    for l in lines:
        outstr += l
    return outstr

setupfilepth = 'setup.py'

def saveNewVersionStr(outstr):
    f = open(setupfilepth,'w')
    f.write(outstr)
    f.close()

def addVersion():
    f = open(setupfilepth,'r')
    lines = f.readlines()
    f.close()

    vnumber = getNowVersionLineNumber(lines)


    if vnumber != None and vnumber > 0:
        versionstr = lines[vnumber].replace('\n','')
        versionstr = versionstr.replace('\r','').replace(' ','')[:-1]
        print(versionstr)
        vercode = versionstr.split('=')[1][1:-1]
        print(vercode)
        newcode = getNewVersion(vercode)
        print(newcode)
        newversionstr = '    version = "%s",\n'%(newcode)
        print(newversionstr)
        lines[vnumber] = newversionstr
        outstr = createNewStrFromLines(lines)
        print(outstr)
        saveNewVersionStr(outstr)

def main():
    addVersion()

if __name__ == '__main__':
    main()
