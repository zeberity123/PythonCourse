import sqlite3

# 변수 선언 부분
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql=""

# 메인 코드 부분
con = sqlite3.connect("naverDB")
cur = con.cursor()

while (True) :
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
    
con.commit()
con.close()
