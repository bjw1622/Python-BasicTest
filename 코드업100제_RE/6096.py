d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    d[i] = list(map(int,input().split()))

number = int(input())
#행
result1=[]
#열
result2=[]

for i in range(number):
    a,b = map(int,input().split())
    result1.append(a)
    result2.append(b)
#행 바꾸기
for i in range (number):
    for j in range(19):
        if d[result1[i]-1][j] == 1:
            d[result1[i] - 1][j] = 0
        else:
            d[result1[i] - 1][j] = 1

#열 바꾸기
for i in range (number):
    for j in range(19):
        if d[j][result2[i]-1] == 1:
            d[j][result2[i]-1] = 0
        else:
            d[j][result2[i]-1] = 1

#정답출력
for i in range(19):
    for j in range(19):
        print(d[i][j],end=" ")
    print()