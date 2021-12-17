def ppcm(a,b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//pgcd(a,b)
 
# exemple d'utilisation:
print ppcm(56,42) # => affiche 168