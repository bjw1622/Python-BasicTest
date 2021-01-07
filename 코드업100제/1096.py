#흰 돌 갯수 입력
b = int(input())

#바둑판 생성
a = [[0 for col in range(20)] for row in range(20)]

for i in range(b):
    c,d = input().split(" ") #여기서 좌표 입력받고 리스트에 추가하고
    c = int(c)
    d = int(d)
    a[c][d] = 1
#바둑판 출력
for i in range (1,20):
    for j in range (1,20):
        print(a[i][j],end = " ")
    print()
