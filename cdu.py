for i in range(100, 1000):
    ch = str(i)
    s = int(ch[0]) + int(ch[1]) + int(ch[2])
    p = int(ch[0]) * int(ch[1]) * int(ch[2])
    if p % s == 0:
        print(i)