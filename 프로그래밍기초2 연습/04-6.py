number = input("숫자를 입력하세요:")

sum = 0
for i in number:
    a = int(i)
    if (a % 2  != 0):
        sum  = sum + 1
print(f"입력된 숫자 중 홀수의 갯수 : {sum}개")