a = int(input())
max1 = max2 = 0
while a != 0:
    if a > max1:
        max2 = max1
        max1 = a
    a = int(input())
print(max2)