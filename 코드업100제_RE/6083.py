a,b,c=map(int,input().split())

l = []
sum = 0
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            sum += 1
            print(i,j,k)
print(sum)