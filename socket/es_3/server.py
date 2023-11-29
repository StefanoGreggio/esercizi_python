# conta caratteri
import socket


def ContaCaratteri(stringa, carattere):
    conta = 0
    i = 0
    while i < len(stringa):
        if stringa[i] == carattere:
            conta = conta + 1
    return conta


HOST = ""
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    print("Client", addr, "::. \t" + stringa)
    carattere = conn.recv(1).decode()
    conta = ContaCaratteri(stringa, carattere)
    print(conta)
    conn.send(conta.encode())

s.close()
