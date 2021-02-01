a = int(input("출력할 항의 개수:"))
list = []
i = 0
for i in range (0,a):
    if i ==0:
        list.append(0)
    elif i == 1:
        list.append(1)
    else:
        list.append(list[i-2]+list[i-1])

for i in list:
    print(list[i] , end = " ")

