# conta caratteri
import socket
import sys


def ContaCaratteri(stringa, carattere):
    conta = 0
    for i in stringa:
        if i == carattere:
            conta = conta + 1
    return conta


if len(sys.argv) < 2:
    print("errore negli argomenti. argomenti: <porta>")
    exit()

HOST = ""
PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conta = 0
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    print("stringa ricevuta: " + stringa + "\n")
    conn.send(stringa.encode())
    carattere = conn.recv(1).decode()
    print("carattere ricevuto: " + carattere)
    conta = ContaCaratteri(stringa, carattere)
    print(conta)
    conn.send(str(conta).encode())
    conn.close()
s.close()
