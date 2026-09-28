import serial
import time

print("Learning Pyserial")

ser = serial.Serial(port="/dev/ttyACM0", baudrate=19200, timeout=10)

time.sleep(1.0) # necessary sinetimes
#while not ser.is_open:
#    print("Not open")

ser.reset_input_buffer()
message = "RESET"
message_bytes = (message + "\n").encode()

print(message_bytes)

ser.write(message_bytes)

response_bytes = ser.readline()
print(response_bytes)
response = response_bytes.decode().strip()
print(response)

time.sleep(2)
# Ser inputs
while ser.is_open:
    pass

ser.close()