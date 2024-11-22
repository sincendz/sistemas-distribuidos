import socket
from  Calculadora import Calculadora
from CalculadoraCientifica import CalculadoraCientifica

HOST = "127.0.0.1"
PORT = 55555  

def calculator(text):
    text = text.split("_")
    operador = text[0]
    numero_1 = float(text[1])
    numero_2 = float(text[2])
    tipo_calculadora = text[3]
    resultado = 0
    if tipo_calculadora == 'CalculadoraSimples':
        calculadora = Calculadora()
        if operador == '+': resultado = calculadora.add(numero_1,numero_2)
        elif operador == '-': resultado = calculadora.sub(numero_1,numero_2)
        elif operador == '*': resultado =  calculadora.mult(numero_1,numero_2)
        elif operador == '/': resultado = calculadora.div(numero_1,numero_2)
    elif tipo_calculadora == 'CalculadoraCientifica':
        calculadora = CalculadoraCientifica()
        if operador == '**' : resultado = calculadora.potencia(numero_1,numero_2)
    return resultado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = calculator(data.decode())
            conn.send(str(response).encode())