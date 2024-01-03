import sqlite3

def print_menu():
    menu_list = ['입력', '보기', '삭제', '수정', '검색', '정렬', '저장', '종료']
    print("==========================")
    print("성적데이터 처리")
    print("==========================")
    for i in range(8):
        print(f'{i+1}. {menu_list[i]}')
    return int(input("메뉴를 선택하세요: "))

def run_menu(menu):
    if menu == 1: add_data()
    elif menu == 2: print_data()
    elif menu == 3: delete_data()
    elif menu == 4: manage_data()
    elif menu == 5: find_data()
    elif menu == 6: sort_data()
    elif menu == 7: save_data()
    elif menu == 8: return 8
    else:
        print('Wront input!')

def add_data():
    name = input("이름: ")
    s1 = input("국어: ")
    s2 = input("영어: ")
    s3 = input("수학: ")
    total = str(int(s1) + int(s2) + int(s3))
    avg = str(int(total)/3)
    sql = "INSERT INTO scores VALUES('"+name+"', "+s1+", "+s2+", "+s3+", "+total+", "+avg+")"
    cur.execute(sql)

def print_data():
    s1_list = []
    s2_list = []
    s3_list = []
    print("==========================")
    print("이름      국어      영어      수학     총점    평균")
    print("==========================")
    cur.execute("SELECT * from scores")
    while True:
        row=cur.fetchone()
        if row == None:
            break
        name = row[0]
        s1 = row[1]
        s2 = row[2]
        s3 = row[3]
        s1_list.append(s1)
        s2_list.append(s2)
        s3_list.append(s3)
        total = row[4]
        avg = row[5]
        print(f'{name}    {s1}    {s2}    {s3}    {total}   {avg}')
    
    s1_avg = sum(s1_list)/len(s1_list)
    s2_avg = sum(s2_list)/len(s2_list)
    s3_avg = sum(s3_list)/len(s3_list)
    print(f'과목별 평균  {s1_avg}  {s2_avg}  {s3_avg}')

def delete_data():
    name = input("\n삭제할 이름을 입력하세요")
    cur.execute(f'delete from scores where name = "{name}"')
    

def manage_data():
    print('=(')

def find_data():
    name = input("\n검색할 이름을 입력하세요")
    cur.execute(f'select * from scores where name = "{name}"')
    row=cur.fetchone()
    if row != None:
        print("==========================")
        print("이름      국어      영어      수학     총점    평균")
        print("==========================")
        name = row[0]
        s1 = row[1]
        s2 = row[2]
        s3 = row[3]
        total = row[4]
        avg = row[5]
        print(f'{name}    {s1}    {s2}    {s3}    {total}   {avg}')
    else:
        print(f'no data found for: {name}!')

def sort_data():
    print('=(')

def save_data():
    con.commit()


####################################
con = sqlite3.connect("./39scoresDB")
cur = con.cursor()
cur.execute('select name from sqlite_master where type="table" and name="scores"')
result=cur.fetchall()
if len(result) == 0:
    cur.execute('create table scores(name char(8), s1 int, s2 int, s3 int, total int, avg int)')

menu = 0
while menu != 8:
    menu = print_menu()
    run_menu(menu)

con.close()