import socket
import sys

file = open(sys.argv[1])
lettura = file.read()
HOST = ""
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
carattere = input("inserisci il carattere da ricercare nel testo ")
s.send(lettura.encode())
s.send(carattere.encode())
conta = s.recv(1024).decode()
print("\n\til carattere " + carattere + " è stato trovato " + conta + "volte")
file.close()
s.close()
