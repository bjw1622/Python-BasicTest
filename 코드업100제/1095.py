a = int(input())
b = input().split()

list = []

for i in range(a):
    list.append(int(b[i]))
list.sort()

print(list[0])