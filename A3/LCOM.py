__author__ = 'india'

import understand

#Open Database
db = understand.open("E:\sm-6611\TestDatabase.udb")

def sortKeyFunc(ent):
  return str.lower(ent.longname())
#
# ents = db.ents("function,method,procedure")
# for func in sorted(ents,key = sortKeyFunc):
#   print (func.longname()," (",sep="",end="")
#   first = True
#   for param in func.ents("Define","Object"):
#     if not first:
#       print (", ",end="")
#     print (param.type(),param,end="")
#     first = False
#   print (")")


ents = db.ents("function,method,procedure")
for func in sorted(ents,key = sortKeyFunc):
  print (func.longname()," (",sep="",end="")
  first = True
  for param in func.ents("use by","Function"):
    if not first:
      print (", ",end="")
    print (param.type(),param,end="")
    first = False
  print (")")