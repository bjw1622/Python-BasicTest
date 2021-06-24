a = int(input())
b = input().split()
li = []
for i in range(0,len(b)):
    li.append(int(b[i]))
li.reverse()
for i in li:
    print(i,end=" ")