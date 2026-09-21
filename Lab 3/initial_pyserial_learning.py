import serial

print("Learning Pyserial")

ser = serial.Serial(port="/dev/ttyACM0", baudrate=19200, timeout=10)

ser.open()

while not ser.is_open():
    print("opening...")

#To-Do: Use the ser object

ser.close()