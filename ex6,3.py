def check(text):
    sets = set() 
    for i in text.split():
        count = 0
        for j in i:
            if j in 'ауоыиэяюёе':
                count += 1
        sets.add(count)
    print(sets)
    if len(sets) == 1:
        return 'yes'
    return 'no'
    print(sets)

text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(check(text))