#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 20:51:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,sys
import sympy



def okexQP(kprice,dk,gg = 20.0,qplv = 0.2):
    if type(kprice) == float and kprice > 1.0 and (dk == 1 or dk == -1):
        kp = kprice         #开仓价
        mz = 100.0          #定单面值为100美元
        kbzj = (mz/kp)/gg   #保证金数量
        x = sympy.symbols('x')
        wsx = dk*(((mz/kp)*(x-kp))/x)/(mz/(kp*gg))*kbzj     #未实现盈亏
        out = sympy.solve( ((kbzj + wsx)*kp*gg/(mz)) - qplv,x)    #计算结果
        print(out)
        print(type(out),len(out))
        pout = out[0]
        shylv = dk*(((mz/kp)*(pout-kp))/pout)/(mz/(kp*gg))
        wsx_out = shylv*kbzj
        bzjv = 1.0 + shylv
        dicout = {'kbzj':kbzj,'qpPrice':pout,'wsx':wsx_out,'sylv':shylv,'bzjv':bzjv}
        return dicout,
    else:
        return {}
def main(kprice,dk):
    out = okexQP(float(kprice),float(dk))
    print(out)
def test():
    out = okexQP(8148,1)
    print(out)
#测试
if __name__ == '__main__':
    args = sys.argv
    fpth = ''
    if len(args) == 3 :
        main(args[1], args[2])
    else:
        print "请加上开仓价，开仓方向，-1为空仓，1为多仓"
    # test()
    
