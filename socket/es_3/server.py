# conta caratteri
import socket


def ContaCaratteri(stringa, carattere):
    conta = 0
    n = 0
    for i in range(len(stringa)):
        if stringa[n] == carattere:
            conta = conta + 1
        n = n + 1
    return conta


HOST = ""
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conta = 0
    conn = s.accept()
    stringa = conn.recv(1024).decode()
    print(stringa)
    carattere = conn.recv(1).decode()
    print(carattere)
    conta = ContaCaratteri(stringa, carattere)
    print(conta)
    conn.send(conta)

s.close()
