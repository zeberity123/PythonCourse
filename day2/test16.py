foods = {
    "떡볶이" : "오뎅",
    "짜장면" : "당무지",
    "라면" : "김치",
    "피자" : "피클"
}

while (True):
    myfood = input(str(list(foods.keys())) + " 중 좋아하는 것은? ")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else :
        print("no food")