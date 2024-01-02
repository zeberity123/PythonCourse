parking = ['','','','','']

top = 0

w = 0

while w != 3:
    w = int(input("1:ParkIn, 2:ParkOut, 3:Quit "))
    if w == 1:
        if top == 5:
            print(f'Full')
            print(parking)
            continue
        parking[top] = f'car{top}'
        top += 1
    elif w == 2:
        if top == 0:
            print(f'Empty')
            print(parking)
            continue
        parking[top-1] = ''
        top -= 1
    else: print('Wrong input')
    print(parking)