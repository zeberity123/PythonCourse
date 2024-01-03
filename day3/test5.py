def para_func(*para):
    result = 0
    for num in para:
        result = result + num
    
    return result

hap = 0

hap = para_func(10, 20)
print("매개변수 2개 함수 호출 결과==>%d" % hap)
hap = para_func(10, 20, 30)
print(f'매개변수 3개 함수 호출 결과==> {hap}')