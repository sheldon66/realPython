import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity = 3000 WHERE Model = 'D'")
    c.execute("UPDATE inventory SET quantity = 4000 WHERE Model = 'E'")

#print all the records
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    print "These are all the records"
    for r in rows:
        print r[0], r[1], r[2]
        print
#print the records that are for Ford vehicles
    c.execute("SELECT * FROM inventory WHERE Make = 'Ford'")
    rows = c.fetchall()
    print "These are the records that are for FOrd vehicles. "
    for r in rows:
        print r[0], r[1], r[2]
        print
