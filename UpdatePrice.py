import pymysql
print("Update New Price")

con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()  
try:
    pid=int(input("Enter a Product ID: "))
    np=input("Enter New Price: ")
    curs.execute("update MOBILES set Price=%s where ProID=%d" %(np,pid))
    con.commit()
    curs.execute("select * from MOBILES where ProID=%d "%pid)
    data=curs.fetchone()
    print(data)

    con.close()
    

except Exception as e:
    print("Model Dose Not Exist")