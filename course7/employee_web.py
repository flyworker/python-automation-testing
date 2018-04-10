from flask import Flask, jsonify
import pymysql
import csv
import os
from time import gmtime, strftime

domain = ""
user = ""
password = user
db_name = ""

app = Flask(__name__)


@app.route('/')
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
    cursor.close()
    db.close()

    # reading file content into list
    headers = ['ID', 'Name']
    delimiter = ","
    print(results)

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
        table += "".join(["<th>" + cell + "</th>" for cell in headers])
    else:
        table += "".join(["<th>" + cell + "</th>" for cell in results])

    # Converting csv to html row by row
    for row in results:
        table += "<tr>" + "".join(["<td>" + str(cell) + "</td>" for cell in row]) + "</tr>" + "\n"
    table += "</table><br>"
    footer = '''
        </body>
        </html>
            '''
    return table + footer
    # r = [dict((cur.description[i][0], value)
    #           for i, value in enumerate(row)) for row in cur.fetchall()]
    # return jsonify({'myCollection' : r})

if __name__ == '__main__':

    app.run()