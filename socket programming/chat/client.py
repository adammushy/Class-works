import socket


client_sock=socket.socket()
host='127.0.0.1'
port=5050
client_sock.connect((host,port)) # we use doble bracket bcoz the address inside  the connect() need to be inform of tuples so the 2nd bracket tuples the whole adress

print(client_sock.recv(1024))
client_sock.close()



