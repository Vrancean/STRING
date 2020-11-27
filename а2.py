s=str(input('introduceti un sir de caractere : '))
nm=0
nc=0
ns=0
for i in s:
    if i.isupper():
        nm+=1
print(nm)
for i in s:
     if ord(i) in range(48,58):
        nc+=1
print(nc)        
for i in s:
    if ((ord(i) in range (32,48)) or (ord(i) in range(58,65)) or (ord(i) in range (91,9)) or (ord(i) in range (123,127))):
        ns+=1
print(ns)