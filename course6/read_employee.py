import pymysql


def read_data(domain=None, user=None, password=None, db_name=None):
    db = pymysql.connect(domain, user, password, db_name)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM ccao.person"
    # try:
    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    return results

if __name__ == '__main__':
    pass