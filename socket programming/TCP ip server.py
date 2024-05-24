from encodings import utf_8
from http import client
import socket
import sys 

server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('127.0.0.1',5050))# bindin the serer to specific address
server_sock.listen(5)#five other can connect


while True:
    print("server waiting for conection")
    client_sock,addr=server_sock.accept()#
    print("client connect from ",addr)
    while True: #accept and send data to client
        data=client_sock.recv(1024)# 1024bytes at most
        if not  data or data.decode('utf-8')=='END':
            break
        print("receive from client client : %s" %data.decode("utf-8"))
        try:
            client_sock.send(bytes('hello client','utf-8'))
        except:
            print("Excited y the user")
    client_sock  .close()       


server_sock.close()