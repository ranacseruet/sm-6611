__author__ = 'Rana'

import os
import re

#installed in system
from git import Repo

source_dir = '/Users/Rana/PycharmProjects/sm-6611/A2/data/src/'

def getFileInfo(fileName):

    ##find first created date/time
    ##

    repo = Repo(source_dir)
    commits = list(repo.iter_commits(paths=fileName))

    authors = set()
    bugs    = set()

    for commit in commits:
        #retrieve commit details
        co = repo.commit(commit)
        author = co.author.name
        authors.add(author)

        #regex to identify bug
        m = re.search('BUG=([\d]+)', co.message)
        if m:
            bugId = m.group(1)
            bugs.add(bugId)
            ##open bug file and find creator/owner/collaborators
            #print bugId

    ##save bugs and authors according to fileName
    saveToDB(fileName, authors, bugs)
    print bugs
    return

for root, dirs, files in os.walk(source_dir):
    for file in files:
        # retrieve info for file and save to db
        getFileInfo(root+file)
        break
    print len(dirs)
    break