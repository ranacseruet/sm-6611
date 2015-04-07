__author__ = 'india'

import os
import sys

import understand

#Open Database
db = understand.open("/Users/Rana/UnderStandProjects/Test2.udb")




def dependsOn(func1, func2):

    #func1 dependents list building is happening everytime unnecessarily

    #TODO check attribute sharing

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


def getLCOM(file):

    functions  = file.ents("","function,method,procedure")
    funcSet = set()

    for func1 in functions:
        if func1.library() == "Standard":
            continue
        for func2 in functions:
            if func2.library() == "Standard":
                continue
            if(func1 != func2) & dependsOn(func1, func2):
                funcSet = funcSet | set([frozenset([func1.name(), func2.name()])])

    graphs = []
    for pair in funcSet:
        #print(pair)
        if len(graphs) <=0:
            graphs.append(pair)
        else:
            processed = False
            for graph in graphs:
                i = graphs.index(graph)
                if len(graph & pair) > 0:
                    graph |= pair
                    graphs[i] = graph
                    processed = True
            if not processed:
                graphs.append(pair)

    count = 0
    #LCOM = no of disconnected graphs
    for graph in graphs:
        #print(graph)
        count += len(graph)

    lcom = len(graphs)

    lcom += len(functions) - count

    return lcom


def getCBO(file):
    classes  = file.ents("","Class")

    count = 0
    for cls in classes:
        if cls.library() == "Standard":
            continue
        count += 1
        print(file.longname()," : ",cls)

    return count




for file in db.ents("File"):

  if(file.library() == "Standard"):
      continue

  fileName, fileExtension = os.path.splitext(str(file))
  if fileExtension == ".cpp":
    #print("LCOM: ", getLCOM(file))
    getCBO(file)
