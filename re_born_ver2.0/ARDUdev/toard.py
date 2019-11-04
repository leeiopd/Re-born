import serial
# print('serial ' + serial.__version__)

# Set a PORT Number & baud rate
PORT = 'COM4'
BaudRate = 9600

ARD= serial.Serial(PORT,BaudRate)
# print(ARD)
A = 1234
B = 5678
A=str(A)
B=str(B)
Trans="Q" + A + B
Trans= Trans.encode('utf-8')
# print(Trans)

while (True):
    ARD.write(Trans)  # 1 전송