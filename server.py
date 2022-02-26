import socket
import sys


def create_socket():
    try:
        global host
        global port
        global socket_obj
        host = ""
        port = 9999
        socket_obj = socket.socket()
    except socket.error as error_msg:
        print(f"Create Socket Error Message: {error_msg}")
                

def bind_socket():
    try:
        global host
        global port
        global socket_obj
        socket_obj.bind((host, port))
        socket_obj.listen(5)
    except socket.error as error_msg:
        print(f"Socket Binding error: {error_msg} Retrying.")
        bind_socket()

def accept_socket():
    try:
        conn, address = socket_obj.accept()
        print(f" IP address: {address[0]}")
        print(f" Port: {address[1]}")
        send_command(conn)
        conn.close()
    except socket.error as error_msg:
        print(f"Socket Binding error: {error_msg} Retrying.")
        bind_socket()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            socket_obj.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    accept_socket()


if __name__ == "__main__":
    main()


    



