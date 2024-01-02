## 함수 정의 부분
def para_func(*para) :
    result = 0
    for num in para :
        result = result + num
        
    return result

## 변수 선언 부분
hap = 0

## 메인 코드 부분
hap = para_func(10, 20)
print("매개변수 2개 함수 호출 결과 ==> %d" % hap)
hap = para_func(10, 20, 30)
print("매개변수 3개 함수 호출 결과 ==> %d" % hap)
