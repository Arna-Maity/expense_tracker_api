import sqlite3 as db
from datetime import datetime

# Context Manager for managing DB connections.


class dbConnectionManager():
    def __init__(self, name):
        self.dbname = name
        self.connection = None
        self.cur = None

    # Creating the DB connection.
    def __enter__(self):
        self.connection = db.connect(self.dbname)
        self.cur = self.connection.cursor()
        return self

    def eval(self, query):
        hand = manager.cur.execute(query)
        self.connection.commit()
        return hand

    # Closing the DB connection.
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


def init():
    '''
    Initialize a new database to store the expenditures.
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    with dbConnectionManager("spent.db") as manager:
        sql = '''
        CREATE TABLE IF NOT EXISTS expenses(
            amount NUMBER,
            category STRING,
            message STRING,
            date STRING
            )
        '''
        manager.eval(sql)


def log(amount, category, message=""):
    '''
    Log the expenditure in the database
    amount: Number
    category: String
    message(optional): String
    '''
    with dbConnectionManager("spent.db") as manager:
        date = str(datetime.now())
        sql = '''
        INSERT INTO expenses VALUES(
            {},
            '{}',
            '{}',
            '{}'
        )
        '''.format(amount, category, message, date)
        manager.eval(sql)


def view(category=None):
    '''
    Returns a list of all expenditures incurred,
    and the total expense. If a category is specified,
    it returns only the info from that category.
    '''

    with dbConnectionManager("spent.db") as manager:
        date = str(datetime.now())

        if category:
            sql = '''
            SELECT * FROM expenses WHERE category='{}'
            '''.format(category)

            sumq = '''
            SELECT SUM(amount) FROM expenses WHERE category='{}'
            '''.format(category)

        else:
            sql = '''
            SELECT * FROM expenses
            '''
            sumq = '''
            SELECT SUM(amount) FROM expenses
            '''
        results = manager.eval(sql).fetchall()
        tot_amt = manager.eval(sumq).fetchone()[0]
    return tot_amt, results
