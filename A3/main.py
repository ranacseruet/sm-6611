__author__ = 'Rana'

import os
import datetime
import understand

from LCOM import getLCOM
from CBO import getCBO, getClassKind
from db import SaveToDB

if __name__ == "__main__":
    start = datetime.datetime.now()

    versions = ["34.0.1847.0"]
    #versions = ["34.0.1847.0", "33.0.1750.0", "32.0.1700.0", "31.0.1650.0", "30.0.1599.0", "29.0.1547.0", "28.0.1500.0", "27.0.1453.0", "26.0.1410.0", "25.0.1364.0"]
    # "34.0.1847.0" "33.0.1750.0"    32.0.1700.0    31.0.1650.0     30.0.1599.0     29.0.1547.0     28.0.1500.0     27.0.1453.0     26.0.1410.0     25.0.1364.0

    for version in versions:
        #Open Database
        db = understand.open("/Users/Rana/UnderStandProjects/Chromium-"+version+".udb")
        #db = understand.open("/Users/Rana/UnderStandProjects/Test2.udb")
        for file in db.ents("File"):

          if(file.library() == "Standard"):
              continue

          fileName, fileExtension = os.path.splitext(str(file))
          if fileExtension == ".cpp" or fileExtension == ".cc" :
            classes = file.ents("Define","Class")
            for cls in classes:
                lcom = getLCOM(cls)
                cbo = getCBO(cls)
                #print("Version: ", version ,"File: ",file.longname()+":"+cls.longname(), " LCOM: ",lcom, " CBO: ", cbo)
                #DB CALL need to save: version, file, lcom, CBO
                SaveToDB(version, file.longname()+":"+cls.longname(), lcom, cbo)

        end = datetime.datetime.now()
        print("total time: ", end-start)
        #print(getClassKind())
        db.close()