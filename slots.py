import random
import pickle


def loadJackpot():
  return pickle.load(open("./.data/jackpot.data","rb"))


default_jackpot = 100000;
jackpot = loadJackpot();

async def rollSlots(message,degenerate):
  def emoToString(emoji):
    return"<:"+str(emoji.name)+":"+str(emoji.id)+">"

  emojis = message.guild.emojis;
  numEmojis = len(emojis)-1;
  global jackpot;
  value = 100;

  if value > degenerate.moneys:
    await message.channel.send("You don't have enough money you fucktard");
    return;
  jackpot += value;
  degenerate.gambledDollarydoos(-value);
  numRoll = 5;
  roll = [1,2,3,4,5];
  output = "";
  numGODS = 0;
  numSIMPS = 0;
  for i in range(numRoll):
    while True:
      roll[i] = random.randint(0,numEmojis);
      if(not emojis[roll[i]].animated):
        break
    output += emoToString(emojis[roll[i]]);

    if emojis[roll[i]].name == "spongebob_pepe": 
      numGODS += 1;
    elif emojis[roll[i]].name == "PepeSimp":
      numSIMPS += 1;
    
  count = [];
  for i in range(5):
    count.append(roll.count(roll[i]));
  check1 = 0;
  check2 = 0;

  if count.count(2) == 4:
    check1 = 2;
    check2 = 2;
  elif count.count(1) == 5:
    check1 = 0;
    check2 = 0;
  else:
    res = []
    [res.append(x) for x in count if x not in res]
    check1 = max(res);
    check2 = min(res);
  
  if numGODS == 5:
    await message.channel.send(output + "\n!!!SPONGEPEPE BLESSES YOU!!!\nYOU WON "+str(5*jackpot)+"\n Try not to waste it on heroine this time");
    degenerate.gambledDollarydoos(5*jackpot);
    jackpot = default_jackpot;
    return;
  if check1 == 5:
    degenerate.gambledDollarydoos(jackpot);
    await message.channel.send(output + "\n5 OF A KIND: YOU WON THE JACKPOT");
    return;
  if check1 == 4:
    if numGODS == 4:
      degenerate.gambledDollarydoos(20000);
      await message.channel.send(output + "\n4 SPONGEPEPE: YOU WON 20K")
      return;
    elif numSIMPS == 4:
      await message.channel.send(output + "\nQUAD SIMP. Lose 4000");
      degenerate.gambledDollarydoos(-3900);
      return;
    degenerate.gambledDollarydoos(10000);
    await message.channel.send(output + "\n4 OF A KIND: YOU WON 10K")
    return;
  if check1 == 3 and check2 == 2:
    degenerate.gambledDollarydoos(3000);
    await message.channel.send(output + "\nFULL HOUSE: YOU WON 3k")
    return;
  if numGODS == 3:
    degenerate.gambledDollarydoos(2000);
    await message.channel.send(output + "\n3 SPONGEPEPE: YOU WON 2k");
    return;
  if check1 == 2 and check2 == 2:
    degenerate.gambledDollarydoos(750);
    await message.channel.send(output + "\nTWO PAIR: YOU WON 750");
    return;
  if check1 == 3:
    if numSIMPS == 3:
      await message.channel.send(output + "\ntriple simp. Lose 500");
      degenerate.gambledDollarydoos(-400);
      return;
    degenerate.gambledDollarydoos(500);
    await message.channel.send(output + "\nthree of a kind: 500");
    return
  if numGODS == 2:
    await message.channel.send(output + "\nspongepepe blesses you: 300");
    degenerate.gambledDollarydoos(300);
    return;
  if check1 == 2:
    if numSIMPS == 2:
      await message.channel.send(output + "\nsimp. Lose 50");
      degenerate.gambledDollarydoos(-50);
      return;
    await message.channel.send(output + "\nPair: 50");
    degenerate.gambledDollarydoos(50);
    return;
  await message.channel.send(output + "\nNothing");
  return;
