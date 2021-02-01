print("-" * 50)
print("센티미터(cm) 인치(inch) 피트(ft) 야드(yd)")
print("-" * 50)

for cm in range(10,201,10):
    inch = cm * 0.393701
    ft = cm * 0.032808
    yd = cm * 0.010936
    print(f"{cm:3d} {inch:8.1f} {ft:8.1f} {yd:8.1f}")

print("-" * 50)