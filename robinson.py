def robinson(n):
    U = 0
    for _ in range(1, n+1):
        ch = str(U)
        L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for chiffre in ch:
            L[int(chiffre)] += 1
        res = ''
        for j in range(9, -1, -1):
            if L[j] != 0:
                res += str(L[j])+str(j)
        U = int(res)
    print('Terme : ', n, ' est ', U)
 
 
robinson(5)