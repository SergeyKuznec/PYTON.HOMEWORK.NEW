from random import randrange as rd
k = int(input("введите степень: "))
for i in range(k+1):
    print(f"{rd(0, 100)} * x **{k-i} + ", end = ' ')
print("= 0")