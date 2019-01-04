#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import schedule
import os
import time

cmd="python portscan.py"

def shell():
	os.system(cmd)
  

#定时每天7：00/18：00执行任务
schedule.every().day.at("7:00").do(shell)
#schedule.every().day.at("18:00").do(shell)

while True:
     #启动服务
     schedule.run_pending()
     time.sleep(1)