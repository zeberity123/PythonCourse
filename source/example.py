inStr = "Python 1234 파이썬"
outStr = ""

for i in range(0, len(inStr)) :
    if  inStr[i].isdigit() == False  :
         outStr += inStr[i]

print("원  문자열 ==> " + '[' + inStr + ']')
print("숫자 제거 ==> " + '[' + outStr + ']')
