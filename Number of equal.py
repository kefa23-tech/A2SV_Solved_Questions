from collections import Counter
n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
if n > m:
    a = Counter(a)
    for num in b:
        if num in a:
            ans+=a[num]
else:
    b = Counter(b)
    for num in a:
        if num in b:
            ans+=b[num]
print(ans)
