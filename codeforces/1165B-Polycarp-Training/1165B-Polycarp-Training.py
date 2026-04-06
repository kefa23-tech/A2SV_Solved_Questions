n = int(input())

nums = list(map(int,input().split()))

nums.sort()
k = 1
ans = 0
for i in range(n):

    if nums[i] >= k:
        ans+=1
        k+=1
print(ans)