## 변수 선언 부분
i, k, ch, starNum = 0, 0, 0, 0
numStr,  starStr =  "", ""

## 메인(main) 코드 부분
numStr=input("숫자를 여러개 입력하세요 : ")
print("")

i=0
ch = numStr[i]
while True :
    starNum = int(ch)

    starStr = ""
    for k in range (0, starNum) :
        starStr += "\u2665"
        k += 1
        
    print(starStr)

    i += 1
    if (i > len(numStr) -1 ) :
        break

    ch = numStr[i]
    
