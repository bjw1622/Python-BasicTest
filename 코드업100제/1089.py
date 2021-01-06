a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
i = 0
while i < c-1:
    a += b
    i += 1

print(a)