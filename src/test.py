import serial
import time

ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with your serial port
time.sleep(2)  # Wait for the serial connection to initialize

ser.write(b'1')
ser.close()