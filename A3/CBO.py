__author__ = 'india'


classKind = set()

def calculateByClass(cls):
    list = set()
    relatedDeclartions = cls.ents("","Declaration")
    for variable in relatedDeclartions:
        if variable.library() == "Standard" or variable.kindname() != "Class":
            continue
        list = list | set({variable.longname()})

    print(list)

    return len(list)


def getCBO(file):
    global classKind

    list = set()

    dependsOn  = file.depends()
    dependsBy  = file.dependsby()

    for cls in dependsOn:
        if cls.library() == "Standard": # or cls.kind() != "Class"
            continue
        list = list | {cls.longname()}
        #print(file.longname()," : ",cls)
        #classKind = classKind | set({cls.kindname()})

    for cls in dependsBy:
        if cls.library() == "Standard": # or cls.kind() != "Class"
            continue
        list = list | {cls.longname()}
        #classKind = classKind | set({cls.kindname()})
        #print(file.longname()," : ",cls.kind())'''

    #print(list)

    return len(list)

def getClassKind():
    global  classKind
    return classKind