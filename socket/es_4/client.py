import socket
import sys


if len(sys.argv) < 5:
    print("errore negli argomenti. argomenti: <stringa1> <stringa2> <indirizzo> <porta>")
    exit()

PORT = sys.argv[4]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[3], int(PORT)))
stringa1 = sys.argv[1]
stringa2=sys.argv[2]
s.send(stringa1.encode())
s.send(stringa2.encode())
stringa1 = s.recv(1024).decode()
stringa2= s.recv(1024).decode()
print("stringa 1 invertita: \t" + stringa1+"\nstringa 2 invertita: "+stringa2)
s.close()
