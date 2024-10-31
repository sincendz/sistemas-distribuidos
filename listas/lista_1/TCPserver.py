import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 50000  

def calculator(text):
    text = text.split("_")
    #print(text)
    if(text[0] == '+'): return float(text[1]) + float(text[2])
    elif(text[0] =='-'): return float(text[1]) - float(text[2])
    elif(text[0] =='.'): return float(text[1]) * float(text[2])
    elif(text[0] =='/'): return float(text[1]) / float(text[2])
    else: return 'operation not recognized'


def multiTh(conn,addr):
    with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #
                time.sleep(10)
                response = calculator(data.decode())
                conn.send(str(response).encode())
            print(f'Disc with {addr}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Cone with {addr}")
        thread = threading.Thread(target=multiTh,args=(conn,addr))
        thread.start()