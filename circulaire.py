import math as mt
 
def premier(n):
    if n == 2:
        return True
    etat = True
    for i in range(2, int(mt.sqrt(n))+2):
        if n % i == 0:
            etat = False
            break
    return etat
 
def circulaire(p, q):
    for i in range(p, q+1):
        if premier(i) == True:
            etat = True
            ch = str(i)
            k = 0
            while k < len(ch) and etat == True:
                ch = ch[-1]+ch[:len(ch)-1]
                if premier(int(ch)) == False:
                    etat = False
                    break
                k += 1
            if etat == True:
                print('nombre : ', i)
 
 
circulaire(100, 300)  