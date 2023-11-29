array=[]
i=0
while i<10:
    x=input("inserisci un numero intero")
    array.append(x)
    i=i+1

for n in array:
    if int(n)%2==0:
        print(n)

for n in array:
    if int(n)%2 != 0:
        print(n)