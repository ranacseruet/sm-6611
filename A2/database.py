__author__ = 'india'

import pg8000
import psycopg

authorname = None
bugid= None
filename1= None



conn = None;
cursor = None;
conn = pg8000.connect(database="postgres", user="postgres", password="root", host="localhost")
cursor = conn.cursor()

def call(filename,authorname,bugid):
    insert_filename(filename)
    insert_Author(authorname)
    insert_Bug(bugid)
    insert_Main_Table(filename,authorname,bugid)
    return


def createTables():
    cursor.execute("CREATE SEQUENCE FILE_id_seq")
    cursor.execute("CREATE TABLE FileTable(ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('FILE_id_seq'), filename varchar(250) NOT null UNIQUE )")
    cursor.execute("CREATE SEQUENCE Author_id_seq")
    cursor.execute("CREATE TABLE AuthorTable (Author_ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('Author_id_seq'), authorname varchar(250) not null UNIQUE)")
    cursor.execute("CREATE SEQUENCE BUG_id_seq")
    cursor.execute("CREATE TABLE BugTable (BUG_ID INT UNIQUE NOT NULL DEFAULT NEXTVAL('BUG_id_seq'), bugID INT not null UNIQUE)")
    cursor.execute("CREATE SEQUENCE TABLE_id_seq")
    cursor.execute("CREATE TABLE BugTable_FileTable (TABLE_ID bigint UNIQUE  NOT NULL DEFAULT NEXTVAL('TABLE_id_seq') , Bug_ID int NOT NULL REFERENCES BugTable(BUG_ID), File_ID int not null REFERENCES FileTable(ID), Author_ID INT not null REFERENCES AuthorTable(Author_ID))")
    conn.commit()
    return

def insert_filename(filename1):
    cursor.execute('INSERT INTO FileTable (filename) SELECT (%s) WHERE NOT EXISTS (SELECT filename FROM FileTable where filename = (%s) )', (filename1,filename1,))
    conn.commit()
    return

def insert_Author(authorname):
    cursor.execute('INSERT INTO AuthorTable (authorname) SELECT (%s) WHERE NOT EXISTS (SELECT authorname FROM AuthorTable where authorname = (%s) )', (authorname,authorname,))
    conn.commit()
    return

def insert_Bug(bugid):
    cursor.execute('INSERT INTO BugTable (bugID) SELECT (%s) WHERE NOT EXISTS (SELECT bugID FROM BugTable where bugID = (%s) )', (bugid,bugid,))
    conn.commit()
    return

def insert_Main_Table(filename1,authorname,bugid):
    fileID = None
    authorID = None
    Bug_ID = None
    cursor.execute("SELECT ID from FileTable WHERE filename=(%s)",(filename1,))
    rows = cursor.fetchall()
    for row in rows:
       fileID = row[0]

    cursor.execute("SELECT Author_ID from AuthorTable WHERE authorname=(%s)",(authorname,))
    rows = cursor.fetchall()
    for row in rows:
       authorID = row[0]

    cursor.execute("SELECT BUG_ID from BugTable WHERE bugID=(%s)",(bugid,))
    rows = cursor.fetchall()
    for row in rows:
       Bug_ID = row[0]

    cursor.execute('INSERT INTO BugTable_FileTable (Bug_ID,File_ID,Author_ID) SELECT (%s), (%s), (%s) WHERE NOT EXISTS (SELECT Bug_ID,File_ID,Author_ID FROM BugTable_FileTable where Bug_ID = (%s) AND File_ID = (%s) AND Author_ID = (%s))', (Bug_ID,fileID,authorID,Bug_ID,fileID,authorID,))
    conn.commit()
    return

#createTables()