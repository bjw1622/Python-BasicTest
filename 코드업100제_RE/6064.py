a,b,c = map(int,input().split())

if a>c and b>c:
    print(c)
elif b>a and c>a:
    print(a)
elif a>b and c>b:
    print(b)
else:
    print(a)