#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading  
import time
from Queue import Queue  

class _timerThread(threading.Thread):  
    def __init__(self, t_name,queue,cond,timePrecision):  
        threading.Thread.__init__(self, name=t_name) 
        self.threadtimes = []
        self.threadFunc = {}
        self.lasttimes = {}
        self.isOnceRuns = []
        self.threadFuncRun = {}
        self.queue = queue
        self.timePrecision = timePrecision
    def setNewTimer(self,newobj):
        if newobj.func == None:
            self.threadtimes.remove(newobj.secendtime)
            self.threadFunc[str(newobj.secendtime)] = None
            self.lasttimes[str(newobj.secendtime)] = None
            self.threadFuncRun[str(newobj.secendtime)] = None
            if newobj.secendtime in self.isOnceRuns:
                self.isOnceRuns.remove(newobj.secendtime)
        else:
            if newobj.secendtime in self.threadtimes:
                self.threadFunc[str(newobj.secendtime)] = newobj.func
                self.lasttimes[str(newobj.secendtime)] = int(time.time())
                self.threadFuncRun[str(newobj.secendtime)] = False
                if newobj.isOnce:
                    self.isOnceRuns.append(newobj.secendtime)
            else:
                self.threadtimes.append(newobj.secendtime)
                self.threadFunc[str(newobj.secendtime)] = newobj.func
                self.lasttimes[str(newobj.secendtime)] = int(time.time())
                self.threadFuncRun[str(newobj.secendtime)] = False
                if newobj.isOnce:
                    self.isOnceRuns.append(newobj.secendtime)
    def run(self):
        while(True):
            time.sleep(self.timePrecision)
            if not self.queue.empty():
                objtmp = self.queue.get()
                self.setNewTimer(objtmp)
            timetmp = int(time.time())
            for tx in self.threadtimes:
                if timetmp - self.lasttimes[str(tx)] >= tx:
                    self.lasttimes[str(tx)] = timetmp
                    self.threadFunc[str(tx)](timetmp)
                    self.threadFuncRun[str(tx)] = True
            romveOnces = []
            for tone in self.isOnceRuns:
                if self.threadFuncRun[str(tone)]:
                    romveOnces.append(tone)
            for rmx in romveOnces:
                self.threadtimes.remove(rmx)
                self.threadFunc[str(rmx)] = None
                self.lasttimes[str(rmx)] = None
                self.threadFuncRun[str(rmx)] = None
                self.isOnceRuns.remove(rmx)
        self.condition.release()
        
class _timerObj():
    def __init__(self,secendt,funct,isOnce = False):
        self.secendtime = secendt
        self.func = funct
        self.isOnce = isOnce

class pytimer():
    #timePrecision为时间精度，时间精度越高越占CPU时间，默认为100毫秒精度
    def __init__(self,timePrecision = 0.1):
        self.queue = Queue()   
        self.cond = threading.Condition()
        self.t_thread = _timerThread(str(int(time.time())),self.queue, self.cond,timePrecision) 
        self._timers = []
        self._initTimer()
    def _initTimer(self):
        self.t_thread.setDaemon(True)
        self.t_thread.start()
    def getTimers(self):
        return self._timers
    def setTimer(self,secendTime,Func,isOnce = False):
        objtmp = _timerObj(secendTime,Func,isOnce)
        self._timers.append(secendTime)
        self.queue.put(objtmp)
    def removeTimer(self,secendTime):
        objtmp = _timerObj(secendTime,None)
        self._timers.remove(secendTime)
        self.queue.put(objtmp)
    


def main():  
    def timerCallBack(timex):
        print timex
    timerx = pytimer()
    timerx.setTimer(2, timerCallBack)
    while(True):
        time.sleep(1)
        pass
if __name__ == '__main__':  
    main()
