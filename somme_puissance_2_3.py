def somme_chiffres(N):
    NB = str(N)
    if len(NB) != 4:
        print("le nombre doit contenir 4 chiffres ")
    else:
        s = int(NB[0]) + int(NB[1]) + int(NB[2]) + int(NB[3])
        puis = 2
        while s < N and puis <= 5:
            s = int(NB[0])**puis + int(NB[1]) ** puis + \
                int(NB[2]) ** puis + int(NB[3]) ** puis
            puis += 1
 
        if s == N:
            return (True, puis)
        else:
            return (False, puis)