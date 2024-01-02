for i in range(9, 1, -1):
    print(f'# {i}단 # ', end='')
print('')
for i in range(9, 0, -1):
    for j in range(9,1, -1):
        print('%dX %d=%2d ' % (j, i, i*j), end='')
    print('')
