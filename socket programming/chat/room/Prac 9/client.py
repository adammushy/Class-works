import socket
import threading

#host=str(input('enter server ip address::'))
host='127.0.0.1'
port=5050

alias=input("choose an alias::")


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

#fcnt for receiver
def client_receive():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message == "alias":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            client.close()
            break
 
#fnctn for sender       
def client_send():
    while True:
        message = f'{alias}:: {input("")}' 
        client.send(message.encode('utf-8'))

receive_thread= threading.Thread(target=client_receive)
receive_thread.start()

send_thread= threading.Thread(target=client_send)
send_thread.start()
