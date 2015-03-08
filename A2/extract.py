__author__ = 'Rana'

import os
import re
import logging
import time

from link_db import saveFileBug, saveFileAuthor, isfileProcessed

#installed in system
import git

source_dir = '/Users/Rana/PycharmProjects/sm-6611/A2/data/src/'
repo = git.Repo(source_dir, odbt=git.GitCmdObjectDB)

logging.basicConfig(filename='mining.log',level=logging.DEBUG)
logger = logging.getLogger('datamining')

def extractAndSaveFileInfo(fileName):

    global repo

    ##find first created date/time
    ##
    commits = list(repo.iter_commits(paths=fileName))

    authors = set()
    bugs    = set()

    if len(commits) <= 0:
        print commits
        return False

    for commit in commits:
        #retrieve commit details
        co = repo.commit(commit)
        author = co.author.name
        saveFileAuthor(fileName, author)
        authors.add(author)

        #regex to identify bug
        m = re.search('BUG=([\d]+)', co.message)
        if m:
            bugId = m.group(1)
            bugs.add(bugId)
            ##open bug file and find creator/owner/collaborators
            #print bugId
            saveFileBug(fileName, bugId)

    ##save bugs and authors according to fileName
    #saveToDB(fileName, authors, bugs)
    #print bugs
    return True

start = time.time()
totalFiles = 0
sessionFiles = 0

def startCrawl():
    global  start, totalFiles, sessionFiles, fileCount
    for root, dirs, files in os.walk(source_dir):
        curTime = time.time()
        curProcessedFiles = 0

        #skip .git directory
        if root.find(".git") >=0:
            logger.info("skipping .git directory: "+root)
            continue

        for file in files:
            if file[0] == '.':
                print "file starts with . , skipping: "+file
                continue
            fullFilePath = root
            fullFilePath += "" if (root[len(root)-1] == "/") else "/";
            fullFilePath += file
            #print "trying for file: "+fullFilePath
            totalFiles += 1

            if isfileProcessed(fullFilePath):
                logger.info("file already processed. skipping")
                continue

            # retrieve info for file and save to db
            if extractAndSaveFileInfo(fullFilePath):
                curProcessedFiles += 1
            else:
                print "file information not found/not saved: "+str(file)+" Dir: "+root

        end = time.time()
        logger.info(str(curProcessedFiles)+" processed in "+str((end-curTime))+" seconds")
        logger.info("Total time passed "+str((end-start))+" seconds. Total Files processed: "+str(totalFiles))
        sessionFiles += curProcessedFiles
        if sessionFiles > 50:
            break
    return

startCrawl()