for _ in range(int(input())):
    s = input()
    res = set()
    res.add("")
    left = len(s)-2
    right = len(s) -1
    while right > -1:
        if left != -1 and s[left] == s[right]:
            right = left -1
            left = right -1
        else:
            res.add(s[right])
            right-=1
            left-=1
    res = sorted(list(res))

    res= "".join(res)
    print(res)
