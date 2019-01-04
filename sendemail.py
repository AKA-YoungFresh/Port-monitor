#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from conf.config import *
 
def sendmail():

    textApart = MIMEText(content)
    excelFile = filepath
    excelFileName='portinfo-'+nowtime+'.xls'
    excelApart = MIMEApplication(open(excelFile, 'rb').read())
    excelApart.add_header('Content-Disposition', 'attachment', filename=excelFileName)

    m = MIMEMultipart()
    m.attach(excelApart)
    m.attach(textApart)
    m['Subject'] = title
    m['from'] = fromaddr
    m['to'] = ','.join(toaddrs)

    try:
        server = smtplib.SMTP('smtp.xxxx.com')
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('report has sended to your email !')
        server.quit()
    except smtplib.SMTPException as e:
        print('fail to send email:',e) #打印错误
