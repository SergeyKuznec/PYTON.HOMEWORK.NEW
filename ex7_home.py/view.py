from logger import input_data, print_data
 
def interf():
    com = int(input('что вы хотите: 1 - записать данные? 2 - вывести данные?'))
    if com == 1:
        input_data()
    if com == 2:
        print_data()