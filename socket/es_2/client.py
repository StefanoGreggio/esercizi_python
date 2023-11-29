import socket
import sys
file=open(sys.argv[1])
lettura=file.read()
HOST = ""    
PORT = 5009       
      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data2=""
s.send(lettura.encode())
data2 = s.recv(1024).decode()
print ('risposta::. \t'+data2)
file.close()
s.close()