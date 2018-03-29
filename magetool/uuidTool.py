#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-09 22:36:40
# @Author  : mage
# @Link    : http://woodcol.com
# @market. : https://fengmm521.taobao.com
# @Version : $Id$

# from win32com.client import GetObject
import platform
import os
sysSystem = platform.system()


def getUUID():
    cmd = ""
    if sysSystem == 'Windows':  
        cmd = 'wmic csproduct get UUID'
    elif sysSystem == 'Darwin':
        cmd = "/usr/sbin/system_profiler SPHardwareDataType | fgrep 'UUID' | awk '{print $NF}'"
    elif sysSystem == 'Linux':
        cmd = "/usr/sbin/dmidecode -s system-uuid"
    output = os.popen(cmd)
    ostr = output.read()
    ostr = ostr.replace('\r','')
    ostrs = ostr.split('\n')
    uuid = ''
    for d in ostrs:
        tmpd = d.strip()
        if len(tmpd) < 20:
            continue
        else:
            uuid = tmpd
    return uuid

def main():
    uuid = getUUID()
    print(uuid)
if __name__ == '__main__':
    main()