n = input()
nums = list(map(int, input().split()))
nums.sort()

x = len(nums)//2
if len(nums)%2==0:
    print(nums[x-1])
else:
    print(nums[x])

