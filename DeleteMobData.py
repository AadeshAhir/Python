import pymysql
print("'DELETE MOBILE DATA'")

con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor() 

pid=int(input("Enter Product Id: " ))
curs.execute("select * from MOBILES where ProId=%s" %pid)
data=curs.fetchall() 
print(data)

print("Do you want to Delete?? Y or N")


try:
    ch=input("Enter Choice: ")
    
    if ch.upper()=="Y":
        curs.execute("delete from MOBILES where ProID=%d" %pid)
        con.commit()
        print("Deleted")
    elif ch.upper()=="N":
        print("No Change")

except Exception as e:
    print("No Data Found")