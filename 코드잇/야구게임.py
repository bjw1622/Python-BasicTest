from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        a = randint(0,9)
        if a not in numbers:
            numbers.append(a)


    print("0과 9사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    count = 1
    while count < 4:
        a = int(input("{}번째 숫자를 입력하세요:".format(count)))
        if a not in new_guess and 0 <= a <= 9:
            new_guess.append(a)
            count += 1
        elif a in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        elif not 0 <= a <= 9:
            print("범위를 벗어나는 숫자입니다.다시 입력하세요.")
            continue
    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
    for i in range(3):
        if guess[i] in solution and guess[i] != solution[i]:
            ball_count +=1
    return strike_count, ball_count


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)