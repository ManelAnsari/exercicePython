"""
Retourne la liste des diviseurs d'un entier
"""
def diviseurs(p):
    liste_diviseur=[]
    for i in range(1,p+1,1):
        if p%i==0:
            liste_diviseur.append(i)
    return liste_diviseur
 
n=int(input("Veuillez entrer un entier :"))

liste=[]
liste=diviseurs(n)
print(liste)