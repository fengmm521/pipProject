#!/usr/bin/python
# -*- coding: utf-8 -*-
#创建SocketServerTCP服务器：

import SocketServer
# from SocketServer import StreamRequestHandler

import os
import socket

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)

print('selfip:%s'%(myaddr))
host = str(myaddr)


port = 9101
addr = (host,port)

class Servers(SocketServer.StreamRequestHandler):
    def handle(self):
        print('got connection from ',self.client_address)
        while True:
            try:  
                data = self.request.recv(1024)
            except EOFError:  
                print('接收客户端错误，客户端已断开连接,错误码:')
                print(EOFError )
                break
            except:  
                print('接收客户端错误，客户端已断开连接')
                break
            if not data: 
                break
            print('data len:%d'%(len(data)))
            print("RECV from ", self.client_address)
            print(data)
            self.request.send('aaa')

def startServer():
    server = SocketServer.ThreadingTCPServer(addr,Servers,bind_and_activate = False)
    server.allow_reuse_address = True   #设置IP地址和端口可以不使用客户端连接等待，并手动绑定服务器地址和端口，手动激活服务器,要不然每一次重启服务器都会出现端口占用的问题
    server.server_bind()
    server.server_activate()
    print('server started:')
    print(addr)
    server.serve_forever()
    
if __name__ == '__main__':
    startServer()