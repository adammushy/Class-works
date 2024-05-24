import socket

client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF INET stands refer to address which is IPV4,SOCK_STREAM- stand for connection oriented tcp protocol
client_sock.connect(('127.0.0.1',5050))

msg='hellow server'

try:
    while True:
        client_sock.send(msg.encode('utf-8'))
        data=client_sock.recv(1024)
        print(str(data))
        extra=input('do you to send more n more data')
        if extra.lower()=='yes':
            msg=input("enter another message")
        else:
            break

except KeyboardInterrupt:
    print("exited by user")
client_sock.close()
