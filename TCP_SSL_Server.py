import socket
import ssl

host='127.0.0.1'
port=80

def server(cafile=None):
    purpose=ssl.Purpose.CLIENT_AUTH
    context=ssl.create_default_context(purpose,cafile=cafile)

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket=context.wrap_socket(server,server_side=True)

    new_socket.bind((host,port))

    new_socket.listen()
    print("[*]Listening...")

    while True:
        another_socket,addr=new_socket.accept()
        print("got connection from:",addr)
        data=another_socket.recv()
        print("data:",data.decode(ascii()))

    server.close()
    new_socket.close()
    another_socket.close()