sel=int(input("입력진수 결정(16/10/8/2) : "))
if set != 16 and set != 10 and set != 8 and set !=2 :
    print("16, 10, 8, 2 숫자중 하나만 입력하세요.")
    exit();
num=input("값 입력 : ")

if sel==16 :
    num10=int(num, 16)
if sel==10 :
    num10=int(num, 10)
if sel==8 :
    num10=int(num, 8)
if sel==2 :
    num10=int(num, 2)
    
print("16진수 ==> ",hex(num10))
print("10진수 ==> ",num10)
print(" 8진수 ==> ",oct(num10))
print(" 2진수 ==> ",bin(num10))
