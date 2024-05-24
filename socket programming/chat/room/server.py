'chat room connection server' 
import socket 
import threading

host='127.0.0.1'
port=5050

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen()
clients=[]#list for clients
aliases=[]# list for aliases (nuicknames for each client)

#function to send massage
def broadcast(message):
    for client in clients:
        client.send(message)



#fnction handle connection to each client computer
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)#this is max no of bytes that a serer can recv from client
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias=aliases[index]
            broadcast(f'this {alias} has left teh chat room'.encode('utf-8'))
            aliases.remove(alias)
            break
        
#main function to receive the client connetion
def receive():
    while True:
        print('server is running and wiating for connection....')
        client,addr= server.accept()
        print(f'connection is established with {str(addr)}')
        client.send('alias?'.encode('utf-8'))
        alias= client.recv(1024)
        aliases.append(alias)#add names of alias inthe aliasses list
        clients.append(client)#adding vclient inthe client list
        print(f'the alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has joined the chat room'.encode('utf-8'))
        client.send('you are connected '.encode('utf-8'))
        thread = threading.Thread(target=handle_client,args=(client,))
        thread.start()

if __name__== "__main__":
    receive()