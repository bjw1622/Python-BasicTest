a,b = input().split(" ")
a = int(a)
b = int(b)
i = 1
j = 1
while i <= a:
    while j <= b:
        print(i,j)
        j += 1
    i += 1
    j = 1