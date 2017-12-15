for n in [1, 2, 3, 4, 5]:
    print(n)


for i in range(1, 10):
    print(i)


a_dict = {'1': 'one', '2': 'two', '3': 'three'}
keys = a_dict.keys()
keys = sorted(keys)
for keys in a_dict:
    print(keys + ': ' + str(a_dict[keys]))


