#map에서 split() 안찍으면 하나씩의 요소들을 각각의 리스트에 저장.
N = int(input())
number = list(map(int,input()))
total = 0
for i in number:
    total += i
print(number[0])
print(number[1])
print(total)