__author__ = 'india'

import os
import sys
import understand

#Open Database
db = understand.open("/Users/Rana/UnderStandProjects/TestProject.udb")




def getMethodsByFile(file):

    functions  = file.ents("","function,method,procedure")

    for func1 in functions:
        for func2 in functions:
            if(func1 != func2):
                print(func1, " and ", func2)

    return


for file in db.ents("File"):

  if(file.library() == "Standard"):
      continue

  fileName, fileExtension = os.path.splitext(str(file))
  if fileExtension == ".cpp":
    getMethodsByFile(file)

