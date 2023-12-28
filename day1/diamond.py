a = 11
iter = a//2
for i in range(iter):
    print(' ' * (iter - i), end = '')
    print('*' * (2*i+1))

for i in range(iter-1):
    print(' ' * (i + 2), end = '')
    print('*' * ((iter*2)-3-2*i))
