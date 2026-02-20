for _ in range(int(input())):
    n,k = map(int,input().split())
    casinos = []
    for i in range(n):
        l,r,real = map(int,input().split())
        casinos.append((l,r,real))
    casinos.sort()
    for l,r,real in casinos:
        if l <= k and k <= r:
            k = max(k,real) 
    print(k)
