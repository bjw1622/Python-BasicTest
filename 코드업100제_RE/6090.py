a,b,c,d = map(int,input().split())

num = 0
if d == 1:
    num = a
else:
    for i in range(0, d-1):
        num = a * b + c
        a = num

print(num)

