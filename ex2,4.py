import math
x, p, y = float(input()), float(input()), int(input())
n = 0
while x < y:
    x = x + (x * p / 100)
    x = math.floor(x)
    n += 1
print(f"{n} лет понадобится")

