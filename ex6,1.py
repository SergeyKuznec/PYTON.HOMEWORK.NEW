Transformation = lambda x: x*1
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(Transformation, values))
if values == transformed_values:
    print('OK')
else:
    print('no')