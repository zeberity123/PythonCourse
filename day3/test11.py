inFp=None
inStr=''

inFp=open('C:\\Users\\Harmony08\\Desktop\\PythonCourse\\day3\\wtest.txt', 'r', encoding='utf-8')

inStr=inFp.readline()
print(inStr, end='')

inStr=inFp.readline()
print(inStr, end='')

inStr=inFp.readline()
print(inStr, end='')

inFp.close()