import socket, sys, json

PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], PORT))

dati = {}
dati["stringa"] = sys.argv[3]
dati["carattere"] = sys.argv[4]
s.send(json.dumps(dati).encode())

stringa = s.recv(len(sys.argv[3])).decode()

print("Stringa %s senza carattere: %c " % (stringa, sys.argv[4]))

s.close