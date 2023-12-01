# inverti stringa
import socket
import sys


def inverti(data, data2):
    n = len(data) - 1
    for i in range(len(data)):
        c = data[n]
        data2 = data2 + c
        n = n - 1
    return data2


if len(sys.argv) < 2:
    print("errore negli argomenti. argomenti: <porta>")
    exit()

HOST = ""
PORT = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)
while 1:
    conn, addr = s.accept()
    data2 = ""
    data = conn.recv(1024).decode()
    print("Client", addr, "::. \t" + data)
    data2 = inverti(data, data2)
    print("stringa inversa", addr, "::. \t" + data2)
    conn.send(data2.encode())

s.close()
