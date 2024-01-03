outFp = None
outStr=''
outFp = open('day3/wtest.txt', 'w', encoding='utf-8')

while True:
    outStr = input("내용 입력: ")
    if outStr != '':
        outFp.writelines(outStr+'\n')
    else:
        break

outFp.close()
print("=)")