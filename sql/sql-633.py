# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3
import traceback

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Francico', 'CA', 800000)")
    #commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try Again..."
    traceback.print_exc()
    #close the database connection
    conn.close()
