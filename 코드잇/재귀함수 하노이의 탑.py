def honoi(n,from_pos,to_pos,aux_pos):
    if n == 1:
        print(from_pos,"->",to_pos)
        return
    else:
        honoi(n-1,from_pos,aux_pos,to_pos)
        print(from_pos,"->",to_pos)
        honoi(n-1,aux_pos,to_pos,from_pos)
print("n=1")
honoi(1,1,3,2)
print("n=2")
honoi(2,1,3,2)
print("n=3")
honoi(3,1,3,2)
