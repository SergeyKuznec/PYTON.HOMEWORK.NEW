from create import surname_d, name_d, number_phone

def input_data():
    name = name_d()
    surname = surname_d()
    number = number_phone()
    vers = int(input('В каком варианте хотите записать данные?\n'
                     '1 - в столбик?\n'
                     '2 - в строку?  -- '))
    if vers == 1:
        with open('data_first.csv', 'a', encoding = 'utf-8') as file:
             file.write(f'{name}\n{surname}\n{numbere}\n\n')
    if vers == 2:
        with open('data_sec.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}; {surname}; {number}\n\n')

def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second
    input_data()
