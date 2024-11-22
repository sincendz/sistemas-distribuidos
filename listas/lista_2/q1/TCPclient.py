import socket
import os

def envioMensagem():
    mensagem = input("Digite a mensagem que deseja mandar mensagem para o servidor: ")
    return mensagem;

def serverConnection():
    HOST = '127.0.0.1'
    PORT = 50000
    dados = envioMensagem().encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        if(dados.decode() == 'exit'):
            exit(1)
        while True:
            s.send(dados)
            data = s.recv(1024)
            print(f"Mensagem servidor:  {data.decode()}")

def main():
    while True:
        serverConnection()        
if __name__ == '__main__':
    main()