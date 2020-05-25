#
# client.py
#

import config
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((config.SERVER_HOSTNAME, config.SERVER_PORT))
    if len(sys.argv) > 1:
        message = sys.argv[1]
        data = message.encode(config.MESSAGE_ENCODING)
        client_socket.send(data)
    client_socket.close()
