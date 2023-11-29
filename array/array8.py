from statistics import mean

media=0

array=[]
while True:
    x=int(input("inserisci un numero. finire la sequenza di numeri inserendo 0\n"))

    if x==0:   
        media=mean(array)
        print("media: "+media+"\n")
    if x>0:
        array.append(x)    
    else:
        break




