a = list(input())
b = 0
for i in a:
    if b == 0:
        print("["+str(int(i)*10000)+"]")
    elif b == 1:
        print("["+str(int(i)*1000)+"]")
    elif b == 2:
        print("["+str(int(i)*100)+"]")
    elif b == 3:
        print("["+str(int(i)*10)+"]")
    elif b == 4:
        print("["+str(int(i)*1)+"]")
    else:
        break
    b += 1


