a,b,c,d = 3,10,2,8

print('', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print('')
for j in range(a, b + 1):
    print(j, end='\t')
    for k in range(c, d + 1):
        print(f'{j * k}', end='\t')
    print('')

