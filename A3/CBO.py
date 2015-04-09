__author__ = 'india'


def getCBO(file):
    classes  = file.ents("","Class")

    count = 0
    for cls in classes:
        if cls.library() == "Standard":
            continue
        count += 1
        #print(file.longname()," : ",cls)

    return count