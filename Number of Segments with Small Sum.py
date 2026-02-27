n,s = map(int,input().split())

nums = list(map(int,input().split()))
left = 0

ans = len(nums)

seg = 0

for right in range(len(nums)):
    seg+=nums[right]
    
    if seg > s:
        while seg > s:
            seg-=nums[left]
            left+=1
    ans+=(right - left)
    # print("seg",seg)
    # print("ans",ans)
print(ans)

