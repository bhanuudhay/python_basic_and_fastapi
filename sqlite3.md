# import sqlite3

con = splite3.connect("databse_name) # establish connection

cur = con.cursor() # yeh database se directly baat kar skta hai queries ke format meh

cur.execute("Select name from table_name")
