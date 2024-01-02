animals = {
    "개" : "강아지",
    "호랑이" : "개호주",
    "곰" : "능소니",
    "말" : "망아지",
    "닭" : "병아리",
    "고등어" : "고도리",
    "명태" : "노가리"
}

while (True):
    myfood = input(str(list(animals.keys())) + " which ")
    if myfood in animals:
        print("<%s> : <%s>." % (myfood, animals.get(myfood)))
    elif myfood == "끝":
        break
    else :
        print("no list")
        