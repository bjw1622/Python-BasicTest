phone = input("핸드폰 번호를 입력해주세요:")
number = ""
for i in range(0,11):
    if i == 2:
        number += (phone[2]+"-")
    elif i == 6:
        number += (phone[6]+"-")
    else:
        number += phone[i]

print(number)