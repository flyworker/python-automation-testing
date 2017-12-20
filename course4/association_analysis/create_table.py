import pymysql

domain = "192.168.88.188"
user = "blockchain"
password = user
db_name = "ccao"
db = pymysql.connect(domain, user, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
