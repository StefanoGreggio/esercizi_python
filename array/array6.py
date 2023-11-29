import sys

def palindroma(stringa):
    t=stringa[len(stringa)::-1]
    if (t==stringa):
        return 1
    else:
        return -1
    
s=sys.argv[1]
print(palindroma(s))