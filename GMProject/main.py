import random
import json
import io
import glob
from collections import OrderedDict
from shutil import get_terminal_size 
import os
from savefile import save_dict
import decode
import dice
from pprint import pprint
try:
  os.chdir('GMProject/')
except FileNotFoundError:
  print('Already There')



pathJson = 'dnd-5e-srd/json/'
fileRaces = '01 races.json'
nameRaces = 'Races'

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
with open(pathJson + '01 races.json', 'r') as data_file:
  race_list = json.load(data_file)
with open(pathJson + '02 classes.json', 'r') as data_file:
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
    decode.callRacelist(pathJson, fileRaces, nameRaces)
    count = 0
    for x in decode.rList:
      count += 1
      print(str(count) + ':' + x)
    pChoice = input()
    myRace = decode.rList[int(pChoice) - 1]
    print('You Chose the ' + myRace + ' Race!')
    print('Racial Traits Include')
    decode.callRacetraits(pathJson, fileRaces, nameRaces, myRace)
    rTraits = decode.traits
    for x in rTraits:
      pprint(x.lstrip(), width=180)
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