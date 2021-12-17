#Exercice 1.1
n= int(input("donner la taille du sapin"))
while(n<0):
    n= int(input("donner la taille du sapin"))
ch=""
if(n>0):
    ch=ch+"^"
    print(ch)

for i in range(1,n,2):
    ch=ch+"^^"
    print(ch)