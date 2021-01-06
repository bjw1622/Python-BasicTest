a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

day = 1
while True:
    if (day % a == 0 and day % b == 0 and day % c == 0 ):
        break
    else:
        day += 1

print(day)
