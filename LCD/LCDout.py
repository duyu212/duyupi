#!/usr/bin/env python3
import LCD1602,cpu
import os,time,subprocess,datetime

def setup():
    #CPU----------------------
    CPUU=cpu.getCPUuse()[0:2]
    CPU_U=CPUU.split('.')[0]
    CPUT=cpu.getCPUtemperature()[0:2]
    #RAM%----------------------
    RAMA=int(cpu.getRAMinfo()[0])
    RAMU=int(cpu.getRAMinfo()[1])
    RAM= str(round(int(RAMU/RAMA*100),0))
    #IP----------------------
    ip_ad=cpu.getLocalIP()
    IP=ip_ad.split('.')

    #time----------------------
    date1=datetime.datetime.now().strftime('%m-%d')
    date2=datetime.datetime.now().strftime('%H:%M:%S')
    Time = date2.split(':')
    #OutLcd01
    LCD1602.init(0x27, 1)	# init(slave address, background light)
    LCD1602.write(0, 0, 'U'+CPU_U+'%')
    LCD1602.write(4, 0, ' R'+RAM+'%')
    LCD1602.write(9, 0, ' D'+date1)
    LCD1602.write(0, 1, 'IP'+IP[2]+'.'+IP[3])
    LCD1602.write(9, 1, ' T'+Time[0]+':'+Time[1])

    CPU_U_1=CPU_U
    RAM_1=RAM
    date1_1=date1
    IP_1=IP
    time_1=Time


    while(1):
        #CPU----------------------
        CPUU=cpu.getCPUuse()[0:2]
        CPU_U=CPUU.split('.')[0]
        CPUT=cpu.getCPUtemperature()[0:2]
        #RAM%----------------------
        RAMA=int(cpu.getRAMinfo()[0])
        RAMU=int(cpu.getRAMinfo()[1])
        RAM= str(round(int(RAMU/RAMA*100),0))
        #IP----------------------
        ip_ad=cpu.getLocalIP()
        IP=ip_ad.split('.')

        #time----------------------
        date1=datetime.datetime.now().strftime('%m-%d')
        date2=datetime.datetime.now().strftime('%H:%M:%S')
        Time = date2.split(':')
        #OutLcd01
        if CPU_U_1!=CPU_U:
            CPU_U_1=CPU_U
            LCD1602.write(1, 0,CPU_U_1+'% ')
        if RAM_1!=RAM:
            RAM_1=RAM
            LCD1602.write(6, 0,RAM_1+'% ')
        if date1_1!=date1:
            date1_1=date1
            LCD1602.write(11, 0,date1_1)
        if IP_1!=IP:
            IP_1=IP
            LCD1602.write(2, 1,IP_1)
        if time_1!=Time:
            time_1=Time
            LCD1602.write(11, 1,Time[0]+':'+Time[1])
            time.sleep(1)
        LCD1602.write(13, 1,' ')
        time.sleep(0.5)
while(1):
    setup()

