print("-" * 30)
print("  섭씨   화씨")
print("-" * 30)

c = -20
while c < 41:
    d = c * 9.0 / 5.0 + 32.0
    print(f"{c:3.0f} {d:3.1f}")
    c= c + 1
print("-" * 30)