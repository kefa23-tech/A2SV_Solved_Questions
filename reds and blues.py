for _ in range(int(input())):
    n = input()
    reds = list(map(int,input().split()))
    m = input()
    blues = list(map(int,input().split()))

    for i in range(1,len(reds)):
        reds[i]+=reds[i-1]

    for i in range(1,len(blues)):
        blues[i]+=blues[i-1]
    reds.append(0)
    blues.append(0)
    total = max(reds) + max(blues)

    print(total)

