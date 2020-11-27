cnp=str(input("Introduceti CNP-ul : "))
r=0
if (len(cnp)!=13) :
    print('Nu este corect')
else:
    for i in cnp :
        if ord(i) in range(48,58) :
            r+=1
    if (r==13) :
            print('Este corect')
    else:
            print('Nu este corect')            
