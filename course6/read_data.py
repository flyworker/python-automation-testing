import pymysql
import csv
import os
from time import gmtime, strftime


domain = " "
user = " "
password = user
db_name = " "
start_date = '2017-04-19 18:50:47'
end_date = '2018-02-26 16:22:54'


def add_data(data):
    db = pymysql.connect(domain, user, password, db_name)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO `person` (`name`) VALUES ('%s')" % (data)
    # try:
    # Execute the SQL command
    cursor.execute(sql)
    cursor.close()
    db.commit()
    db.close()


def read_data():
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
    header = ['ID', 'Name']

    file_name = 'temp_employee' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '.csv'

    with open(file_name, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(header)
        for row in results:
            spamwriter.writerow(row)

    # Converting to html
    myheader = 'ID,Name'
    html_table = csv_to_html_table(file_name, myheader)
    text_file = open('employee-' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".html", "w")
    text_file.write(html_table)
    text_file.close()
    # except:
    #     print("Error: unable to fetch data")
    cursor.close()
    db.close()


def csv_to_html_table(fname, headers=None, delimiter=","):
    with open(fname) as f:
        content = f.readlines()
    # reading file content into list
    rows = [x.strip() for x in content]
    header = '''
    <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }
        
        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        
        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        </head>
        <body>

        <h2>Employee Report</h2>
    '''
    table = header + "<table>"
    # creating HTML header row if header is provided
    if headers is not None:
        table += "".join(["<th>" + cell + "</th>" for cell in headers.split(delimiter)])
    else:
        table += "".join(["<th>" + cell + "</th>" for cell in rows[0].split(delimiter)])
        rows = rows[1:]
    # Converting csv to html row by row
    for row in rows:
        table += "<tr>" + "".join(["<td>" + cell + "</td>" for cell in row.split(delimiter)]) + "</tr>" + "\n"
    table += "</table><br>"
    footer = '''
        </body>
        </html>
            '''
    return table + footer




def clean_up(dir_name,extension_name):
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(extension_name):
            os.remove(os.path.join(dir_name, item))

if __name__ == "__main__":
    clean_up('.','.csv')
    clean_up('.','.html')

    data = 'james'
    # add_data(data)

    read_data()
