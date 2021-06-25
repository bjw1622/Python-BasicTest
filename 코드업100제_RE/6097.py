a,b = map(int,input().split())
number = int(input())
result = []

#방 갯수 미리 잡아놓기
index = [0] * number
for i in range(a+1):
    result.append([])
    for j in range(b+1):
        result[i].append(0)

for i in range(number):
    index[i]=list(map(int,input().split()))

for i in range(number):
    #가로
    if index[i][1] == 0:
        for j in range(index[i][0]):
            result[ index[i][2] ] [ index[i][3] + j] = 1
    #세로
    else:
        for j in range(index[i][0]):
            result[ index[i][2] + j ] [ index[i][3] ] = 1
#출력
for i in range(1,a+1):
    for j in range(1,b+1):
        print(result[i][j],end =" ")
    print()