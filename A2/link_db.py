__author__ = 'Rana'

import pg8000

conn = pg8000.connect(user="Rana", password="r@n@", database="chrome")
cursor = conn.cursor()
#cursor.execute("DROP TABLE ChromeFiles, ChromeBugs, FileBugs, ChromeAuthors, FileAuthors")

cursor.execute("CREATE TABLE IF NOT EXISTS ChromeFiles (id SERIAL PRIMARY KEY, FileName varchar(250) UNIQUE)")
cursor.execute("CREATE TABLE IF NOT EXISTS ChromeBugs (id SERIAL PRIMARY KEY, BugId integer UNIQUE)")
cursor.execute("CREATE TABLE IF NOT EXISTS FileBugs (id SERIAL PRIMARY KEY, FileId integer REFERENCES ChromeFiles (id), BugId integer REFERENCES ChromeBugs (id), constraint u_file_bug unique (FileId, BugId))")
cursor.execute("CREATE TABLE IF NOT EXISTS ChromeAuthors (id SERIAL PRIMARY KEY, AuthorName varchar(250) UNIQUE)")
cursor.execute("CREATE TABLE IF NOT EXISTS FileAuthors (id SERIAL PRIMARY KEY, FileId integer REFERENCES ChromeFiles (id), AuthorId integer REFERENCES ChromeAuthors (id), constraint u_file_authors unique (FileId, AuthorId))")
conn.commit()


def isfileProcessed(fileName):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ChromeFiles WHERE FileName = '"+fileName+"'")
    result = cursor.fetchone()
    if(result):
        return True
    return False

def getFileId(fileName):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ChromeFiles WHERE FileName = '"+fileName+"'")
    result = cursor.fetchone()
    if(result):
        return result[0]
    else:
        return saveFile(fileName)

def getAuthorId(authorName):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ChromeAuthors WHERE AuthorName = '"+authorName+"'")
    result = cursor.fetchone()
    if(result):
        return result[0]
    else:
        return saveAuthor(authorName)

def getBugId(bugId):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ChromeBugs WHERE BugId = %s", (bugId,))
    result = cursor.fetchone()
    if(result):
        return result[0]
    else:
        return saveBug(bugId)

def saveFile(fileName):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ChromeFiles (FileName) VALUES('"+fileName+"') RETURNING id")
    #cursor.execute("SELECT MAX(id) FROM ChromeFiles")
    results = cursor.fetchone()
    #conn.commit()
    #returning the fileId
    return results[0]

def saveBug(bugId):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ChromeBugs (BugId) VALUES(%s) RETURNING id",(bugId,))
    results = cursor.fetchone()
    #conn.commit()
    #returning the bugId
    return results[0]

def saveAuthor(authorName):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ChromeAuthors (AuthorName) VALUES('"+authorName+"') RETURNING id")
    results = cursor.fetchone()
    #conn.commit()
    #returning the fileId
    return results[0]

def updateAuthor(authorName, experience):
    cursor = conn.cursor()
    cursor.execute("UPDATE ChromeAuthors SET experience=%s WHERE AuthorName=%s AND experience < %s", (experience,authorName,experience,))
    #results = cursor.fetchone()
    conn.commit()
    #returning the fileId
    return

def saveFileBug(fileName, bugId):
    fileId = getFileId(fileName)
    bugDBId = getBugId(bugId)

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO FileBugs (FileId, BugId) VALUES(%s, %s)",(fileId, bugDBId))
    except pg8000.ProgrammingError:
        return
        #print "skipping duplicate entry"
    finally:
        conn.commit()

    return

def saveFileAuthor(fileName, authorName):

    fileId = getFileId(fileName)
    authorId = getAuthorId(authorName)

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO FileAuthors (FileId, AuthorId) VALUES(%s, %s)",(fileId, authorId))
    except pg8000.ProgrammingError:
        return
        #print "skipping duplicate entry"
    finally:
        conn.commit()
    return

def updateFileAuthor(authorName,fileName, isOwner):

    fileId = getFileId(fileName)
    authorId = getAuthorId(authorName)
    #print fileId,":",authorId
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE FileAuthors SET owner=%s WHERE fileid=%s AND authorid=%s",(isOwner, fileId, authorId,))
    except pg8000.ProgrammingError:
        return
        #print "skipping duplicate entry"
    finally:
        conn.commit()
    return

#print saveFile("test")
#print saveBug(1234)
#saveFileBug("test.cpp", 1234)
#saveFileAuthor("test2.cpp", "Md Ali Ahsan Rana")
#print getFileId("test3.cpp")
#print saveAuthor("Md Ali Ahsan Rana")
#print isfileProcessed("/Users/Rana/PycharmProjects/sm-6611/A2/data/src/WATCHLISTS")