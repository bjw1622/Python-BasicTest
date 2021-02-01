first = int(input("첫 수를 입력하세요:"))
end = int(input("끝 수를 입력하세요:"))
want = int(input("합계를 구하고자 하는 배수를 입력하세요:"))
sum = 0
i = first
while (i < end + 1):
    if (i % want == 0):
        sum += i
    i += 1

print(f"{first}~{end}까지의 정수 중 {want}의 배수의 합계 : {sum}")