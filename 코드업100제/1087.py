sum = 0
a = int(input())
i = 1
while True:
    sum += i
    if sum >= a:
        break
    else:
        i += 1
print(sum)