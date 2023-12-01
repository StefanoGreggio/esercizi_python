import socket
import sys


if len(sys.argv) < 4:
    print("errore negli argomenti. argomenti: <file> <indirizzo> <porta>")
    exit()

file = open(sys.argv[1])
lettura = file.read()
PORT = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[2], PORT))
data2 = ""
s.send(lettura.encode())
data2 = s.recv(1024).decode()
print("risposta::. \t" + data2)
file.close()
s.close()
