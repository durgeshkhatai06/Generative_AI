import sqlite3

#connect to sqlite
connection  = sqlite3.connect("Student.db")

##Create a curso object to insert record,create table, retrive
cursor = connection.cursor()

#create the table
table_info= """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)


#insert some more records
cursor.execute('''Insert into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert into STUDENT values('Dipesh','DEVOPS','A',35)''')

##Disply all the records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
    
    
## Close  the connection
connection.commit()
connection.close()