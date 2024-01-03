inFp, outFp=None,None
inStr=''

inFp=open('c:/Windows/win.ini', 'r', encoding='utf-8')
outFp=open('day3/wtest.txt', 'w', encoding='utf-8')

inList = inFp.readlines()
for i in inList:
    outFp.writelines(i)
inFp.close()
outFp.close()
print('=)')