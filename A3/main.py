__author__ = 'Rana'

import os
import datetime
import understand

from LCOM import getLCOM
from CBO import getCBO
from db import SaveToDB

if __name__ == "__main__":
    start = datetime.datetime.now()

    versions = ["34.0.1847.0"]

    for version in versions:
        #Open Database
        db = understand.open("/Users/Rana/UnderStandProjects/Chromium-"+version+".udb")

        for file in db.ents("File"):

          if(file.library() == "Standard"):
              continue

          fileName, fileExtension = os.path.splitext(str(file))
          if fileExtension == ".cpp" or fileExtension == ".cc" :
            lcom = getLCOM(file)
            cbo = getCBO(file)
            #print("Version: ", version ,"File: ",file, " LCOM: ",lcom, " CBO: ", cbo)
            #DB CALL need to save: version, file, lcom, CBO
            SaveToDB(version, file.longname(), lcom, cbo)
        end = datetime.datetime.now()

        print("total time: ", end-start)
        db.close()