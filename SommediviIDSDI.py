#Exercice 1.3
n= int(input("donner un entier positive"))
while(n<0):
    n= int(input("donner un entier positive"))
s=0
i=2
while(s==0 and i<n):
    if(n%i==0):
        s+=1
        break
    else: i+=1
if(s==0):
    print("{} est premier".format(n))
else : 
    s=0
    l=[]
    print("non premier")
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    print("les diviseursde {} sont {}".format(n,l))
    print("Somme des diviseurs de {} est {}".format(n,sum(l)))