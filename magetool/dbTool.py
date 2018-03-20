#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-22 09:44:42

import dbm
import json
import time

dbpth = './db/keysdb'

class DBMObj(object):
    """docstring for ClassName"""
    def __init__(self, pth):
        self.dbpth = pth
        self.dbtimepth = pth + 'time'

    def inset(self,key,value):
        db = dbm.open(self.dbpth, 'c')
        db[key] = value
        db.close()
        tdb = dbm.open(self.dbtimepth, 'c')
        if key in tdb:
            timedic = json.loads(tdb[key])
            timedic['last'] = int(time.time())
            tdb[key] = json.dumps(timedic)
        else:
            timedic = {'create':int(time.time()),'last':int(time.time())}
            tdb[key] = json.dumps(timedic)
        tdb.close()

    def insetList(self,keys,values):
        if len(keys) == len(values):
            db = dbm.open(self.dbpth, 'c')
            tdb = dbm.open(self.dbtimepth, 'c')
            for i in range(len(keys)):
                db[keys[i]] = values[i]
                key = keys[i]
                if keys[i] in tdb:
                    timedic = json.loads(tdb[key])
                    timedic['last'] = int(time.time())
                    tdb[key] = json.dumps(timedic)
                else:
                    timedic = {'create':int(time.time()),'last':int(time.time())}
                    tdb[key] = json.dumps(timedic)
            tdb.close()
            db.close()

            return True
        else:
            return False

    def delet(self,key):
        db = dbm.open(self.dbpth, 'c')
        if key in db:
            del db[key]
            tdb = dbm.open(self.dbtimepth, 'c')
            del tdb[key]
            tdb.close()
        db.close()

    def update(self,key,value):
        db = dbm.open(self.dbpth, 'c')
        db[key] = value
        db.close()
        tdb = dbm.open(self.dbtimepth, 'c')
        if key in tdb:
            timedic = json.loads(tdb[key])
            timedic['last'] = int(time.time())
            tdb[key] = json.dumps(timedic)
        else:
            timedic = {'create':int(time.time()),'last':int(time.time())}
            tdb[key] = json.dumps(timedic)
        tdb.close()

    def select(self,key):
        db = dbm.open(self.dbpth, 'c')
        out = None
        if key in db:
            out = db[key]
        db.close()
        return out

    def allKeys(self):
        db = dbm.open(self.dbpth, 'c')
        keys = db.keys()
        db.close()
        return keys
        
    def getDBDatas(self):
        db = dbm.open(self.dbpth, 'c')
        data = {}
        for k in db.keys():
            data[k] = json.loads(db[k])
        db.close()
        return data
def main():
    tobj = DBMObj(dbpth)
    print(tobj)
    print(tobj.allKeys())
    tobj.inset('mykey2', '111')
    print(tobj.select('mykey'))
    tobj.delet('mykey')
    print(tobj.select('mykey'))
    print(tobj.select('mykey2'))
    tobj.update('mykey2', 'dddx')
    print(tobj.select('mykey2'))
    # delet('mykey2')
    print(tobj.allKeys())

if __name__=="__main__":  
    main()

