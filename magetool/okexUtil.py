#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 20:51:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
import sympy




#kprice:开仓价格,dk:开仓方向,gg:杠杆倍数,qplv:强平保证金率
def okexQP(kprice,dk,num = 1.0,gg = 20.0,qplv = 0.2):
    if type(kprice) == float and kprice > 1.0 and (dk == 1 or dk == -1):
        kp = kprice         #开仓价
        mz = 100.0          #定单面值为100美元
        kbzj = num*(mz/kp)/gg   #保证金数量
        x = sympy.symbols('x')
        wsx = dk*(((mz/kp)*(x-kp))/x)/(mz/(kp*gg))*kbzj     #未实现盈亏
        out = sympy.solve( ((kbzj + wsx)*kp*gg/(mz*num)) - qplv,x)    #计算结果
        print(out)
        print(type(out),len(out))
        pout = out[0]
        shylv = dk*(((mz/kp)*(pout-kp))/pout)/(mz/(kp*gg))
        wsx_out = shylv*kbzj
        bzjv = 1.0 + shylv
        dicout = {'kbzj':kbzj,'qpPrice':pout,'wsx':wsx_out,'sylv':shylv,'bzjv':bzjv}
        return dicout
    else:
        return {}


#kplist:开仓价格和数量
def okexQP_Mutil(kplist,dk,gg = 20.0,qplv = 0.20):
    kbzj_all = 0.0   #保证金数量
    mz = 100.0          #定单面值为100美元
    # kp = kprice         #开仓价    
    x = sympy.symbols('x')
    wsx_all = 0.0
    k_all = 0.0
    num_all = 0.0
    minprice = 0.0
    maxprice = 0.0
    for i,v in enumerate(kplist):
        kp = v[0]
        num = v[1]
        kbzj = num*(mz/kp)/gg   #保证金数量
        kbzj_all += kbzj
        k_all += kp*num
        num_all += num
        wsx = dk*(((mz/kp)*(x-kp))/x)/(mz/(kp*gg))*kbzj     #未实现盈亏
        wsx_all += wsx
        if maxprice == 0.0 or kp > maxprice:
            maxprice = kp
        if minprice == 0.0 or kp < minprice:
            minprice = kp
    kp_all = k_all/num_all
    out = sympy.solve( ((kbzj_all + wsx_all)*kp_all*gg/(mz*num_all)) - qplv,x)    #计算结果
    # print(out)
    # print(type(out),len(out))
    pout = out[0]
    shylv = dk*(((mz/kp_all)*(pout-kp_all))/pout)/(mz/(kp_all*gg))
    wsx_out = shylv*kbzj_all
    bzjv = 1.0 + shylv
    outpercent = 0
    if dk < 0:
        outpercent = abs(pout - minprice)*100/minprice
    elif dk > 0:
        outpercent = abs(pout - maxprice)*100/maxprice
    dicout = {'kbzj':kbzj_all,'qpPrice':pout,'wsx':wsx_out,'sylv':shylv,'bzjv':bzjv,'pprice':kp_all,'maxpercent':outpercent}
    return dicout


def addNextPrice(plists,dk):
    dktype = 1
    if dk < 0:
        dktype = -1
    minput = []
    for i,v in enumerate(plists):
        minput.append([v,1])
    mtmp = okexQP_Mutil(minput, dktype)
    plists.append(mtmp['qpPrice'])
    return mtmp['kbzj'] #反回开仓保证金

def mutilPrice(kprice,dp):
    out = []
    if dp > 1:
        count = dp
        tmp = okexQP(float(kprice),1)
        # {'bzjv': 0.200000000000000, 'wsx': -0.000453001132502831, 'qpPrice': 8490.38461538462, 'sylv': -0.800000000000000, 'kbzj': 0.000566251415628539}
        # print(tmp)
        qpprice = tmp['qpPrice']
        tmplist = [kprice]
        tmplist.append(qpprice)
        kbzj = 0.0 #保证金
        count -= 1
        while count >0:
            kbzj = addNextPrice(tmplist,1)
            count -= 1
        # print(tmplist)
        return tmplist,kbzj
    elif dp < 0:
        count = dp
        tmp = okexQP(float(kprice),-1)
        qpprice = tmp['qpPrice']
        tmplist = [kprice]
        tmplist.append(qpprice)
        kbzj = 0.0 #保证金
        count += 1
        while count <0:
            kbzj = addNextPrice(tmplist,-1)
            count += 1
        # print(tmplist)
        return tmplist,kbzj #保证金
    else:
        return [],None

def main(kprice,dk):
    if dk > 1 or dk < -1:
        out = mutilPrice(float(kprice),int(dk))
        print(out)
    else:
        out = okexQP(float(kprice),int(dk))
        print(out)
def test():
    # out = okexQP(8148,1)
    # print(out)
    # out = okexQP_Mutil([[7310.1,4],[7351.83,3],[7400.86,3],[7460,3],[7534,2],[7635.48,2],[7788,1],[8100,1]], 1)
    # out = okexQP_Mutil([[7310.1,1],[7572.83,8]], 1)
    
    out = mutilPrice(8848.0, 3)

    print(out)
#测试
if __name__ == '__main__':
    args = sys.argv
    fpth = ''
    if len(args) == 3 :
        main(float(args[1]), int(args[2]))
    else:
        print "请加上开仓价，开仓方向，-1为空仓，1为多仓"
    # test()
    
