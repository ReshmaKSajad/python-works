#module = its a python file...and consist of several functions
import pymysql
db = pymysql.connect(host = 'localhost',user = "root",password = "reshma@123",db = "database1")
#prepare cursor object using cursor() method
cur1 = db.cursor()
# sql = "create table person(ID int,NAME varchar(15))"
# sql = "insert into person values(101,'reshma')"
# sql = "insert into person values(102,'archana')"
# sql = "insert into person values(103,'arunima')"
# sql = "insert into person values(104,'nihana')"
# sql = "insert into person values(105,'salman')"
#sql = "update person set name = 'anju' where ID = 101"
#sql = "insert into person values(106,'sravan')"
#sql = "select * from person"
# sql = "select * from person"
# cur1.execute(sql)
# rows = cur1.fetchall()   #fetch all records from the table
# print( "ID  NAME")
# for i in rows:
#     print(i[0],i[1])
# db.commit()

# sql = "select NAME from person"
# cur1.execute(sql)
# rows = cur1.fetchall()   #fetch all records from the table
# print( "NAME")
# for i in rows:
#     print(i[0])
# db.commit()

# sql = "select * from person"
# cur1.execute(sql)
# row = cur1.fetchone()    #fetch only the first record from the table
# print("ID  NAME")
# if row:
#     print(row[0],row[1])




