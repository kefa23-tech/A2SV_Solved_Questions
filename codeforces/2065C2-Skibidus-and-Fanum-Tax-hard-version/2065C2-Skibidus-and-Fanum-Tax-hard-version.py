import bisect
for _ in range(int(input())):

    n,m = map(int,input().split())
    
    a = list(map(int,input().split()))
    b_lis = list(map(int,input().split()))
    b_lis.sort()
    choice1 = a[0]
    choice2 = b_lis[0] - choice1
    prev = min(choice1,choice2)
    for i in range(1,n):

  
        orig = a[i]
        target = prev + orig
        idx = bisect.bisect_left(b_lis,target)
        
       
        new = b_lis[idx] - orig if idx < m else float("inf")
        choices = []
        # print("b",b)
        # print("orig",orig)
        # print("new",new)
        if orig >= prev :
            choices.append(orig)
        if idx < m:
            choices.append(new)
        if not choices:
            print("NO")
            break
        prev = min(choices)
    else:
        print("YES")
    # print(a)