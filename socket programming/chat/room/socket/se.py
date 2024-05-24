from socket import *
s = socket(AF_INET, SOCK_STREAM)
print("socket created")
port = 12345
s.bind(("", port))
s.listen(5)
print("Waiting for connections......")
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    message = "Thank you for connecting,Your welcome"
    c.send(message.encode())
    c.close()
