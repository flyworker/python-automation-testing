import pymysql


domain = "192.168.88.188"
user = "blockchain"
password = user
db_name = "ccao"
db = pymysql.connect(domain, user, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
