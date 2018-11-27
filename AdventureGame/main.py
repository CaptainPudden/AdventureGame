import random
import json
import io
from collections import OrderedDict
from shutil import get_terminal_size 

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

with open('character_list.json', 'r') as data_file:
  characters = json.load(data_file)
with open('static_encounters.json', 'r') as data_file:
  static_encounters = json.load(data_file)
with open('random_encounters.json', 'r') as data_file:
  random_encounters = json.load(data_file)
with open('monster_list.json', 'r') as data_file:
  monster_list = json.load(data_file)
with open('special_encounters.json', 'r') as data_file:
  special_encounters = json.load(data_file)
with open('riddle_list.json', 'r') as data_file:
  riddle_list = json.load(data_file)
with open('treasure_list.json', 'r') as data_file:
  treasure_list = json.load(data_file)
#greetings
class myList(list):
    def __init__(self, *args):
        super(myList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])

def greeting(x):
  print('Good day, ' + x + ' , welcome to the Adventure game!')
#write my file
def save_dict(fileName, dictName):
  with io.open(fileName, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(dictName,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

#statcall
def cls():
  print("\n" * get_terminal_size().lines, end='')
def statcall():
  print('Name:   ' + myName + '\n' + 'Class:  ' + str(myCharacter) + '\n' + 'Health: ' + str(health) + '/' + str(maxhealth) + '\n' + 'Damage: ' + str(damage) + '\n' + 'Gold:   ' + str(gold) + '\n')
def mStatCall(mDict):
  print('Name:   ' + str(mDict['Name']) + '\n' + 'Health: ' + str(mDict['Health']) + '\n')
def allStats(mDict):
  statcall()
  mStatCall(mDict)
  
def fight(mDict):
  mCharacter = mDict
  print('You Strike at the ' + mCharacter['Name'])
  damagedealt = random.randint(0, damage - mCharacter['Armor'])
  NEWmCharacterHealth = mCharacter['Health'] - damagedealt
  mCharacter['Health'] = NEWmCharacterHealth
  if damagedealt == 0:
    print('You Missed Scrub!')
  if damagedealt >= 1:
    print('You Dealt ' + str(damagedealt))

#def randomEncounter(level, character)
print('Hello what is your name?')
myName = input()
greeting(myName)
print('Pick a gamemode')
gamemode = input()
#if gamemode == '1':
  #Rules???
if gamemode == '2':
  #Newgame
  print('New Game')
  print('Choose a Character: 1, 2, 3, 4')
  myChoice = input()
  myStats = characters[myChoice]
  myCharacter = myStats[0]
  health = myStats[1]
  maxhealth = myStats[1]
  damage = myStats[2]
  armor = myStats[3]
  gold = myStats[4]
  nextroom = 0
  level = 1
  gamemode = '4'
if gamemode == '3':
  #Load game?
  print('Load game, name your save file')
  try:
    saveGameName = input() + '.json'
    with open(saveGameName, 'r') as data_file:
      stats = json.load(data_file)
      armor = stats['Armor']
      health = stats['Health']
      maxhealth = stats['Max Health']
      damage = stats['Damage']
      gold = stats['Gold']
      level = stats['Level']
      myChoice = stats['myChoice']
      myStats = characters[myChoice]
      myCharacter = myStats[0]
      myName = stats['myName']
      gamemode = '4'
      nextroom = int(stats['nextroom'])
  except NameError:
    print("Oops!  That was not a valid file.")
if gamemode == '4':
  print('The Adventure Begins ,' + myName)
  statcall()
  while health >= 1:
    print('You see 4 doors: Pick one. \n')
    nRoom = str(random.randint(1,4))
    sRoom = str(random.randint(1,4))
    if sRoom == nRoom:
      sRoom = int(sRoom) - 1
      if sRoom <= 0:
        sRoom = str(4)
      else:
        sRoom = str(sRoom)
    print('Elite Room ' + str(sRoom))
    print('Boss Room ' + str(nRoom))
    roomList = myList(1, 2, 3, 4)
    notroomList = myList(int(nRoom), int(sRoom))
    randomRoomList = roomList - notroomList
    X = ', '.join( str(a) for a in randomRoomList )
    print('Other Rooms: ' + X)
    myRoom = input()
    with open('monster_list.json', 'r') as data_file:
      monster_list = json.load(data_file)
    with open('elite_list.json', 'r') as data_file:
      elite_list = json.load(data_file)
    mDict = monster_list[str(random.randint(1, len(monster_list)))]
    eDict = elite_list[str(random.randint(1, len(elite_list)))]
    if myRoom == 'Save':
      stats = {'myName': myName, 'myChoice' : myChoice, 'Health' : health, 'Max Health' : maxhealth, 'Damage' : damage, 'Armor' : armor, 'Gold' : gold, 'Level' : level, 'nextroom' : nextroom}
      print('Name your save file')
      saveGameName = input() + '.json'
      save_dict(saveGameName, stats)
      print('You see 4 doors: Pick one.')
      
      myRoom = input()
    if myRoom == 'Exit':
      break
    if myRoom == nRoom:
      nextroom += 1
      level += 1
      try:
        print(static_encounters[str(nextroom)])
      except KeyError:
        print('You have beaten the game!')
        break
#Special Encounter Write out
    if myRoom == sRoom:      
      specialEncounter = random.randint(1, len(random_encounters))
      encounter = special_encounters[str(specialEncounter)]
      #print(encounter + '\n')
      if specialEncounter == 1:
        #print('Treasure Room')
        treasure = random.randint(1, len(treasure_list))
        yTreasure = treasure_list[str(treasure)]
        print('You found treasure: ' + yTreasure['Name'] + '\n You grow stronger!')
        maxhealth += yTreasure['Health']
        health = maxhealth
        damage += yTreasure['Damage']
        armor += yTreasure['Armor']
        statcall()
      if specialEncounter == 2:
        print('It is an Elite!!! \n The ' + edict['Name'] + 'wants to fight!!')
        while eDict['Health'] >= 1 and health >= 1:
          print('Fight or Defend')
          combatChoice = input()
          if combatChoice == 'Fight':
            fight(eDict)
            try:
              eDamage = random.randint(0, eDict['Damage'] - armor)
            except ValueError:
              eDamage = 0
            health -= eDamage
            if eDamage == 0:
              print(eDict['Name'] + ' missed you!!')
            if eDamage >= 1:
              print(eDict['Name'] + ' hits you for ' + str(eDamage))
            allStats(eDict)
          if combatChoice == 'Defend':
            print('You go on the defense ' + str(health))
            health += int(maxhealth/2)
            if health >= maxhealth:
              health = maxhealth
            print(str(health))
            try:
              eDamage = random.randint(0, eDict['Damage'] - armor)
            except ValueError:
              eDamage = 0
            health -= eDamage
            if eDamage == 0:
              print(eDict['Name'] + ' missed you!!')
            if eDamage >= 1:
              print(eDict['Name'] + ' hits you for ' + str(eDamage))
            allStats(eDict)
        else:
          if eDict['Health'] <= 0:
            print('The ' + eDict['Name'] + ' is Dead!')
            level += 1
          if health <= 0:
            print('Game Over You have Died to ' + eDict['Name'])
      if specialEncounter == 3:
        #print('Trapped Treasure')
        treasure = random.randint(1, len(treasure_list))
        yTreasure = treasure_list[str(treasure)]
        print('You feel a sense of unease! \n Continue? (y/n)')
        yChoice = input()
        if yChoice == 'y':
          print('You found treasure: ' + yTreasure['Name'] + '\n You grow stronger! \n But it was trapped!!!!!')
          health -= yTreasure['Trapped']
          maxhealth += yTreasure['Health']
          damage += yTreasure['Damage']
          armor += yTreasure['Armor']
          statcall()
          if health <= 0:
            print('Game Over You have Died to ' + encounter)
        else:
          print('You leave the room alone...')
      if specialEncounter == 4:
        print('Welcome to the item Store')
        for key, value in treasure_list.items() :
          print (key, value['Name'], value['Gold'])
        tChoice = input()
        treasure = tChoice
        yTreasure = treasure_list[str(treasure)]
        if gold >= int(yTreasure['Gold']):
          gold -= int(yTreasure['Gold'])
          print('You purchased the treasure: ' + yTreasure['Name'] + '\n You grow stronger!')
          maxhealth += yTreasure['Health']
          health = maxhealth
          damage += yTreasure['Damage']
          armor += yTreasure['Armor']
          statcall()
        else:
          print('You can not afford that!!!!!')
      if specialEncounter == 5:
        print('\n its a secret \n')
#Random Encounter Write out
    if myRoom != nRoom and myRoom != sRoom:
      randomEncounter = random.randint(1, len(random_encounters))
      encounter = random_encounters[str(randomEncounter)]
      print(encounter + '\n')

      if randomEncounter == 1:
        greeting(myName)
        score = 1
        loses = 0
        attempts = 0
        gamemode = 3
        multiplier = 10
        number = random.randint(1, multiplier)
        print('What do you want to do? Press 1 for the Directions, 2 to play the game!')
        mathGame = input()
        if int(mathGame) == 1:
          print('Directions: Hints are not absolute, they are a random number between the actual difference and one. If you get a ^So Close^ message means you are 1 number off either high or low.')
          print('What do you want to do? Press 2 to play the game!')
          mathGame = input()
        while int(mathGame) == 2:
          print('Pick a number between 1 and '+ str(multiplier))
          yNumber = input() 
          attempts += 1
          timeout = 5 + score
          if int(yNumber) != int(number):
            x = int(yNumber)
            y = int(number)
            if x < y:
              z = y - x
              if z < 2:
                print('So close')
              if z > 1:
                a = random.randint(2, int(z))
                print('You are low by about ' + str(a))
            if x > y:
              z = x - y
              if z < 2:
                print('So Close')
              if z > 1:
                a = random.randint(2, int(z))
                print('You are high by about ' + str(a))
          if int(number) == int(yNumber):
            score += 1
            multiplier = 10 ** score
            number = random.randint(1, multiplier)
            print('Correct, Level ' + str(score) + ' Attempts ' + str(attempts) + ' Losses ' + str(loses) + ' Next level is ' + str(multiplier))
            attempts = 0
          if score == 4:
            print('Congrats on making it past the obstacle!')
            gold += 50
            maxhealth += 5
            health = maxhealth
            statcall()
            break
          if attempts == timeout:
            loses += 1
            multiplier = 10
            print('Game Over, the number was ' + str(number) + ' score ' + str(score) + ' Attempts ' + str(attempts) + ' Losses ' + str(loses))
            number = random.randint(1, multiplier)
            if loses == 3:
              health = 0   
            if health <= 0:
              print('Game Over You have Died to the Math Room!')
              break
            print('What do you want to do? Press 2 to continue to play the game, Press 3 to give up')
            attempts = 0
            mathGame = input()

      if randomEncounter == 2:
        riddle = riddle_list[str(random.randint(1, len(riddle_list)))]
        print(riddle['Riddle'] + '\n')
        answer = riddle['Answer']
        answerList = [riddle['Answer'], riddle['False 1'], riddle['False 2'], riddle['False 3']]
        print(random.sample(answerList, 4))
        pAnswer = input()
        if pAnswer == answer:
          print('Congrats, that is correct!')
          gold += 30
          damage += 3
          statcall()
        else:
          print('Incorrect! You will be punished!')
          health -= int(maxhealth/4)
          statcall()
          if health <= 0:
            print('You died to the words of a riddle!')

      if randomEncounter == 3:
        while mDict['Health'] >= 1 and health >= 1:
          print('Fight or Defend')
          combatChoice = input()
          if combatChoice == 'Fight':
            fight(mDict)
            try:
              mDamage = random.randint(0, mDict['Damage'] - armor)
            except ValueError:
              mDamage = 0
            health -= mDamage
            if mDamage == 0:
              print(mDict['Name'] + ' missed you!!')
            if mDamage >= 1:
              print(mDict['Name'] + ' hits you for ' + str(mDamage))
            allStats(mDict)
          if combatChoice == 'Defend':
            print('You go on the defense ' + str(health))
            health += int(maxhealth/2)
            if health >= maxhealth:
              health = maxhealth
            print(str(health))
            try:
              mDamage = random.randint(0, mDict['Damage'] - armor)
            except ValueError:
              mDamage = 0
            health -= mDamage
            if mDamage == 0:
              print(mDict['Name'] + ' missed you!!')
            if mDamage >= 1:
              print(mDict['Name'] + ' hits you for ' + str(mDamage))
            allStats(mDict)
        else:
          if mDict['Health'] <= 0:
            print('The ' + mDict['Name'] + ' is Dead!')
            level += 1
          if health <= 0:
            print('Game Over You have Died to ' + mDict['Name'])

      if randomEncounter == 4:
        print('The room is empty, best lead on! \n')