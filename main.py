from keep_alive import keep_alive
from roulette import roulette
import Users
import slots
import discord
import os
import pickle
import time
import asyncio
import Pool

client = discord.Client();

pool = [];


def loadUsers():
  return pickle.load(open("./.data/users.data","rb"));
  print("loaded");
def save():
  pickle.dump(users,open("./.data/users.data","wb"));
  pickle.dump(slots.jackpot,open("./.data/jackpot.data","wb"));
  print("saved");

users = loadUsers();


async def handout(message,autist):
  if time.time() - autist.lastHandout < 7*60:
      await message.channel.send("come back for your food stamps in " + str(int(7 - (time.time() - autist.lastHandout)/60)) + " minutes, loser");
      return;
  if autist.moneys >= 500:
    autist.lastHandout = time.time();
    autist.gambledDollarydoos(250);
    await message.channel.send("You got 250");
    return
  
  autist.lastHandout = time.time();
  autist.handoutsTaken += 1;
  qty = 500 - autist.moneys;
  if qty > 500:
    await message.channel.send("500 free dollars and you're still in the red. Sucks to blow");
    autist.gambledDollarydoos(500);
  else:
    await message.channel.send("you're topped off to 500");
    autist.gambledDollarydoos(qty);

    

async def send(message,bitch):
  target = message.mentions;
  if(len(target) == 0):
    await message.channel.send("You have to pick a person to give it to, idiot");
  
  value = [];

  try:
    value = int(message.content.split()[1]);
  except Exception as e: 
    print(e);
    await message.channel.send("try /send value reciever");
    return;
  
  if value < 0:
    await message.channel.send("Nice try");
    return;

  if value * len(target) > bitch.moneys:
    await message.channel.send("You're too broke to be giving out money");
    return;
  for i in range(len(target)):
    degenerate = users.gamblers[users.findGambler(target[i])];
    degenerate.moneys += value;
    bitch.moneys -= value;
  
  await message.channel.send("Send confirmed");

async def stats(message):
  await users.printStats(message);

async def upgrade(message,degen):
  roles = await message.channel.guild.fetch_roles();
  badNames = ["Groovy","Dealer","@everyone","Simple Poll","DM"];

  for r in roles:
    #print(r.name);
    if r.name in badNames:
      roles.remove(r);
      #print("- removed");
  #print(roles);
  value = [0,501, 2500, 10000, 25000,50000,100000,1000000];
  for i in range(len(roles)):
    if(degen.moneys >= value[len(value)-i-1]):
      
      try:
        #print(roles);
        if(message.author.roles[1] == roles[len(roles) - i - 2]):
          return;
      except Exception as e:
        print(e);
        #print("no old role");
      try:
        await message.author.remove_roles(message.author.roles[1]);
      except:
        print("no role to remove");
      await message.author.add_roles(roles[len(roles) - i - 2])
      return;

async def cheat(message):
  if not message.author.name == "Austinll":
    await message.channel.send("No");
    return;
  target = message.mentions;
  value = [];
  try:
    value = int(message.content.split()[1]);
  except Exception as e: 
    print(e);
    await message.channel.send("try /send value reciever");
    return;

  for i in range(len(target)):
    degenerate = users.gamblers[users.findGambler(target[i])];
    degenerate.moneys += value;


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client));
  global pool;
  pool = await Pool.establishPool(client);
  while True:
    await asyncio.sleep(45);
    pool = await Pool.completePool(pool,client);

  


@client.event
async def on_message(message):
  author = message.author;
  if author == client.user:
    return



  content = message.content.lower();

  degenerate = users.gamblers[users.findGambler(author)];

  if content.startswith('/handout'):
    await handout(message,degenerate);
    
  if content.startswith('/mymoney'):
    await message.channel.send(author.name + " has " + str(degenerate.moneys));


  if content.startswith('/roulette'):
    await roulette(message,degenerate);    
  
  if content.startswith('/slots'):
    await slots.rollSlots(message,degenerate);

  if content.startswith('/jackpot'):
    await message.channel.send("The jack pot is " + str(slots.jackpot) + "\nnot like it matters, you're not that lucky");

  if content.startswith('/send'):
    await send(message,degenerate);
    
  if content.startswith('/stats'):
    await stats(message)

  if content.startswith('/pool'):
    await Pool.bet(message,degenerate,pool);

  if content.startswith('/cheat'):
    await cheat(message);
    
  await upgrade(message,degenerate);
  save();

keep_alive()

client.run(os.getenv('TOKEN'))