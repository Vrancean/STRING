sir1 = str(input("Dati primul cuvint :"))
sir2 = str(input("Dati al doilea cuvint :"))
sir3 = str(input("Dati al treilea cuvint :"))
sir4 = str(input("Dati al patrulea cuvint :"))
cuvant=""
if (len(sir1)>2 and len(sir2)>2 and len(sir3)>2 and len(sir4)>2):
    cuvant+=sir1[0:2]+sir2[0]+sir3[0:3]+sir4[0:len(sir4)//2]
else:
    print("Dati un cuvint, cu mai mult decit 2 caractere")
print(cuvant)