
n,k = map(int,input().split())

nums = list(map(int,input().split()))

uniques = 0

goods = 0

freqs = {}

left = 0
for right in range(n):
    if nums[right] not in freqs:
        freqs[nums[right]] = 1
        uniques +=1
    else:
        freqs[nums[right]] +=1

    while uniques > k:  
        freqs[nums[left]]-=1
        if freqs[nums[left]] == 0:
            del freqs[nums[left]]
            uniques-=1
        left+=1
    goods += right - left + 1
print(goods)
 
