N = int(input())
a = N - 1
for i in range(1,2*N):
    if i < N:
        print(" " * (N - i),end = "")
        print("*" * i)
    elif i == N:
        print("*" * N)
    else:
        print(" " * (N - a) ,end = "")
        print("*" * a )
        a = a - 1


