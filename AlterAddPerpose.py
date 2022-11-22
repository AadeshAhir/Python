import pymysql
print("Add Perpose Column using alter")
con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()
try:
    curs.execute("alter table MOBILES add Purpose varchar(50)")
    con.commit()
    print("Column Added")


except Exception as e:
    print("Failed")