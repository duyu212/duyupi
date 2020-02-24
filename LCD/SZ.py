#!/usr/bin/env python3
import LCD1602,cpu
import os,time,subprocess,datetime

def TT():
    date1=datetime.datetime.now().strftime('%Y-%m-%d')
    date2=datetime.datetime.now().strftime('%H:%M:%S')

    a = date2.split(':')

    b=a

    print (a()==b())




    LCD1602.init(0x27, 1)
    LCD1602.write(3, 0, date1)
    LCD1602.write(4, 1, date2)

    print (date1)
    print (date2)
    print (a)
    print (b)

    time.sleep(1)

while(1):
    TT()
