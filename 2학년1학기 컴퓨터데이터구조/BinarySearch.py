def find(L,target,start,end):
    if start > end:
        return -1

    mid = (start+end)//2
    if L[mid] == target:
        return mid
    if L[mid] < target:
        return find(L,target,mid+1,end)
    else:
        return find(L,target,start , mid-1)

L = []
L.append(5)
L.append(8)
L.append(10)
L.append(15)
L.append(20)
L.append(25)
L.append(30)
L.append(40)
L.append(50)
L.append(54)
L.append(66)
L.append(69)
L.append(83)
L.append(86)
L.append(90)

index = find(L,67,0,len(L)-1) #리스트 엘 전달 , 찾고자하는 값 전달
print(index)










