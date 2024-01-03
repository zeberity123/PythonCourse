import os

inFp = None
fName = input("파일명을 입력하세요: ")

if os.path.exists(fName):
    inFp = open(fName, 'r', encoding='utf-8')

    inList = inFp.readlines()
    for i in inList:
        print(i, end='')

    inFp.close()
else:
    print(f'{fName} 파일이 없습니다.')