n = int(input())
a = input().split()
li = []
for i in range(0,24):
    li.append(0)

for i in a:
    li[int(i)] += 1

for i in range(1,len(li)):
    print(li[i],end=" ")