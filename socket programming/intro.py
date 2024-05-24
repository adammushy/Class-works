#TCP SOCKET
from ast import Try
from socket import *
import socket
import sys 

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #the socket famly is the domain of scoket,
    #SOck_stream for TCP,
    #SOck_dgram for UDP,
    #port-specifies variation of protocol 

except socket.error as err:
    print("failed to create a socket")
    print("reason " + str(err))
    sys.exit()

print("socket created")

target_host=input("enter the target host name to connect::")
target_port=input("enter the target port:: ")
#for this to connect need to have internet so as to connect with address name

try:
    sock.connect((target_host,int(target_port)))
    print("socket connected to: " + target_host +" "+ target_port)
    sock.shutdown(2)
    
except socket.error as err:
    print("failed to connect  to %s on port %s" %(target_host, target_port))
    print("reason is : %s" %str(err))
    sys.exit()