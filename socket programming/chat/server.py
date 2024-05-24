from socket import *
import socket
import sys
from traceback import print_tb
 
'''
server has this common functions
bind()-- bindi it to specif ip and port
listen()-- listen incoming connectiom it receives
accept()-- initiate connection wih client
close() -- close connection with client
#AF INET stands refer to address which is IPV4,SOCK_STREAM- stand for connection oriented tcp protocol
 #SOck_stream for TCP,
    #SOck_dgram for UDP,
    #port-specifies variation of protocol 

'''
sock_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket succsesfully created")
port=5050 # put any reasonable of your choice but max number is 63500(not sure) it start 1 since port 0 is reserved

sock_server.bind(('',port))
print(f'socket is binded to port {port}')

sock_server.listen(5) #the number inside indicate the number of server that it can listen if 6th try to connect it will refuse connection
print('server listening...') 

#forever loophelps to keep it active until we interfere with connection
while True:
    c,addr=sock_server.accept()# c- is my connection name you can write any
    print("received connection from ::",addr)
    message=("thanks for connecting..!")
    c.send(message.encode('utf-8'))#since the msg is store in string we can't send it as strings hence we need to encode it and send it as bytes
    c.close()
