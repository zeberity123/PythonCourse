aa = []
bb = []
value = 0

for i in range(0,200) :
    aa.append(value)
    value += 3

for i in range(0, 200) :
    bb.append(aa[199-i])

print(" bb[0]은 %d, bb[199]는 %d 입력됨 " % (bb[0], bb[199] ))
