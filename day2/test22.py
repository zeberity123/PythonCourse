def dict_input(ppl_dict):
    name = input("이름: ")
    age = input("나이: ")
    city = input("주소: ")
    ppl_dict[name] = [age, city]
    replay = input("계속 입력하시겠습니까(y/n)?")
    if replay == 'y':
        dict_input(ppl_dict)

def menu_input():
    print('1.입력')
    print('2.출력')
    print('3.검색')
    print('4.종료')
    return int(input("번호를 입력하세요: "))

menu = 1
ppl_dict = {}

while menu != 4:
    menu = menu_input()
    if menu == 1:
        dict_input(ppl_dict)
    elif menu == 2:
        print('-----------------')
        print('이름, 나이, 주소')
        for i in ppl_dict:
            print(f'{i}  {ppl_dict.get(i)[0]}  {ppl_dict.get(i)[1]}')
        print('-----------------')
        print('')
    elif menu == 3:
        name = input("검색할 이름을 입력하세요: ")
        if name in ppl_dict:
            print('-----------------')
            print('이름, 나이, 주소')
            print(f'{name}  {ppl_dict.get(name)[0]}  {ppl_dict.get(name)[1]}')
        print('-----------------')
        print('')
    elif menu == 4:
        break
    else:
        print("Wrong input!")