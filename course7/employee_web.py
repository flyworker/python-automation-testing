import random

import names
from flask import Flask, jsonify, request, render_template
import pymysql
import csv
import os
from time import gmtime, strftime

domain = ""
user = ""
password = ""
db_name = ""

app = Flask(__name__)


def setup_connection(domain, password, user, db_name):
    db = pymysql.connect(domain, user, password, db_name)
    return db


def add_data(db, table_name, FirstName, LastName, AGE, Sex, Salary):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO %s (`FirstName`, `LastName`, `AGE`, `Sex`,`Salary`) VALUES ('%s','%s', '%s', '%s','%s')" \
          % (table_name, FirstName, LastName, AGE, Sex, Salary)
    # try:
    # Execute the SQL command
    cursor.execute(sql)
    cursor.close()
    db.commit()


@app.route('/employee')
def read_data_to_html():
    results = read_employee()

    # reading file content into list
    headers = ['ID', 'FirstName', 'LastName', 'AGE', 'Sex', 'Salary']
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


def read_employee():
    db = pymysql.connect(domain, user, password, db_name)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM EMPLOYEE"
    # try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results


def valid_login(username, password):
    results = read_employee()
    find_user = False
    for e in results:
        if e[1] == username:
            find_user = True
    return find_user


def log_the_user_in(user):
    print('User %s Success fully login' % user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = None
    status = None
    if request.method == 'POST':
        username = request.form['username']
        if valid_login(username,
                       request.form['password']):
            log_the_user_in(username)
            status = 'Success'
        else:
            status = 'User does not exist'

    return jsonify(
        username=username,
        status=status
    )


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    db = setup_connection(domain, user, password, db_name)
    status = None
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    sex = request.form['sex']
    salary = request.form['salary']

    add_data(db, 'EMPLOYEE', first_name, last_name, age, sex, salary)
    status = 'Success'
    return jsonify(
        first_name=first_name,
        last_name=last_name,
        status=status
    )


if __name__ == '__main__':
    app.run()
