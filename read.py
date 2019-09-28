import serial
import time

ser = serial.Serial("COM3", 115200)
time.sleep(1)

def decodeSerial(data):
    decodedStr = data.decode("utf-8").strip()
    if len(decodedStr) == 0 or decodedStr[0] != "(" or decodedStr[-1] != ")":
        return None
    return list(map(float,decodedStr[1:-1].split(",")))

while True:
    print(decodeSerial(ser.readline()))

