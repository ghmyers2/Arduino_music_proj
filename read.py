import serial
import time

ser = serial.Serial("COM4", 9600)
time.sleep(1)

while True:
    print(ser.readLine())

