with open("C:/intel/singer1.csv", "r") as inFp :
    with open("C:/intel/new_singer2.csv", "w") as outFp:
        header = inFp.readline()
        
        
        outFp.write(header)
        for inStr in inFp:
            inStr = inStr.strip()
            print(inStr)
            row_list = inStr.split(',')
            print(row_list)
            row_list[-1] = row_list[-1].replace('.', '/')
            height_str = "{0:.2f}".format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')
print('Save. OK~')






# data = [['song','sdfasd', '44'],['song','sdfasd', '44'],['song2','sdfasd', '44'],['song1','sdfasd', '44']]
# with open("C:/intel/tmp2.csv", "w") as outFp1:
    
#     for d in data: 
#         tmp =''       
#         tmp = ','.join(d)   
    
#         outFp1.write(tmp+"\n")

