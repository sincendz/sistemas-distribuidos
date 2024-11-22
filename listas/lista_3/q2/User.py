from TCPclient import TCPclient

OPERADORES = ['+', '-', '*', '/', '**']

def string_input(stg: str) -> bool:
    stg = stg.split('_')

    operador = stg[0]

    if len(stg) < 2:
        print("Erro: formato de entrada inválido. Use OPR_NUM_NUM ou OPR_NUM.")
        return False

    if operador not in OPERADORES:
        print(f"Erro: operador '{operador}' não suportado.")
        return False

    try:
        numeros = [float(num) for num in stg[1:]]
    except ValueError:
        print("Erro: os valores após o operador precisam ser números.")
        return False

    if operador in ['+', '-', '*', '/'] and len(numeros) != 2:
        print("Erro: são necessários dois números para essa operação binária.")
        return False
    elif operador == '**' and len(numeros) != 1:
        print("Erro: a operação unária '**' precisa de apenas um número.")
        return False

    return True

def user_menu():
    print("** DIGITE A OPERAÇÃO MATEMÁTICA QUE DESEJA CALCULAR ****")
    print("** OPERAÇÕES BINÁRIAS: OPR_NUM_NUM ********************")
    print("** OPERAÇÕES UNÁRIAS: OPR_NUM *************************")

def main():
    HOST = '127.0.0.1'
    PORT = 50_000
    cliente = TCPclient(HOST, PORT)
    
    while True:
        user_menu()
        user_input = input("Digite: ")
        if string_input(user_input):
            try:
                cliente.sendRequest(user_input)
                resposta = cliente.getResponse()
                print(f"Resultado: {resposta}")
            except Exception as e:
                print(f"Erro ao comunicar com o servidor: {e}")
            break 

if __name__ == '__main__':
    main()
