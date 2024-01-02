ss='[<<<파<<이>>썬>>>]'
print(f'원 문자열 ==> {ss}')
ss = ss.replace('<', '')
ss = ss.replace('>', '')
print(f'<>제거 ==> {ss}')