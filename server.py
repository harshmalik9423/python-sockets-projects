#
# server.py
#
import config
import socket
from threading import Thread

def client_thread(client_socket, address):
    print("Connection from {}:{}.").format(address[0], address[1])
    data = client_socket.recv(config.BUFFER_SIZE)
    message = data.decode(config.MESSAGE_ENCODING)
    if message:
        print("Client at {}:{} says \"{}\".").format(address[0], address[1], message)

if __name__ == '__main__':
    # Create socket, bind to port, and start listening.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config.SERVER_HOSTNAME, config.SERVER_PORT))
    server_socket.listen(config.SERVER_MAX_CONN_QUEUE)

    # Receive connections and pass off to new threads.
    while True:
        (client_socket, address) = server_socket.accept()
        Thread(target=client_thread, args=(client_socket, address)).start()
    server_socket.close()
