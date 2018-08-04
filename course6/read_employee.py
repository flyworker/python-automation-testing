import random
import names
import pymysql


def read_data(db, table_name):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = 'select * from %s' % table_name
    # try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    return results


def add_data(db, table_name, FirstName, LastName, AGE, Sex, Salary):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO %s (`FirstName`, `LastName`, `AGE`, `Sex`,`Salary`) VALUES ('%s','%s', '%d', '%s','%d')" \
          % (table_name, FirstName, LastName, AGE, Sex,Salary)
    # try:
    # Execute the SQL command
    cursor.execute(sql)
    cursor.close()
    db.commit()


def setup_connection(domain, password, user, db_name):
    db = pymysql.connect(domain, user, password, db_name)
    return db


if __name__ == '__main__':
    db = setup_connection('192.168.88.188', 'blockchain', 'blockchain', 'ccao')
    print(read_data(db, 'EMPLOYEE')[-1])
    add_data(db, 'EMPLOYEE', names.get_first_name(), names.get_last_name(), random.randint(18, 67), 'm',random.randint(2000, 6000))
    print(read_data(db, 'EMPLOYEE')[-1])
    db.close()
