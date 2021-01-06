h,b,c = input().split(" ")
h = int(h)
b = int(b)
c = int(c)
total = h*b*c

print("%.2f" %(total/(1024**2*8)),"MB")