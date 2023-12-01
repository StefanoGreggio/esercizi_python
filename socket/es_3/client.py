import socket
import sys


if len(sys.argv) < 4:
    print("errore negli argomenti. argomenti: <file> <indirizzo> <porta>")
    exit()

file = open(sys.argv[1])
lettura = file.read()
PORT = int(sys.argv[3])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[2], PORT))
carattere = input("inserisci il carattere da ricercare nel testo ")
s.send(lettura.encode())
s.recv(1024)
s.send(carattere.encode())
conta = s.recv(1024).decode()
print("\n\til carattere " + carattere + " è stato trovato " + conta + " volte")
file.close()
s.close()
