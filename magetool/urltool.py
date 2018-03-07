#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import chardet


def conventStrTOUtf8(oldstr):
    try:
        nstr = oldstr.encode("utf-8")
        return nstr
    except Exception as e:
        print('nstr do not encode utf-8')
    cnstrtype = chardet.detect(oldstr)['encoding']
    utf8str =  oldstr.decode(cnstrtype).encode('utf-8')
    return utf8str


def getUrl(purl):
    try:
        req = urllib2.Request(purl)
        req.add_header('User-agent', 'Mozilla 5.10')
        res = urllib2.urlopen(req)
        html = conventStrTOUtf8(res.read())
        return html
    except Exception, e:
        print(e)
    return None

if __name__ == '__main__':
    pass