a = int(input("교환할 돈은 얼마 : "))

coin = [500, 100, 50, 10]

for i in coin:
    print(f'{i}원짜리 ==> {a//i}개')
    a %= i
print(f'바꾸지못한 잔돈 ==> {a}원')