ef auto_nombre(N):
    etat = True
    for i in range(N):
        s = i
        M = str(i)
        for j in M:
            s += int(j)
        if s == N:
            etat = False
            break
 
    return etat