a = int(input("연도를 입력하세요 : "))

if(((a % 4 == 0) or (a % 400 == 0)) and (a % 100 != 0)):
    print(f'{a}년은 윤년입니다.')
else:
    print(f'{a}년은 윤년이 아닙니다.')