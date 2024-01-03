a = input('문자열을 입력하세요 : ')
w = ''
for i in a:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'): w+=i.lower()
    elif ord(i)>ord('a') and ord(i)<=ord('z'): w+=i.upper()
    else: w+=i
print(w)