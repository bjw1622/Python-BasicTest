a,b,c = map(int,input().split())
l = []
l.append(a)
l.append(b)
l.append(c)

for i in l:
    if i % 2 ==0:
        print("even")
    else:
        print("odd")