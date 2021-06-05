import random
import time

class Roll:
  def __init__(self,one,two):
    self.d1 = one;
    self.d2 = two;
    self.score = one+two;

class Bet: 
  def __init__(self,message, degenerate):
    self.degenerate = degenerate;
    self.value = message.split[2];
    self.type = message.split[3];
    self.beginTime = time.time();

class Game:
  def __init__(self):
    self.point = -1;
    self.bets = [];

  def addBet(self,b):
    self.bets.append(b);

  def resolveBets(self):
    print("temp");



def rollDice():
  return Roll(random.randint(0,6),random.randint(0,6));

def passLine(game,roll):
  if(game.point == -1):
    if(roll.score == 7 or roll.score == 11):
      return 1;
    elif(roll.score == 2 or roll.score == 3):
      return 0;
    elif(roll.score == 12):
      return -2;
  else:
    if(roll.score == 7):
      return 0;
    elif roll.score == game.point:
      return 1;
  
  return -1;

def noPassLine(game,roll):
  val = passLine(game,roll);
  if val == -1:
     return val;
  return not val;
  
  




  