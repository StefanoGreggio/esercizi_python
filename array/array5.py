import sys

s=""

for i in range(len(sys.argv)-1):
    s+=sys.argv[i+1]+ " "

print(s)