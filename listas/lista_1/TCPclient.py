import socket
import os

operdores = ['+','-','.','/']
#Calculadora remota que execute as 4 funções básicas (+,-,∙,÷).

def Input():
    #Ler o que o usuário escreveu
    userInput = input("Digite a operação matemática na seguinte ordem -> Operação_Number_Number : ")
    #Vai separar a string em um vetor
    userInputSplit = userInput.split('_')
    if(userInputSplit[0]=='exit'):
        exit(1)
    #tratamento de exceção caso o usuário passe uma string invalida
    try:
        operador = str(userInputSplit[0]) 
        num_1 = float(userInputSplit[1]) #Garante que é um número
        num_2 = float(userInputSplit[2]) #Garante que é um número
        if operador not in operdores:
            print("   Operadores Válidos  ")
            print(".......Adição -> + ....")
            print("....Subtração -> - ....")
            print("Multiplicação -> . ....")
            print("......Divisão -> / ....")
            print(".......................")
            print("Digite exit para fechar")
            raise Exception ("invalid operator")
        if(userInputSplit[0] =='/' and float(userInputSplit[2]) == 0):
            raise Exception("it's not possible divide by 0")
        return userInput
    except Exception as exc:
        print("Digite exit para fechar")
        print(str(exc))
        return Input()

def serverConnection(text):
    HOST = '127.0.0.1'
    PORT = 50000
    dados = text.encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.send(dados)
        data = s.recv(1024)
        print(f"Valor:  {data.decode()}")

def main():
    while True:
        response = Input()
        serverConnection(response)        
if __name__ == '__main__':
    main()