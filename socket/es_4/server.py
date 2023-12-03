# inverti stringa
import socket
import sys


def inverti(stringa):
    str_invertita=""
    n = len(stringa) - 1
    for i in stringa:
        c = i
        str_invertita = str_invertita + c
        n = n - 1
    return str_invertita


if len(sys.argv) < 2:
    print("errore negli argomenti. argomenti: <porta>")
    exit()

HOST = ""
PORT = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, int(PORT)))
s.listen(6)
while 1:
    conn, addr = s.accept()
    stringa1 = ""
    stringa2 = ""
    stringa1 = conn.recv(1024).decode()
    stringa2 = conn.recv(1024).decode()
    str1_invertita = inverti(stringa1)
    str2_invertita=inverti(stringa2)
    print("stringa inversa", addr, "::. \t" + str1_invertita +" "+ str2_invertita)
    conn.send(str1_invertita.encode())
    conn.send(str2_invertita.encode())

s.close()
