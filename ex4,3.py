l = input("введите последовательность чисел через пробел  ").split()
print(l)
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)