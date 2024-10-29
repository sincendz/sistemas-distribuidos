import socket
#Calculadora remota que execute as 4 funções básicas (+,-,∙,÷).
def Input():
    #Ler o que o usuário escreveu
    userInput = input("Digite a operação matemática na seguinte ordem -> Operação_Number_Number : ")
    #Vai separar a string em um vetor
    userInputSplit = userInput.split('_')
    #tratamento de exceção caso o usuário passe uma string invalida
    try:
        str(userInputSplit[0])
        float(userInputSplit[1])
        float(userInputSplit[2])
        return userInput
    except:
        print("malformed input")
        return Input()

def serverConnection(text):
    HOST = '127.0.0.1'
    PORT = 65432
    dados = text.encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.send(dados)
        data = s.recv(1024)
        #print(f"Received {data!r}")
        print(data)

def main():
    response = Input()
    serverConnection(response)
        
if __name__ == '__main__':
    main()