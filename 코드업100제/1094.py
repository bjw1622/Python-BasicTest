a = int(input())
b = input().split()

list = []

for i in range(a):
    list.append(int(b[i]))
list.reverse()

for i in list:
    print(i,end = " ")