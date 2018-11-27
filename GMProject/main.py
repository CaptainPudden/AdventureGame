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
#character creation
def abilityroll(ability):
  dieRoll1 = random.randint(1,6)
  dieRoll2 = random.randint(1,6)
  dieRoll3 = random.randint(1,6)
  dieRoll4 = random.randint(1,6)
  rollList = [dieRoll1, dieRoll2, dieRoll3, dieRoll4]
  print(rollList)
  rollList.remove(min(rollList))
  ability = sum(rollList)
  print(ability)
#name/playername
print('Hello what is your name?')
myName = input()
print('Good day, ' + myName + ' , welcome to the hero creator!')
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
Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Wisdom = 0
Charisma = 0
abilityroll(Strength)
abilityroll(Dexterity)
abilityroll(Constitution)
abilityroll(Intelligence)
abilityroll(Wisdom)
abilityroll(Charisma)

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
