number = int(input())
for i in range(number):
    a,b = map(int,input().split(" "))
    print(f"Case #{i+1}: {a+b}")