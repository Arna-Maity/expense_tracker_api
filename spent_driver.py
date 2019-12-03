from docopt import docopt
from spent import *
from tabulate import tabulate

usage='''

    Expense Tracker CLI
    Usage:
        spent_driver.py init
        spent_driver.py view [<view_category>]
        spent_driver.py <amount> <category> [<message>]
'''

args = docopt(usage)
#print (args)

if args['init']:
    init()
    print("User profile created!")

if args['view']:
    category = args['<view_category>']
    amount, results = view(category)
    print(amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        #print(amount)
        log(amount,args['<category>'],args['<message>'])

    except:
        print(usage)


