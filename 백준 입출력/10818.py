N = int(input())
number = list(map(int,input().split()))
number.sort()
print(f"{min(number)} {max(number)}")