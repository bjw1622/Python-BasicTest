""""# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # 코드를 입력하세요.
     some_list_length = len(some_list)
     if some_list_length == 0 or some_list_length == 1:
         return some_list
     else:
        sub = some_list.pop()
        a =  some_list.insert(0,sub)
        return some_list
# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
"""

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # 코드를 입력하세요.
    if len(some_list) == 0 or len(some_list) ==1:
        return some_list

    else:
        return some_list[-1:] + flip(some_list[:-1])
# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

