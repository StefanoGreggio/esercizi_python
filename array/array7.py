array=[]
while True:
    x=int(input("inserisci un numero\n"))

    if x==0:
        if (len(array)%2==0):
            print("dimensione array pari")
        else:
            print("dimensione array dispari")
        break
    if x>0:
        array.append(x)
    else:
        break