import serial
import time

ser = serial.Serial("COM3", 115200)
time.sleep(1)

while True:
    print(ser.readLine())

