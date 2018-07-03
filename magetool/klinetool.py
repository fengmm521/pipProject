#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-28 16:28:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
from magetool import timetool
import numpy as np

#didx为数值在数据中的序号，用来取作均线计算的数据位
def getAverageData(datas,pAver = 3,didx = 4):
    #[1517536380000,142.443,142.443,142,142,3486,244.8654307]
    ##时间戳，开，高，低，收，交易量，交易量转化为BTC或LTC数量
    outs = []
    for n in range(len(datas)):
        d = datas[n]
        tmps = [d[0]]
        if n < pAver -1:
            dtmp = datas[0:n+1]
            vtmp = [x[didx] for x in dtmp]
            mean = np.mean(vtmp)
            tmps.append(mean)
        else:
            dtmp = datas[n - pAver+1:n+1]
            vtmp = [x[didx] for x in dtmp]
            mean = np.mean(vtmp)
            tmps.append(mean)
        outs.append(tmps)
    return outs

def subList(lis1,lis2):
    v1 = list(lis1)
    v2 = list(lis2)
    v = list(map(lambda x: x[0]-x[1], zip(v1, v2)))
    return v


def get_EMA(df,N,idx = 4):  
    emas = []
    for i in range(len(df)):  
        if i==0:  
            emas = [df[i][idx]]
        if i>0:  
            emastmp = (emas[-1] * (N-1.0) + df[i][idx] * 2.0)/(N+1.0)
            emas.append(emastmp)
    return emas  



def get_MACD(df,dshort = 12,dlong = 26,M = 9):
    a=get_EMA(df,dshort)  
    b=get_EMA(df,dlong)  
    DIF=subList(a, b) 

    DEA = []
    #print(df['diff'])  
    for i in range(len(df)):  
        if i==0:  
            # df.ix[i,'dea']=df.ix[i,'diff'] 
            DEA = [DIF[i]] 

        if i>0:  
            DEAtmp = (2 * DIF[i] + (M - 1) * DEA[i-1])/(M+1)
            DEA.append(DEAtmp)

    MACD = list(map(lambda x: (x[0]-x[1])*2, zip(DIF, DEA)))

    return DIF,DEA,MACD
    

def test():
    # openLong()
    print timetool.getNowDate()
    #1.buy,0.不操作，-1.sell



def getLastMacdType(macd):

    mtmps = macd[::-1]
    SXidx = -1
    JXidx = -1
    for i in range(len(mtmps)):
        if i > 0:
            if macd[i-1] >= 0 and macd[i] < 0:
                SXidx = i
            if macd[i-1] <= 0 and macd[i] > 0:
                JXidx = i

            if SXidx >= 0 and JXidx >= 0:
                break
    return SXidx,JXidx


def main():
    # k5d = read5MimKline()
    #['时间戳'，'开'，'高'，'低'，'收'，'交易量'，'交易量转化为BTC或LTC数量']
    kdatas = []
    # isUP = isClose(k1d)
    if not kdatas:
        return
    dif,dea,macd = get_MACD(kdatas)


    

#测试
if __name__ == '__main__':
    main()
    # test()
