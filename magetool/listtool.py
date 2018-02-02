#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json


def saveListWithJson(datas,jsonpth):
    ostr = json.dumps(datas)
    f = open(jsonpth,'w')
    f.write(ostr)
    f.close()

def getListDataFromJsonFile(jpth):
    f = open(jpth,'r')
    jstr = f.read()
    f.close()
    datas = json.loads(jstr)
    return datas

def saveDicWithJson(dic,jsonpth):
    ostr = json.dumps(dic)
    f = open(jsonpth,'w')
    f.write(ostr)
    f.close()

def getDicDataFromJsonFile(jpth):
    f = open(jpth,'r')
    jstr = f.read()
    f.close()
    datas = json.loads(jstr)
    return datas

def saveListWithLineTxt(datas,txtpth):
    ostr = ''
    for d in datas:
        ostr += str(d) + '\n'
    ostr = ostr[:-1]
    f = open(txtpth,'w')
    f.write(ostr)
    f.close()

def getListWithCSVFile(csvpth,isHeaveHand = False):
    outs = []
    f = open(csvpth,'r')
    lines = f.readlines()
    f.close()
    if isHeaveHand:
        lines = lines[1:]

    for l in lines:
        tmpl = l.replace('\n','')
        tmpl = tmpl.replace('\r','')
        tmps = tmpl.split(',')
        if len(tmps) > 0:
            outs.append(tmps)
    return outs

if __name__ == '__main__':
    pass