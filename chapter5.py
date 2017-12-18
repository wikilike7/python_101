for n in [1, 2, 3, 4, 5]:
    print(n)


for i in range(1, 10):
    print(i)


a_dict = {'1': 'one', '2': 'two', '3': 'three'}
keys = a_dict.keys()
keys = sorted(keys)
for keys in a_dict:
    print(keys + ': ' + str(a_dict[keys]))


i = 0
while i < 10:
    if i % 2 != 0:
        print(i)
    i += 1


n = 0
while n < 10:
    if n == 5:
        continue
    print(n)
    n += 1

