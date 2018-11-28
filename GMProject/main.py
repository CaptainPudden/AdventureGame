import random
import json
import io
import glob
from collections import OrderedDict
from shutil import get_terminal_size 
import os

os.chdir('GMProject/')

import dice

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
with open('race_list.json', 'r') as data_file:
  race_list = json.load(data_file)
with open('class_list.json', 'r') as data_file:
  class_list = json.load(data_file)
try:
  with open('character_list.json', 'r') as data_file:
    character_list = json.load(data_file)
except  FileNotFoundError:
  print('filenotfound')
  character_list = ['nouserfound']
  with io.open('character_list.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(character_list, ensure_ascii=False))
#character creation
def save_dict(fileName, dictName):
  with io.open(fileName, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(dictName,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
#default values
  
#name/playername
print('Hello what is your name?')
myName = input()
print('Good day, ' + myName + ' , welcome to the hero creator!')
if 0 == 0:
  if myName not in character_list:
    print('Lets Pick a Race!')
    print(character_list)
    #list race for choice
    for list in race_list:
        for x in list:
            listed_races = race_list[x]
            for z,y in listed_races.items():
              if z == "Name":
                print(x + ":" + y)
    pChoice = input()
    myRace = race_list[str(pChoice)]
    print('You Chose the ' + myRace["Name"] + ' Race!')
    print('Lets Pick A Class!')
    for dict in class_list.keys():
        for x in dict:
          listed_class = class_list[x]
          for z,y in listed_class.items():
            if z == "Name":
                print(x + ":" + y)
    pChoice = input()
    myClass = class_list[str(pChoice)]
    print('You Chose the ' + myClass["Name"] + ' Class!')
    print(myName + ' you have decided on a ' + myRace["Name"] + ":" + myClass["Name"])
    print("OK, Let us find our ability scores!")

    abilityScores = {"Strength" : 0, "Dexterity" : 0, "Constitution" : 0, "Intelligence" : 0, "Wisdom" : 0, "Charisma" : 0}
    for a,b in abilityScores.items():
      abRoll = dice.Dice()
      abRoll.roll(4)
      b = abRoll.total
      print(f"{a}: {b}")
      c = {a: b}
      abilityScores.update(c)
    
    
    for a in abilityScores.items():
      print(str(a))
    character_list.append(myName)
    if 'nouserfound' in character_list:
      character_list.remove('nouserfound')
    myDict = {"Name" : myName, "Race" : myRace, "Class" : myClass, "Ability Scores" : abilityScores}
    save_dict(myName + '_info.json', myDict)
    with io.open('character_list.json', 'w', encoding='utf8') as f:
      f.write(json.dumps(character_list, ensure_ascii=False))
  else:
    print('You have a Character!')
  print(character_list)
else:
  print("god is dead")
#rollabilityscores
#racelist
#classlist
#classfeatures
#background
#assignabilityscores
#computestats (health, initiative)
#knownlanguages
#armor
#weapons
#attacks
#spells