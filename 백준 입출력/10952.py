while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0:
        break
    else:
        print(a[0] + a[1])
