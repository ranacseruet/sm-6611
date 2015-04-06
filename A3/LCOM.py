__author__ = 'india'

import os
import sys

import understand

#Open Database
db = understand.open("/Users/Rana/UnderStandProjects/TestProject.udb")




def dependsOn(func1, func2):

    #func1 dependents list building is happening everytime unnecessarily

    #TODO check attribute dependency

    relatedFunctions = func1.ents("","function,method,procedure")

    if relatedFunctions == None:
        return False

    fList = []
    for func in relatedFunctions:
        if func.library() == "Standard":
            continue
        if func.name() != func1.name():
            fList.append(func.name())

    if func2.name() in fList:
        #print(func1.name(), "depends on", func2.name())
        return True
    else:
        return False


def getMethodsByFile(file):

    functions  = file.ents("","function,method,procedure")
    funcSet = set()

    for func1 in functions:
        if func1.library() == "Standard":
            continue
        for func2 in functions:
            if func2.library() == "Standard":
                continue
            if(func1 != func2) & dependsOn(func1, func2):
                # (a,b) and (b,a) both are being added
                funcSet = funcSet | set([frozenset([func1.name(), func2.name()])])

    for pair in funcSet:
        print(pair)

    return


for file in db.ents("File"):

  if(file.library() == "Standard"):
      continue

  fileName, fileExtension = os.path.splitext(str(file))
  if fileExtension == ".cpp":
    getMethodsByFile(file)

