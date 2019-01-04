#!/usr/bin/python
#coding:utf-8
#auth:Devotes

from socket import * 
import threading 
from time import time
import xlwt
from sendemail import *

lock = threading.Lock() 
row=1
row2=1
gbadport=[]


def portScanner(host,port,sheet,white_list,sheet1): 

	try: 
		s = socket(AF_INET,SOCK_STREAM) 
		s.connect((host,port)) 
		lock.acquire()
		badport=""
		hostandport=host+":"+str(port)
		if hostandport not in white_list:
			badport=port
		print('[+] %s --> %d  open' % (host,port)) 
		fl.write('[+] %s -->%d  open' % (host,port)+'\r\n')
		report(sheet,host,port,sheet1,badport)
		lock.release() 
		s.close() 
	except Exception as e:
		pass 

def report(sheet,host,port,sheet1,badport):
	global row,row2,gbadport
	sheet.write(row,0,host)
	sheet.write(row,1,port)
	if badport:
		sheet1.write(row2,0,host)
		sheet1.write(row2,1,badport)
		#print badport
		gbadport.append(badport)
		row2=row2+1
	row=row+1
	

def main(ip,sheet,excel,white_list,sheet1):
	#start_time=time() 
	print '-'*60
	fl.write('-'*60+'\n')
	print 'scaning for : %s'% ip
	fl.write('scaning for : %s' % ip +'\r\n')
	print '-'*60
	fl.write('-'*60+'\n')
	setdefaulttimeout(3) 
	for n in range(1,76): 
		threads = [] 
		#print (n-1)*880,n*880 
		for p in range((n-1)*880,n*880): 
			t = threading.Thread(target=portScanner,args=(ip,p,sheet,white_list,sheet1)) 
			threads.append(t) 
			t.start() 
		for t in threads: 
			pass 
		t.join() 
	print '-'*60
	fl.write('-'*60+'\n')
	print('[*] The scan is complete!') 
	#print('[*] Total time: %s' % str(time()-start_time))
	fl.write('[*] The scan is complete!'+'\r\n')
	excel.save('report/portinfo.xls')


if __name__ == '__main__': 
	f=open('ip.txt','r')
	fl=open('log/logs.txt','a')
	fwl=open('white_list.txt','r')
	excel = xlwt.Workbook(encoding = 'utf-8')
	pattern = xlwt.Pattern()  # Create the Pattern
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour = 22
	style = xlwt.XFStyle()  # Create the Pattern
	style.pattern = pattern  # Add Pattern to Style
	sheet = excel.add_sheet('端口开放情况'.decode('utf-8'),style)  
	sheet.write(0, 0, 'ip地址'.decode('utf-8'),style)  
	sheet.write(0, 1, '端口'.decode('utf-8'),style)
	sheet1 = excel.add_sheet('新增对外开放的端口'.decode('utf-8'),style)  
	sheet1.write(0, 0, 'ip地址'.decode('utf-8'),style)  
	sheet1.write(0, 1, '端口'.decode('utf-8'),style)
	white_list=[]
	for i in fwl:
		i=i.strip('\r\n')
		white_list.append(i)
	#print white_list
	for ip in f:
		ip=ip.strip('\r\n')
		main(ip,sheet,excel,white_list,sheet1)
	#print gbadport
	if gbadport:
		sendmail()

