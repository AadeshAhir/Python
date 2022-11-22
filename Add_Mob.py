import pymysql
print("Add New Mobile Data")
con=pymysql.connect(host='byueyfvwmbhnx91zo0ux-mysql.services.clever-cloud.com',user='ugwhg23oly5v9p5u',password='8zNi9kVnLlYYyKG5yjiz',database='byueyfvwmbhnx91zo0ux')
curs=con.cursor()   
try:

    mn=str(input("Enter a Model Name:- "))
    co=str(input("Enter a Company Name:- "))
    covt=str(input("Enter a Connectivity (4G/5G):- "))
    rm=int(input("Enter a Ram in GB:- "))
    ro=int(input("Enter a Rom in GB:- "))
    clr=str(input("Enter a Colour:- "))
    scrn=str(input("Enter a Screen Size in inch:- "))
    btr=str(input("Enter a Battery Capicity:- "))
    prs=str(input("Enter a Processer Name:- "))
    prc=str(input("Enter a Price:- "))
    rt=str(input("Rate (5 out of):- "))
    pr=input("Enter Purpose of Mobile:- ")
    print("Gathering Your Response pls Wait...")
    
    curs.execute("insert into MOBILES (ModelName,Company,Connectivity,Ram,Rom,Colour,Screen,Battery,Processer,Price,Rating,Purpose) values('%s','%s','%s','%d','%d','%s','%s','%s','%s','%s','%s','%s')" %(mn,co,covt,rm,ro,clr,scrn,btr,prs,prc,rt,pr))
    con.commit()

    print('New Device Added Succesfully Device:- %s,%s' %(co ,mn))
    

    con.close()    

except Exception as e:
    print("Fail")
    




