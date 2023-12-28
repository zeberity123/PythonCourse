a = int(input("첫번째 수를 입력하세요 : "))
b = input("계산할 연산자를 입력하세요 : ")
c = int(input("두번째 수를 입력하세요 : "))
ans = 0
if b == '+':
    ans = a + c
elif b == '-':
    ans = a - c
elif b == '*':
    ans = a * c
elif b == '/':
    ans = a / c
elif b == '%':
    ans = a % c
elif b == '//':
    ans = a // c
elif b == '**':
    ans = a**c
else:
    print(f'알 수 없는 연산자 입니다.')

print(f'{a} {b} {c} = {ans}')