matrix=[]
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)


for i in matrix:
    for j in i:
        if j==1:
            print(abs(2-(matrix.index(i)))+abs(2-(i.index(j))))
            break
          
    
