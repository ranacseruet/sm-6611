__author__ = 'india'

import pg8000
import psycopg

#bug_id = 0;


#cursor = conn.cursor()

authorname="kunwar"
bugid=1222
filename="concordir univeristy"

conn = None;
cursor = None;
conn = pg8000.connect(database="postgres", user="postgres", password="root", host="localhost")
cursor = conn.cursor()

def createTables():
    #cursor.execute("CREATE TABLE t1 (f1 int primary key, f2 int not null, f3 varchar(50) null)")
    cursor.execute("CREATE TABLE FileTable(ID serial NOT NULL PRIMARY KEY, filename varchar(250) null)")
    cursor.execute("CREATE TABLE AuthorTable (Author_ID VARCHAR(250) primary key, authorname varchar(50) null)")
    cursor.execute("CREATE TABLE BugTable (ID VARCHAR(250) primary key, bug_ID int not null)")
    cursor.execute("CREATE TABLE BugTable_FileTable (Bug_ID VARCHAR(250), bug_id int not null)")
    cursor.execute("CREATE TABLE AuthorTable_FileTable (Bug_ID VARCHAR(250), bug_id int not null)")

    conn.commit()
    return

def insert_filename(filename1):
    cursor.execute("INSERT INTO FileTable (filename) VALUES (%s)", (filename1))
    conn.commit()
    return

def insert_Author(authorname, filename):
    cursor.execute("INSERT INTO AuthorTable (filename, authorname) VALUES (%s, %s)", (filename, authorname))
    #cursor.execute("INSERT INTO t1 (f1, f2, f3) VALUES (%s, %s, %s)", (4, 1000, None))
    # results = cursor.fetchall()
    # for row in results:
    #      f1, f2, f3  = row

        # print("f1 = %s, f2 = %s, f3 = %s" % (f1, f2, f3))

    conn.commit()
    return

def insert_Bug(filename,bugid):
    cursor.execute("INSERT INTO BugTable (filename, bugid) VALUES (%s, %s)", (filename, bugid))
    return

#createTables()
insert_filename("Hello")
#insert_Author("kunwar","rattan")
#insert_Bug("kunwar",1234)
