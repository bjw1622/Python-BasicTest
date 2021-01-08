a = [[0]*10 for i in range(10)]
for i in range(10):
    a[i]= list(map(int,input().split()))

x=y=1
while True:
    if a[x][y]==0:
        a[x][y]=9
        if x==8 and y==8:
            break
        y+=1        
    elif a[x][y]==1:
        y-=1
        x+=1
    else : # 2일때
        a[x][y]=9
        break        
for i in range(10):
    print(*a[i])