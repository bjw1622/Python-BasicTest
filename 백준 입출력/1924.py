x,y = map(int,input().split())
day = 0
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = 2

for i in range(x):
    if i in a:
        day += 31
    elif i in b:
        day += 30
    elif i == c:
        day += 28

day += y

if day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
elif day % 7 == 0:
    print("SUN")