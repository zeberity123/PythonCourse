inFp = None
inList = ''

loc = input("파일명을 입력하세요: ")
inFp = open(loc, 'r', encoding='utf-8')

inList=inFp.readlines()
for i in inList:
    print(i, end='')

inFp.close()