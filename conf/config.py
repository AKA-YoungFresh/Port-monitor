#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import time

#发送邮箱
fromaddr = 'xxx@xxx.com'
#邮箱授权码 
password = 'xxxxxxxx'
#接收邮箱  
toaddrs = ['xxx@xxxx.com','xxxx@xxxx.com']
#邮件内容
content = 'The scan for port has finshed.for details, see attached'
#邮件标题
nowtime = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
title='result of portscan  '+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#附件路径
filepath='report/portinfo.xls'