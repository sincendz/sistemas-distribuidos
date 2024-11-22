import socket
import threading

HOST = "127.0.0.1"
PORT = 50000  


def mensageToClient():
    mensagem = input("Digite a mensagem que deseja mandar mensagem para o cliente: ")
    return mensagem

def reciveMensageFromClient():
    while True:
        data = conn.recv(1024)
        print(f"Mensagem Cliente: {data.decode()}")

def sendMensageToClient():
    while True:
        conn.send(mensageToClient().encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Servidor Rodando!")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Con with{addr}')
        while True:
            thread = threading.Thread(target=reciveMensageFromClient)
            thread.start()
            thread1 = threading.Thread(target=sendMensageToClient)
            thread1.start()
    print(f'Disc with {addr}')