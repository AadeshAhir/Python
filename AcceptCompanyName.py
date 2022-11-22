import pymysql

print("Search Mobiles with Price (Low to High)")

conm=input("Enter Company Name: ")
con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()  
try:
    curs.execute("select * from MOBILES where Company='%s' order by Price" %conm)
    data=curs.fetchall()

    print(data)
    con.close()   
    


except Exception as e:
    print("Not Found")