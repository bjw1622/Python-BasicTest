number = input("하이폰(-)을 포함한 휴대폰 번호를 입력하세요:")

for x in number:
    if x != "-":
        print(x,end="")