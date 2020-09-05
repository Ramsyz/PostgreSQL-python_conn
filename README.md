# PostgreSQL-python_conn
Repo fro python postgreSQL

### Connecting to a Database
To connect to your database,create a connection object representing the database. 

Next, create a cursor object to help you in execution of your SQL statements.

`import psycopg2`

`con = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")`

`print("Database opened successfully")`

`cur = con.cursor()`

`cur.execute("SELECT first_name, last_name from actor")`

`rows = cur.fetchall()`

`for row in rows:`

    `print('first_name =', row[0])`
    
    `print('last_name =', row[1])`

`print('successful')`

`con.close`


### Inserting Data into Table

INSERT statement via the execute() method to add the data into the table.

`cur = con.cursor()`

`cur.execute("INSERT into language(language_id,name) VALUES(8,'Spanish')");`

`con.commit()`

`print("Record inserted successful")`

`con.close()`

### Update values in Table
cursor() function to create a cursor object.

Run the execute() method to execute the UPDATE statement with input values.

`cur = con.cursor()`

`cur.execute("UPDATE language set name = 'German' WHERE language_id=6")`

`con.commit()`

`print("Updated rows:", cur.rowcount)`


`cur = con.cursor()`

`cur.execute("SELECT * from language")`

`rows = cur.fetchall()`

`for row in rows:`

    `print('language_id =', row[0])`
    
   ` print('name =', row[1])`

`print('successful')`

### Delete Row
cursor object should be created by calling the cursor() function. 

Run the DELETE statement to perform the deletion.

`cur.execute('DELETE from language where language_id=8')`

`con.commit()`

`print('Total deleted rows: ', cur.rowcount)`

`cur = con.cursor()`

`cur.execute("SELECT * from language")`

`rows = cur.fetchall()`

`for row in rows:`

    `print('language_id =', row[0])`
    
   ` print('name =', row[1])`

`print('deletion success')`

`con.close()`



# Extract the table headers

`headers = [i[0] for i in cursor.description]`

`# Open CSV file for writing.`
 `csvFile = csv.writer(open(filePath + fileName, 'w', newline=''),`
                             `delimiter=',', lineterminator='\r\n',`
                            ` quoting=csv.QUOTE_ALL, escapechar='\\')`

`# Add the headers and data to the CSV file.`
 `csvFile.writerow(headers)`
 `csvFile.writerows(results)`
`
` # Message stating export successful.`
  
  `print("Data export successful.")`



