a,b,c,d = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
i = 0
while i < d-1:
    a = a * b + c
    i += 1

print(a)