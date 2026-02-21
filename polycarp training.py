n = int(input())
contests = list(map(int, input().split()))

contests.sort()
k = 1
for problems in contests:
    if problems >= k:
        k+=1
print(k-1)
