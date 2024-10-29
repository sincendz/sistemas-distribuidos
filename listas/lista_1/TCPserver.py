import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def calculator(text):
    text = text.split("_")
    print(text)
    if(text[0] == '+'): return float(text[1]) + float(text[2])
    elif(text[0] =='-'): return float(text[1]) - float(text[2])
    elif(text[0] =='.'): return float(text[1]) * float(text[2])
    elif(text[0] =='/'): return float(text[1]) / float(text[2])
    else: return 'operation not recognized'

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