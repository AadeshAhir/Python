import pymysql
print("UPDATE PURPOSE")
con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()
try:
    mon=input("Enter a Model Name: ")
    pur=input("Enter a Purpose: ")
    curs.execute('update MOBILES set Purpose="%s" where ModelName="%s"' %(pur,mon))
    con.commit()
    print("Updated")

    curs.execute('select * from MOBILES where ModelName="%s" ' %mon)
    data=curs.fetchone()
    print(data)

    con.close()



except Exception as e:
    print("Failed")