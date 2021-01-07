array = [[0 for col in range(19)] for row in range(19)]

for i in range(19):
    a = list(map(int,input().split()))
    array[i] = a

n = int(input()) #뒤집을 수
for w in range(n) :
    x , y = map(int,input().split())
    for z in range(19) :
        if array[x-1][z] == 1 :array[x-1][z]=0
        else :array[x-1][z]=1
        if array[z][y-1] == 1 :array[z][y-1]=0
        else :array[z][y-1]=1

for z in array :
    for o in z :
        print(o,end=" ")
    print()