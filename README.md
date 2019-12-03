## expense_tracker_api ##

This repo contains python APIs for the Expense Tracker Application

#### Implemented APIs ####

**init:** Function to initialize a new database file if it is not present and create a table *expenses*. This table is used to hold the expenses and the category of expenses made by a person.

**log:** Function to log or enter the expenditure made by the person into the *expenses* table.

**view:** Function to return the total amount spent by the person and also the list of category-wise expenditure made. 

#### Dependencies ####
Before trying to run the application make sure you have the following python packages installed.

- docopt
- tabulate
- sqlite3 (installed by default in most cases)

To install a python package use the following command:

> pip install *package_name*

Replace the *package_name* with the package you want to install.