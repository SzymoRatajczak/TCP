import socket

host='127.0.0.1'
port=80

def client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client.connect((host,port))

    client.send("my reqest".encode(ascii()))


    client.close()