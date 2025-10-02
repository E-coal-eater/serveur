import serial

arduino = serial.Serial(port ="COM16", baudrate=9600, timeout = .1)

arduino.write(bytes(5, 'utf-8'))
reponse = arduino.readline()
print(reponse)