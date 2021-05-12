import random

async def roulette(message,degenerate):

  roll = random.randint(0,35);
  color = "red";
  if (roll >= 1 and roll <= 10) or (roll >= 19 and roll <= 28):
    if roll % 2 == 0:
      color = "black";
  elif roll == 0:
    color = "green";
  else:
    if roll % 2 == 1:
      color = "black";
  
  try:
    betMessage = message.content.split();
    value = int(betMessage[1]);
    bet = betMessage[2];

    if value <= 0:
      await message.channel.send("Bet a real number you autist");
      return;

    if degenerate.moneys < value:
      await message.channel.send("You don't have enough money you fucktard");
      return;
  
    if len(betMessage) == 4:
      try:
         num = int(betMessage[3])
      except:
        await message.channel.send("Not a right bet, idiot");
        return;
      if num == roll:
        degenerate.gambledDollarydoos(35*value);
        await message.channel.send(color +" "+ str(roll) +  ": " + degenerate.name + " won " + str(34*value));
      else:
        degenerate.gambledDollarydoos(-value);
        await message.channel.send(color +" "+ str(roll) +  ": " + degenerate.name + " lost " + str(value));

    elif bet.lower() == color:
      degenerate.gambledDollarydoos(value);
      await message.channel.send(color +" "+ str(roll) + ": " + degenerate.name + " won " + str(value));
    else:
      degenerate.gambledDollarydoos(-value);
      await message.channel.send(color +" "+ str(roll) + ": " + degenerate.name + " lost " + str(value));
  except ValueError:
    await message.channel.send("Just because you only have a fraction of a brain doesn't mean we accept fractions");
  except Exception as e:
    print(e);
    await message.channel.send("Something went wrong, and it was probably your fault. Because you're an idiot. it's roulette betValue color number. The #number is optional.");