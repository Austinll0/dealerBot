import time
import random
import discord


class Pool:
  
  def __init__(self,time,bet,client):
    self.ch = discord.utils.get(client.get_all_channels(), guild__name='BlackJack and hookers',name="pool")
    self.time = time;
    self.bet = bet;
    self.size = 0;
    self.betters = [];
  
  async def print(self):
    timeDone = time.localtime(self.time);
    output = "Pool ending at " + str(timeDone[3]) + ":" + str(timeDone[4]);
    output += " with bet size: " + str(self.bet);
    await self.ch.send(output)

  def addBetter(self,degen):
    self.betters.append(degen);



async def establishPool(client):
  T = time.time();
  waitMins = 60;
  waitSecs = waitMins * 60;
  nextPool = T + waitSecs -(T%waitSecs); # next 10 minute interval
  p = Pool(nextPool,random.randint(0,10000),client);
  await p.print();
  return p;
  

async def bet(message,degen,pool):
  if pool.bet > degen.moneys:
    await message.channel.send("You're too broke")
    return;
  degen.gambledDollarydoos(-pool.bet);
  pool.size += pool.bet;
  pool.addBetter(degen);
  await pool.ch.send("Bet confirmed, new pool size: " + str(pool.size));

async def completePool(p,client):
  if time.time() < p.time:
    return p;
  if p.betters:
    winner = p.betters[random.randint(0,len(p.betters)-1)];
    winner.gambledDollarydoos(p.size);
    await p.ch.send(winner.name + " Wins " + str(p.size));

  return await establishPool(client);
  