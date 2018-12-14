import json
from pprint import pprint
dList = []
traits = []
rList = []
def callRacetraits(filePath, file, name, source):
  with open(filePath + file, 'r') as data_file:
    File = json.load(data_file)
  for a in File[name]:
    aName = File[name]
    for b in aName[a]:
      bA = aName[a]
      for c in bA[b]:
        cB = bA[b]
        if source in a:
          traits.clear()
          for d in cB[c]:
            traits.append(d)
          return
def callRacelist(filePath, file, name):
  with open(filePath + file, 'r') as data_file:
    File = json.load(data_file)
  rList.clear() 
  for a in File[name]:
    aName = File[name]
    rList.append(a)
    