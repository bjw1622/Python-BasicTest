while True:
    try:
        a = list(map(int,input().split()))
    except:
        break
    if a[0] > 0 and a[1] < 10:
        print(a[0]+ a[1])