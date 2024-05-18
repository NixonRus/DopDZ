a,b,c,d = 7,10,5,6

print('\t',5, '\t', 6)
for i in range(7, 11):
    for j in range(5,7):
        print(i, (f'{i * j}'), end='')
    print('')