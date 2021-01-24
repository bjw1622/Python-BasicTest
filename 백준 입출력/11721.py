sentence = list(map(str,input()))
count = 0
for i in range(0,len(sentence)):
    if count == 10:
        print()
        print(sentence[i],end = "")
        count = 1
    else:
        print(sentence[i],end = "")
        count += 1