for x1 in (0,1):
    for x2 in (0,1):
        for x3 in (0,1):
            a = x1 <= x2 or x1 ^ x3
            print(x1,x2,x3, a)