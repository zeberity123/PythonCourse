import sqlite3

con, cur = None, None
data1, data2, data3, data4='','','',''

sql=''
con = sqlite3.connect("naver1DB")
cur = con.cursor()

# cur.execute("create table userTable(id char(4), userName char(15), email char(15), birthYear int)")

while True:
    data1= input("사용자ID==> ")
    if data1=='':
        break
    data2 = input("사용자이름==> ")
    data3 = input("사용자 이메일==> ")
    data4 = input("사용자 출생년도==> ")
    # sql = f'INSERT INTO userTable VALUES("{data1}, {data2}, {data3}, {data4}")'
    sql = "INSERT INTO userTable VALUES('"+data1+"', '"+data2+"', '"+data3+"', "+data4+")"
    cur.execute(sql)

con.commit()
cur.execute("SELECT * from userTable")
con.close()