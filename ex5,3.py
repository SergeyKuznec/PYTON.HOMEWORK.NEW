strok = input('введите строку:  ')
strok = list(strok)
#print(len(strok))
l = len(strok)
new_str = []
s = 1
#if strok[1] != strok[0]:
#    new_str.append(str(1) + str(strok[0]))
for i in range(1, l):
    if strok[i] == strok[i-1]:
        s += 1
    else:
        new_str.append(str(s) + str(strok[i-1]))
        s = 1
new_str.append(str(s) + str(strok[l-1]))
print(''.join(new_str))