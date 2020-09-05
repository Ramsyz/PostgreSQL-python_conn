import psycopg2

con = psycopg2.connect(database = 'dvd_rental', user = 'postgres', password = 'postgresql',
                       host ='127.0.0.1', port='5432')
print("database connected")

#cur = con.cursor()
#cur.execute("SELECT first_name, last_name from actor")
#rows = cur.fetchall()

#for row in rows:
    #print('first_name =', row[0])
    #print('last_name =', row[1])
    #print('language =', row[2])

#print('successful')
#con.close


cur = con.cursor()
cur.execute("UPDATE language set name = 'German' WHERE language_id=6")
con.commit()
print("Updated rows:", cur.rowcount)
    
cur = con.cursor()
cur.execute("SELECT * from language")
rows = cur.fetchall()

for row in rows:
    print('language_id =', row[0])
    print('name =', row[1])
    #print('language =', row[2])

print('successful')
con.close

