__author__ = 'Rana'

from github import Github
import time

g = Github()
repo = g.get_repo('poise/python')
contributors = repo.get_contributors()
for c in contributors:
    print c.name
    time.sleep(1)


