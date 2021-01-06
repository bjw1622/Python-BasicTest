h,b,c,s = input().split(" ")
h = int(h)
b = int(b)
c = int(c)
s = int(s)
total = h*b*c*s

print("%.1f" %(total/(1024**2*8)),"MB")