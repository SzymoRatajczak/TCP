import ssl
import socket

host='127.0.0.1'
port=80

def client(cafile=None):
    purpose=ssl.Purpose.SERVER_AUTH
    context=ssl.create_default_context(purpose,cafile=cafile)

    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket=context.wrap_socket(client,server_side=False)

    new_socket.connect((host,port))

    new_socket.send("my request".encode(ascii()))


    new_socket.close()
    client.close()