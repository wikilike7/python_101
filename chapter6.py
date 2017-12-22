x = [1, 2, 3, 4, 5]
y = [int(i) for i in x ]
print(y)


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])


print({i: str(i) for i in range(10)})
