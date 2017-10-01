import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import OnehotTransactions
import pymysql
from sqlalchemy import create_engine

password = "test123"


def insert_file():
    # df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
    df = pd.read_excel('/Users/ccao/Downloads/OnlineRetail.xlsx')
    print(df.columns)
    # Open database connection
    db = pymysql.connect("localhost", "root", password, "walmart")

    for i in df.index:
        np_df = df.as_matrix()
        insert_row(db, np_df[i])

    # disconnect from server
    db.close()


def insert_row(db, row):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO sales_order(InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country) \
       VALUES ('%s', '%s','%s','%s','%s','%s','%s','%s' )" % \
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()


def read_data():
    # dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
    #            ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
    #            ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
    #            ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
    #            ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
    #
    # oht = OnehotTransactions()
    # oht_ary = oht.fit(dataset).transform(dataset)
    # df = pd.DataFrame(oht_ary, columns=oht.columns_)
    # frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
    # rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
    # print(rules)
    # Open database connection
    engine = create_engine('mysql+pymysql://root:oracle9i@localhost:3306/walmart')

    df = pd.read_sql_query('SELECT * FROM sales_order', engine)
    print(df)
    print(df.index)
    print(df.describe())


    df['Description'] = df['Description'].str.strip()
    df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
    df['InvoiceNo'] = df['InvoiceNo'].astype('str')
    df = df[~df['InvoiceNo'].str.contains('C')]
    print(df.shape)
    basket = (df[df['Country'] == "France"]
              .groupby(['InvoiceNo', 'Description'])['Quantity']
              .sum().unstack().reset_index().fillna(0)
              .set_index('InvoiceNo'))

    basket_sets = basket.applymap(encode_units)
    basket_sets.drop('POSTAGE', inplace=True, axis=1)
    frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
    print(frequent_itemsets)
    # rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    # print(rules)
    # rules.head()
    # rules[(rules['lift'] >= 6) &
    #       (rules['confidence'] >= 0.8)]
    # basket['ALARM CLOCK BAKELIKE GREEN'].sum()


    # basket2 = (df[df['Country'] =="Germany"]
    #           .groupby(['InvoiceNo', 'Description'])['Quantity']
    #           .sum().unstack().reset_index().fillna(0)
    #           .set_index('InvoiceNo'))
    #
    # basket_sets2 = basket2.applymap(encode_units)
    # basket_sets2.drop('POSTAGE', inplace=True, axis=1)
    # frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
    # rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)
    #
    # rules2[ (rules2['lift'] >= 4) & (rules2['confidence'] >= 0.5)]


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


if __name__ == "__main__":
    # insert_file()
    read_data()
