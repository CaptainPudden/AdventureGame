import random
import json
import io
import glob
from collections import OrderedDict
from shutil import get_terminal_size 
import os

os.chdir('GMProject/')

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
with open('race_list.json', 'r') as data_file:
  race_list = json.load(data_file)
with open('class_list.json', 'r') as data_file:
  class_list = json.load(data_file)
with open('character_list.json', 'r') as data_file:
  character_list = json.load(data_file)
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
if myName not in character_list:
  print('Lets Pick a Race!')
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

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Strength = sum(rollList)

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Dexterity = sum(rollList)

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Constitution = sum(rollList)

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Intelligence = sum(rollList)

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Wisdom = sum(rollList)

  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  Charisma = sum(rollList)
  abilityScores = {"Strength" : Strength, "Dexterity" : Dexterity, "Constitution" : Constitution, "Intelligence" : Intelligence, "Wisdom" : Wisdom, "Charisma" : Charisma}
  for a in abilityScores.items():
    print(str(a))
  character_list.append(myName)
  myDict = {"Name" : myName, "Race" : myRace, "Class" : myClass, "Ability Scores" : abilityScores}
  save_dict(myName + '_info.json', myDict)
  with io.open('character_list.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(character_list, ensure_ascii=False))
else:
  print('You have a Character!')



print(character_list)
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
