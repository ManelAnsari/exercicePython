#Exercice 3.1
def nombreDiviseur(x):
    s=0
    for i in range(1,x):
        if(x%i==0):
            s+=1
    return s