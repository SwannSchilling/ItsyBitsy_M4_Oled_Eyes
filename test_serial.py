import serial
#You will need to find out on which port your board is connected
#and change the COM or /dev/tty accordingly!

# Connect a Raspberry Pi
#ser = serial.Serial('/dev/ttyAMA0', 115200)
# Connect a PC
ser = serial.Serial('COM11', 115200)
print(ser.portstr)
#send data via serial port
ser.write('3\r\n'.encode())
ser.close()
