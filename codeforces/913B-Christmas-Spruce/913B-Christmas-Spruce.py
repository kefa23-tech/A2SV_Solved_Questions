from collections import defaultdict

n = int(input())


tree = defaultdict(list)
j = 2
for i in range(1,n):
    node = int(input())
    tree[node].append(j)
    j+=1
# print(tree)
valid = True
for node in tree:
    leafs = len(tree[node])
    for val in tree[node]:

        if val in tree:
            leafs-=1
        
        if leafs < 3:
            print("No")
            valid = False
            break
    if not valid:
        break

else:
    print("Yes")