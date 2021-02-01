i = 200
count = 0
while i < 601:
    if (i % 3 != 0 ):
        print(i , end = " ")
        count += 1
        if (count > 7):
            print()
            count = 0

    i += 1
