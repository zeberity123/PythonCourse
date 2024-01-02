inStr, outStr='',''
count, i=0,0

inStr=input("문자열: ")
count=len(inStr)

for i in range(count):
    outStr+=inStr[count-(i+1)]

print("reverse-->  %s" % outStr)