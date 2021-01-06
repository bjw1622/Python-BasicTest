a = int(input())

total = 0
i = 1

while i <= a:
    if i % 2 == 0:
        total += i
    i += 1
print(total)