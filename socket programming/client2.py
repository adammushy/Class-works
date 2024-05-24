import socket
from urllib import response

from requests import Response

client_sock=socket.socket()

#host=str(input("enter the ip address::"))
#port=int(input("enter the port no::"))
host="127.0.0.1"
port=5050

try:
    client_sock.connect((host,port))

except socket.error as e:
    print(str(e))
    
Response=client_sock.recv(2048)
print(Response.decode('utf-8'))

#to keep client running as  server running until we decide to stop
while  True:
    Input=input("Say something::")
    client_sock.send(str.encode(Input))
    response=client_sock.recv(2048)
    print(response.decode("utf-8"))

client_sock.close()