from socket import *
from threading import *
import socket
from _thread import *

server_sock=socket.socket()

host="127.0.0.1"
port=5050

#address={host,port}
threadcount=0 #  counts the number of threads

try:
    server_sock.bind((host,port))#binding the server obj to this address
    
except socket.error as e:
    print(str(e))
print("waiting for connection....")
server_sock.listen(5)


def client_thread(connection):#client function
    connection.send(str.encode("welcome to the server::"))
    while True:
        data=connection.recv(2048)
        reply="hellow i am server::" + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
    
#to keep the server running all time until we stop it manually
while True:
    client,address=server_sock.accept() #accepting connection from client
    print("connected to host "+address[0]+"and port "+str(address[1]))
    start_new_thread(client_thread,(client,))
    threadcount+=1
    print("thread number "+str(threadcount))
    
server_sock.close()