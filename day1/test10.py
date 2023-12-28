import random
numbers = []
for num in range(10):
    numbers.append(random.randrange(0,10))

for i in range(10):
    if i not in numbers:
        print(f'no {i} in numbers')