n = int(input("введите натуральное число: "))
list_del = []
k = 0
for i in range(2,n):
    if n % i == 0:
        list_del.append(i)
    k +=1
print(list_del)
