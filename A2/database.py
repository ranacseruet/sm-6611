__author__ = 'india'

import pg8000
import psycopg

#bug_id = 0;


#cursor = conn.cursor()

authorname="kunwar"
bugid=1222
filename="mila.txt"

conn = None;
cursor = None;
conn = pg8000.connect(database="postgres", user="postgres", password="root", host="localhost")
cursor = conn.cursor()

def createTables():
    cursor.execute("CREATE SEQUENCE FILE_id_seq")
    cursor.execute("CREATE TABLE FileTable(ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('FILE_id_seq'), filename varchar(250) NOT null UNIQUE )")
    cursor.execute("CREATE SEQUENCE Author_id_seq")
    cursor.execute("CREATE TABLE AuthorTable (Author_ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('Author_id_seq'), authorname varchar(250) not null UNIQUE)")
    cursor.execute("CREATE SEQUENCE BUG_id_seq")
    cursor.execute("CREATE TABLE BugTable (BUG_ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('BUG_id_seq'), bugID INT not null UNIQUE)")
    cursor.execute("CREATE SEQUENCE TABLE_id_seq")
    cursor.execute("CREATE TABLE BugTable_FileTable (TABLE_ID bigint NOT NULL DEFAULT NEXTVAL('TABLE_id_seq') , Bug_ID int NOT NULL REFERENCES BugTable(BUG_ID), File_ID int not null REFERENCES FileTable(ID), Author_ID INT not null REFERENCES AuthorTable(Author_ID))")
    conn.commit()
    return

def insert_filename(filename1):
    cursor.execute('INSERT INTO FileTable (filename) VALUES (%s)', (filename1))
    conn.commit()
    return

def insert_Author(authorname):
    cursor.execute("INSERT INTO AuthorTable (authorname) VALUES (%s)", (authorname))
    conn.commit()
    return

def insert_Bug(bugid):
    cursor.execute("INSERT INTO BugTable (bugID) VALUES (%s)", (bugid))
    cursor.commit()
    return

def insert_Main_Table(filename1,authorname,bugid):
    cursor.execute("INSERT INTO BugTable_FileTable(Bug_ID,File_ID,Author_ID) VALUES (%s,%s,%s)", (filename1,authorname,bugid))
    cursor.commit()
    return

#createTables()
filename="tkk.txt"
insert_filename(filename)
insert_Author(authorname)
insert_Bug(bugid)
insert_Main_Table(filename,authorname,bugid)