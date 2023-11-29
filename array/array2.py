i=0
array=[]
while i<5:
    x = [input("inserisci  numeri interi\n")]
    array.append(x)
    i=i+1

print(array[::-1])