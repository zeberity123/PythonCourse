## 함수 정의 부분
def func1() :
    a = 10 # 지역변수
    print("func1()에서 a의 값 %d" % a)

def func2() :
    print("func2()에서 a의 값 %d" % a)
    
## 변수 선언 부분
#a = 20 # 전역변수

## 메인 코드 부분
func1()
func2()
