def parfait(n):#parfait(n) retourne True si le nombre est parfait ou False sinon
    s=0
    for i in range(1,n//2+1):
        if n % i ==0 :
            s=s+i
    if s==n:
        return True
    else:
        return False