n = int(input('введите целое число: '))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"!= {f}")
