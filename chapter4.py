var1 = 141
if var1 < 10:
    print('less than 10')
elif var1 < 20:
    print('less than 20')
else:
    print('other contition')


my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print('x is not in the list, so this is True!')


empty_list = []
empty_tuple = ()
empty_string = ''
nothing = None

if not empty_list:
    print('it is an empty list!')

if not empty_tuple:
    print('it is an empty tuple')
