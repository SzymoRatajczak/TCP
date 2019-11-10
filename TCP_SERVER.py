import socket

host='127.0.0.1'
port=80

def server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))

    server.listen()
    print("[*]Listening...")

    while True:
        new_socket,addr=server.accept()
        print("got connection from:",addr)
        data=new_socket.recv()
        print("data:",data.decode(ascii()))

        new_socket.send("my response".encode(ascii()))

    server.close()
    new_socket.close()
