from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = ''
port = 12345

s.connect((host, port))
print(s.recv(1024))
s.close()
