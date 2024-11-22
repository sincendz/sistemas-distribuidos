import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 50000  


def envioMensagem():
    mensagem = input("Digite a mensagem que deseja mandar mensagem para o cliente: ")
    return mensagem


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Servidor Rodando!")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Con with{addr}')
        while True:
                data = conn.recv(1024)
                #if not data: break
                print(f"Mensagem Cliente: {data.decode()}")
                conn.send(envioMensagem().encode())
        print(f'Disc with {addr}')