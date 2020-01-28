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

    def eval(self,query):
        hand = manager.cur.execute(query)
        self.connection.commit()
        return hand.fetchall()

    # Closing the DB connection.
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.connection.close() 


def init():
    '''
    Initialize a new database to store the expenditures.
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS expenses(
        amount NUMBER,
        category STRING,
        message STRING,
        date STRING
        )
    '''

    cur.execute(sql)
    conn.commit()

def log(amount, category, message=""):
    '''
    Log the expenditure in the database
    amount: Number
    category: String
    message(optional): String
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    date = str(datetime.now())
    sql = '''
    INSERT INTO expenses VALUES(
        {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount,category,message,date)

    cur.execute(sql)
    conn.commit()

def view(category=None):
    '''
    Returns a list of all expenditures incurred, 
    and the total expense. If a category is specified,
    it returns only the info from that category. 
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
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
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sumq)
    tot_amt = cur.fetchone()[0]
    return tot_amt, results