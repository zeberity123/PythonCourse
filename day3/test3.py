def add(var1, var2):
    return var1 + var2
def min(var1, var2):
    return var1 - var2
def mul(var1, var2):
    return var1 * var2
def div(var1, var2):
    return var1 / var2

res = 0
var1, var2, oper=0,0,''

oper = input("계산입력(+,-,*,/): ")
var1 = int(input("첫 번째 숫자 입력"))
var2 = int(input("두 번째 숫자 입력"))

if oper == '+':
    res = add(var1,var2)
elif oper == '-':
    res = min(var1,var2)
elif oper == '*':
    res = mul(var1,var2)
elif oper == '/':
    res = div(var1,var2)

print("## 계산기 %d %s %d = %d" % (var1, oper, var2, res))