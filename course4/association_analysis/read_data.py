import pymysql

# Open database connection
domain = "192.168.88.188"
user = "blockchain"
password = user
db_name = "CDDSERVER"
db = pymysql.connect(domain, user, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM POLONIEX_HISTORICAL_CHART"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
       print(row)
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()