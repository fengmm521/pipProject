#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import json
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


datatool = None


class TestHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        print(self.path.encode())
        print(type(self.path))
        print(self.client_address)
        global datatool
        try:
            # fpth = '/root/svnclient/svnp8100/httpserver' + self.path
            fpth = '.' + self.path
            if os.path.exists(fpth):
                f = open(fpth,'r')
                jstr = f.read()
                f.close()
                self.sendJsonMsg(jstr)
                return None
            elif self.path == '':
                self.send_error(404,'File Not Found: %s' % self.path) 
                return None
        except Exception as e:
            print(e)
            self.send_error(404,'File Not Found: %s' % self.path)  
            return None
        
    def sendJsonMsg(self,jmsg):
        length = len(jmsg)
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        self.wfile.write(jmsg.encode())
    def do_POST(self):


        dictmp = self.do_GET()


        # length = self.headers.getheader('content-length');
        print(self.headers.headers())



        """Serve a POST request."""
        # form = cgi.FieldStorage(
        #     fp=self.rfile,
        #     headers=self.headers,
        #     environ={'REQUEST_METHOD': 'POST',
        #              'CONTENT_TYPE': self.headers['Content-Type'],
        #              })
        # filename = form['file'].filename
        # print filename
        # path = self.translate_path(self.path)
        # print path
        # filepath = os.path.join(path, filename)
        # print filepath
        # if os.path.exists(filepath):
        #     self.log_error('File %s exist!', filename)
        #     filepath += '.new'

        # with open(filepath, 'wb') as f:
        #     f.write(form['file'].value)

        

    # def do_HEAD(self):
    #     """Serve a HEAD request."""
    #     f = self.send_head()
    #     if f:
    #         f.close()

def runHttpServer(port,objtool):
    global datatool
    datatool = objtool
    print(datatool)
    http_server = HTTPServer(('172.16.6.25', int(port)), TestHTTPHandler)
    print('server is start:(172.16.6.25,%d)'%(port))
    http_server.serve_forever() #设置一直监听并接收请求

def start_server(port):
    thr = threading.Thread(target=runHttpServer,args=(port,'xxx'))
    thr.setDaemon(True)
    thr.start()

def main():
    start_server(8889)

    while True:
        time.sleep(1000)
        # print('sleep2')

if __name__ == '__main__':
    main()
