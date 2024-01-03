inFp, outFp=None,None
inStr=''

with open('day3/singer1.csv', 'r') as inFp:
    with open('day3/singer2.csv', 'w') as outFp:
        header = inFp.readline()

        outFp.write(header)
        for i in inFp:
            i = i.strip()
            row_list = i.split(',')
            row_list[-1] = row_list[-1].replace(',', '/')
            height_str = '{0:.2f}'.format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ','.join(map(str,row_list))
            outFp.write(row_str + '\n')
print('=)')