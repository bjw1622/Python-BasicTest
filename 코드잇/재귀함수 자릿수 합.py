"""

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if n < 10 : # 1의 자리
        return n
    elif n <100: # 10의 자리
        a = n//10
        return sum_digits(n-a*10)+(n // 10)
    elif n <1000: # 100의 자리
        a = n // 100
        return sum_digits(n-a*100) + (n//100)
    elif n < 10000: # 1000의 자리
        a = n // 1000
        return sum_digits(n-a*1000) + (n//1000)
    elif n < 100000:
        a = n// 10000
        return sum_digits(n - a*10000) + (n//10000)
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
"""

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # base case
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))