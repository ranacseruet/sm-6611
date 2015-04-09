__author__ = 'india'

import pg8000
#import psycopg

release = ""
class_path = "kunwar"
cbo = 2
lcom = 11

conn = None;
cursor = None;
conn = pg8000.connect(database="D3", user="Rana", password="r@n@", host="localhost")
cursor = conn.cursor()

def createTable():
    cursor.execute("CREATE SEQUENCE FILE_id_seq")
    cursor.execute("CREATE TABLE Release_Info(ID BIGINT UNIQUE NOT NULL "
                   "DEFAULT NEXTVAL('FILE_id_seq'), RELEASE varchar(100) NOT NULL ,class_path varchar(250) NOT NULL, LCOM INT NOT NULL, CBO INT NOT NULL,  CONSTRAINT versionpath UNIQUE(RELEASE, class_path)) ")
    conn.commit()
    return


def SaveToDB(release,class_path,lcom,cbo):
    insert_Main_Table(release,class_path,lcom,cbo)
    return

def insert_Main_Table(release,class_path,lcom,cbo):
    cursor.execute("INSERT INTO  Release_Info (RELEASE,class_path,LCOM,CBO) VALUES(%s,%s,%s,%s)",(release,class_path,lcom,cbo,))
    conn.commit()
    return


#createTable()

#SaveToDB(release,class_path, lcom,cbo)
