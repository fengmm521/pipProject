#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import urllib2
import chardet
import requests
from urllib import parse

def urldecode(purl):
    return parse.unquote(purl)
def urlencode(purl):
    return parse.quote(purl)

def conventStrTOUtf8(oldstr):
    try:
        nstr = oldstr.encode("utf-8")
        return nstr
    except Exception as e:
        print('nstr do not encode utf-8')
    cnstrtype = chardet.detect(oldstr)['encoding']
    utf8str =  oldstr.decode(cnstrtype).encode('utf-8')
    return utf8str

def postDataToURL(purl,data):
    if purl[0:5] == 'https':
        response = requests.post(purl,data=data,verify=False)
        dat = response.text
        return dat
    else:
        response = requests.post(purl,data=data)
        dat = response.text
        return dat

def getUrl(purl):
    try:
        if purl[0:5] == 'https':
            res = requests.get(purl, verify=False)
            # print(res.text)
            return res.text
        else:
            res = requests.get(purl)
            # print(res.text)
            return res.text
    except Exception as e:
        print(e)
    return None

def getUrlWithChrome(purl,isProxy=False):
    rurl = purl
    proxies = { "http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080" }
    try:
        s = requests.Session()
        s.headers.update({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'})
        if purl[0:5] == 'https':
            res = None
            if isProxy:
                res = s.get(rurl,verify=False,proxies=proxies)
            else:
                res = s.get(rurl,verify=False)
            # print(res.text)
            return res.text
        else:
            res = None
            if isProxy:
                res = requests.get(purl,proxies=proxies)
            else:
                res = requests.get(purl)
            # print(res.text)
            return res.text
    except Exception as e:
        print(e)
    return None

if __name__ == '__main__':
    pass