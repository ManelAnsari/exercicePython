N = 10080
 
def nhc(n):
    liste_nhc = []
    for i in xrange(n, 0, -1):
        if n % i == 0:
            liste_nhc.append(i)
    return len(liste_nhc)
 
liste = [0]
for i in range(N+1):
    n_div = nhc(i)
    if n_div > max(liste):
        liste.append(n_div)
        print i,