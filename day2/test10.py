myList=[30,10,20]
print(f'현재 리스트: {myList}')

myList.append(40)
print(f'append(40)후의 리스트: {myList}')

print(f'pop으로 추출한 값: {myList.pop()}')
print(f'pop()후의 리스트: {myList}')

myList.sort()
print(f'sort(): {myList}')

myList.reverse()
print(f'revers(): {myList}')

print(f'20: {myList.index(20)}')

myList.insert(2, 200)
print(f'insert(2, 200): {myList}')