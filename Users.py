class Users:
  def __init__(self):
    self.gamblers = [];

  def addGambler(self, Member):
    self.gamblers.append(Gambler(Member));

  def findGambler(self,Member):
    for i in range(len(self.gamblers)):
      if self.gamblers[i].name == Member.name:
        return i;
    self.addGambler(Member);
    return len(self.gamblers) - 1;

  async def printStats(self,message):
    self.gamblers.sort(key = lambda gambler: gambler.moneys,reverse = True);
    output ="Leaderboard: \nUser: money : handouts\n";
    for loser in self.gamblers:
      output += loser.name + " : " + str(int(loser.moneys)) + " : " + str(int(loser.handoutsTaken))+"\n";
    await message.channel.send(output)
      



class Gambler:
 
  def __init__(self,Member):
    self.name = Member.name;
    self.moneys = 0;
    self.lastHandout = 0;
    self.handoutsTaken = 0;

  def gambledDollarydoos(self,value):
    self.moneys += value;