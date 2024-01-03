import random

def getNumber():
    return random.randrange(1,46)

lotto = []
num = 0

print("**Lotto\n")
while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto)>=6:
        break

print("lotto==> ", end='')
lotto.sort()
for i in range(0,6):
    print("%d " % lotto[i], end='')