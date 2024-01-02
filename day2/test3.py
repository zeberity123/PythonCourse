i, hap = 0, 0
num1, num2, num3 = 0, 0, 0

num1 = int(input("start"))
num2 = int(input("end"))
num3 = int(input("inc"))

for i in range(num1, num2+1, num3):
    hap = hap + i

print(f'{num1}에서 {num2}까지 {num3}씩 증가함 값의 합 {hap}')