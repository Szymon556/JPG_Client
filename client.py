import socket
import time

PORT = 80
HOST = 'data.pr4e.org'

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((HOST,PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

count = 0
picture = b''

while True:
    data = mysock.recv(5120)
    if len(data)<1:break
    count = count + len(data)
    print(len(data), count)
    time.sleep(0.25)
    picture = picture + data

mysock.close()

pos = picture.find(b'\r\n\r\n')
print(f"Dlugos naglowka: {pos}")
header = picture[:pos].decode()
print(header)

picture = picture[pos+4:]
fhand = open('image.jpg','wb')
fhand.write(picture)
print(picture)
fhand.close()

