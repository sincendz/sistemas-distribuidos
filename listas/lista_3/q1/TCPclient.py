import socket
import os
#Calculadora remota que execute as 4 funções básicas (+,-,∙,÷).

OPERADORES = ['+','-','*','/','**']
TIPOS_CALCULADORA = ['CalculadoraSimples','CalculadoraCientifica']

def Input():
    #Ler o que o usuário escreveu
    userInput = input("Digite a operação matemática na seguinte ordem -> Operação_Number_Number_TipoCal : ")
    #Vai separar a string em um vetor
    userInputSplit = userInput.split('_')
    #tratamento de exceção caso o usuário passe uma string invalida
    try:
        operador = str(userInputSplit[0])
        numero_1 = float(userInputSplit[1])
        numero_2 = float(userInputSplit[2])
        tipoCalculadora = str(userInputSplit[3])

        if operador not in operador: # Operador que não existe
            raise Exception("Operador Invalido")
        if tipoCalculadora not in TIPOS_CALCULADORA: #Calculadora que não existe
            raise Exception("Tipo de calculadora invalida")

        if(operador == '**' and tipoCalculadora == "CalculadoraCientifica"):
            return userInput
        if(operador =='/' and numero_2 == 0):
            os.system('cls')
            print("não eh possivel fazer divisao por 0")
            return Input()
        return userInput
    except:
        print("malformed input")
        return Input()

def serverConnection(text):
    HOST = '127.0.0.1'
    PORT = 55555
    dados = text.encode()
    #print(dados)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.send(dados)
        data = s.recv(1024)
        print(f"Valor:  {data.decode()}")

def main():
    response = Input()
    serverConnection(response)
        
if __name__ == '__main__':
    main()