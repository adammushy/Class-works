from socket import *
import socket
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#to print an ip of a web
name=str(input("enter name of the web site::"))
ip=socket.gethostbyname(name)

print(ip)