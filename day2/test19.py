ss = input("input string: ")
print("output String: ", end='')

if ss.startswith('(')==False:
    print("(", end='')

print(ss, end='')

if ss.endswith('(')==False:
    print(")", end='')