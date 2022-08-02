def print_oper(operation, rows = 9, col = 9):
    for i in range(1, rows+1):
        print(*[operation(i, j) for j in range(1, col + 1)], sep = '\t')
print_oper(lambda x, y: x*y)