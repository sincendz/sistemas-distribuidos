import socket

class TCPclient:
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None
        self.connect()

    def connect(self):
        """Estabelece conexão com o servidor."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            print(f"Conexão estabelecida com {self.host}:{self.port}")
        except socket.error as e:
            raise ConnectionError(f"Erro ao conectar ao servidor: {e}")
    
    def sendRequest(self, request: str):
        """Envia uma solicitação ao servidor."""
        if not self.socket:
            raise ConnectionError("O cliente não está conectado ao servidor.")
        try:
            self.socket.sendall(request.encode())
        except socket.error as e:
            raise ConnectionError(f"Erro ao enviar dados: {e}")

    def getResponse(self) -> str:
        """Recebe a resposta do servidor."""
        if not self.socket:
            raise ConnectionError("O cliente não está conectado ao servidor.")
        try:
            resposta = self.socket.recv(1024)
            return resposta.decode()
        except socket.error as e:
            raise ConnectionError(f"Erro ao receber dados: {e}")
    
    def close(self):
        """Fecha a conexão com o servidor."""
        if self.socket:
            try:
                self.socket.close()
                print("Conexão fechada.")
            except socket.error as e:
                raise ConnectionError(f"Erro ao fechar a conexão: {e}")
