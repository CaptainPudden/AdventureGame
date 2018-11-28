import random

class Die():
  def __init__(self):
    self.value = None
  
  def __repr__(self):
    return f'Die: {self.value}'
  
  def roll(self):
    self.value = random.randint(1,6)
    return self.value
  
class Dice():
  def __init__(self):
    self.dice = []
    self.history = []
    
  def __repr__(self):
    return f'<Badass Dice {self.dice}>'
 
  def roll(self, num_dice):
    if self.dice:
      self.history.append(self.dice)
    self.dice = []
    for i in range(0, num_dice):
      self.dice.append(Die())
    self.rolls = [x.roll() for x in self.dice]

    for idx, roll in enumerate(self.rolls):
      if roll is min(self.rolls):
        self.rolls.pop(idx)
        break
        
    return self.rolls
   
  @property
  def total(self):
    return sum(self.rolls)