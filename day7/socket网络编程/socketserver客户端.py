#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    msg=input('>>:')
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data)