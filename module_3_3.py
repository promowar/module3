def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(1, 2)
print_params(1, 2, 3, 4, 5)           #нарошная ошибка
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, True, 'logic']
values_dict = { 'a' : True , 'b' : 4829, 'c' : 'think'}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [False, 'galaxy']
print_params(*values_list2, 42)