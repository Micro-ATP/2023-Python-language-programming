piDividedByFour = 0
item = 1
n = 1

while abs(item) >= 10**(-5):
    piDividedByFour += item
    n += 2
    item = (-1) ** (n // 2) * (1 / n)

piDividedByFour *= 4

print("π的近似值:", piDividedByFour)
