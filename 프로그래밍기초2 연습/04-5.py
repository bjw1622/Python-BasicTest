print("-" * 50)
print("킬로그램(kg) 파운드(pd) 온스(oz)")
print("-" * 50)

for kg in range(10,101,5):
    pd = kg * 2.204623
    oz = kg * 35.273062
    print(f"{kg:3d} {pd:3.1f} {oz:3.1f}")

print("-" * 50)