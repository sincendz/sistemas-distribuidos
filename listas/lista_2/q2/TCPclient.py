import socket
import threading

def envioMensagem():
    mensagem = input("Digite a mensagem que deseja mandar mensagem para o servidor: ")
    return mensagem

def sendMensageToServer():
    while True:
        s.send(envioMensagem().encode())

def reciveMensageFromServer():
    while True:
        data = s.recv(1024)
        print(f"Mensagem servidor:  {data.decode()}")

HOST = '127.0.0.1'
PORT = 50000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        thread = threading.Thread(target=sendMensageToServer)
        thread.start()
        thread_1 = threading.Thread(target=reciveMensageFromServer)
        thread_1.start()
        
