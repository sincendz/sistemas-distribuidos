import socket
from Calculadora import Calculadora

class TCPserver:
    def __init__(self, host='127.0.0.1', port=50_000):
        self.host = host
        self.port = port
        #AF_INET = IPv4
        #SOCK_STREAM = TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        print("Servidor On-line")
        self.socket.listen()
        self.conn , self.addr = self.socket.accept()
        print(f"Servidor iniciado em {self.host}:{self.port}")
        
    def getRequest(self) -> str:
        if not self.conn:
            print("Servidor não conecetado ao cliente.")
        try:
            data = self.conn.recv(1024)
            return data.decode()
        except socket.error as e:
            raise ConnectionError(f"Erro ao receber o pacote do cliente{e}")
            

    def sendResponse(self , response : str):
        data = response.split('_')
        print(data)
        operador = data[0]
        n1 = float(data[1])
        n2 = float(data[2])
        if not self.conn:
            print("Servidor não conectado ao cliente")
        try:
            resultado = 0
            calculadora = Calculadora()
            if operador == '+': resultado = calculadora.add(n1,n2)
            elif operador == '-': resultado = calculadora.sub(n1,n2)
            elif operador == '*': resultado = calculadora.mult(n1,n2)
            elif operador == '/': resultado = calculadora.div(n1,n2)
            self.conn.sendall(str(resultado).encode())
        except :
            print("Fazz o L")


if __name__ == '__main__':
    servidor = TCPserver()
    while True:
        data = servidor.getRequest()
        if not data: break
        servidor.sendResponse(data)