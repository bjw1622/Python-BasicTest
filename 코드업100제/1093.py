
#출석 번호를 부른 횟수의 정수 n이 입력.
a = int(input())
#무작위로 부른 n개의 번호가 공백을 두고 저장
b = input().split()

list = []

for i in range(24):
    list.append(0)

for j in range(a):
    list[int(b[j])] += 1

for i in range(1,24):
    print(list[i] , end = " ")
