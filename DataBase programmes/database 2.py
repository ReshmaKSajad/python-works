import pymysql
db = pymysql.connect(host = "localhost",user = "root",password = "reshma@123",db = "database1")
cur1 = db.cursor()
#sql = "create table students_information(Adno int,Name varchar(20),Average int,Sex varchar(1),Scode int)"
#sql = "insert into students_information values(501,'R.Jain',98,'M',111)"
#sql = "insert into students_information values(545,'Kavitha',73,'F',333)"
#sql = "insert into students_information values(705,'K.Rashika',85,'F',111)"
#sql = "insert into students_information values(754,'Rahul Goel',60,'M',444)"
#sql = "insert into students_information values(892,'Sahil Jain',78,'M',333)"
#sql = "insert into students_information values(935,'Rohan Saini',85,'M',222)"
#sql = "insert into students_information values(955,'Anjali',64,'F',444)"
#sql = "insert into students_information values(983,'Sneha Aggarwal',80,'F',444)"

#1.display all students' information?

# sql = "select * from students_information"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("Adno  Name Avg Sex Scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#2.display Rohan Saini's information?

# sql = "select * from students_information where Adno = 935"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("Adno  Name Avg Sex Scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#3.display number of students in the table?

# sql = "select count(*) from students_information"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("count")
# for i in rows:
#     print(i[0])
# db.commit()

#4.display number of studfents in each sex?
# sql = "select sex,count(*) from students_information group by sex"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("count of students:")
# for i in rows:
#     print(i[0],i[1])
# db.commit()

#5.display students' information in ascending order using name?

# sql = "select * from students_information order by name asc"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("Adno Name avg sex scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#6.display students' information in descending order using average marks?

# sql = "select * from students_information order by average desc"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("Adno Name avg sex scode")
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

#7.display students' name starting with letter 'K'?

# sql = "select name from students_information where name like 'K%'"
# cur1.execute(sql)
# rows = cur1.fetchall()
# print("NAMES STARTING WITH LETTER 'K':")
# for i in rows:
#     print(i[0])
# db.commit()

#8.display students' information where name ends with 'l'?

sql = "select * from students_information where name like '%l'"
cur1.execute(sql)
rows = cur1.fetchall()
print("NAMES ENDING WITH LETTER 'l':")
for i in rows:
    print(i[0],i[1],i[2],i[3],i[4])
db.commit()


