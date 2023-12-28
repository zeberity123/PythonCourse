a = int(input("키를 입력하세요(cm): "))
b = float(input("몸무게를 입력하세요(kg): "))
bmi = (b/((a - 100) * 0.85)) * 100
if bmi <= 90:
    print("결과 : 저체중")
elif (bmi > 90 and bmi <= 110):
    print("결과 : 정상")
elif (bmi > 110 and bmi <= 120):
    print("결과 : 과체중")
else:
    print("결과 : 비만")



c = int(input("약수를 출력할 숫자를 입력하세요 : "))
div = []
for i in range(1, c+1):
    if c % i == 0:
        div.append(i)
print(f'{c}의 약수는 {div} 입니다')



print("세 개의 수를 입력해주세요")
d = int(input("첫 번째 수: "))
e = int(input("두 번째 수: "))
f = int(input("세 번째 수: "))
print(f'{d}, {e}, {f} 중 가장 큰 수는 {max([d, e, f])}입니다')



g = int(input("1부터 N까지의 합을 구할 숫자 N을 입력해주세요 : "))
sum = 0
for i in range(1, g+1):
    sum+=i
print(f'1부터 {g}까지의 합은 {sum} 입니다')



print('==================================')
data = []
for i in range(1, 10):
    for j in range(1, 4):
        data.append(f'{j}x{i}= {j*i}')
    print(data)
    data = []
print('==================================')
for i in range(1, 10):
    for j in range(4, 7):
        data.append(f'{j}x{i}= {j*i}')
    print(data)
    data = []
print('==================================')
for i in range(1, 10):
    for j in range(7, 10):
        data.append(f'{j}x{i}= {j*i}')
    print(data)
    data = []
print('==================================')