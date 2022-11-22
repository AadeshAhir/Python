import pymysql
print("SEARCH RAM & ROM COMBINATION")
con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()
try:
    ra=int(input("Enter Ram: "))
    ro=int(input("Enter Rom: "))
    curs.execute("select * from MOBILES where Ram='%d' and Rom='%d'"%(ra,ro))
    data=curs.fetchall()
    print(data)
    con.close() 
   


except Exception as e:
    print("Combination Not Found")