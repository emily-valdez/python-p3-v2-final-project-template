import sqlite3

# this connects us to the database
CONN = sqlite3.connect('holidays.db')
# this creates a tool where we can talk to the database
CURSOR = CONN.cursor()





