import serial
from time import sleep

data ='' 
angle =''

serialPort = "/dev/ttyUSB0"

baudRate   = 115200


ser = serial.Serial(serialPort, baudRate, timeout=0.5) 

while True:  
    #data =recv(ser) 
    data = ser.readline() 
    #ser.write(data)
    if len(data)>50:
       angle=data[15:18]
    print(angle)

