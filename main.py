import discord
import os
import requests
import json
import random

url = "https://dad-jokes.p.rapidapi.com/random/joke"

minecraft = ['Minecraft','minecraft','pog','pogchamp','Pogchamp', 'Pog']

headers = {
    'x-rapidapi-key': "1bd4e87b13msh987a22ff4710ab9p14ea05jsn5c48b0c13bfe",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
}

rpsList = ['rock','paper','scissors']

def rpsWinner(x,y):
  if rpsList.index(x) == rpsList.index(y):
        res = "I also had "+x+", its a tie"
    # the key part
  elif (rpsList.index(x) - rpsList.index(y)) % 3 == 1:
      res = "I had "+x+", you lose"
  else:
      res = "I had "+x+", you win"
  return(res)

def rps(userChoice):
  choiceNum = random.randint(0, 2)
  choice = rpsList[choiceNum]
  ret = rpsWinner(choice,userChoice)
  return(ret)


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
  return(quote)


def get_joke():
    resp = requests.request("GET", url, headers=headers)
    joke = json.loads(resp.text)['body'][0]
    return joke['setup'] + '\n'*2 + joke['punchline']


client = discord.Client()

@client.event
async def on_ready():
  print('I am {0.user}!'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('?hello'):
    embedVar = discord.Embed(title="Hello", description="Hello", color=0xFF0000)
    await message.channel.send(embed=embedVar)
  
  if message.content.startswith('?rps'):
  #  embedVar = discord.Embed(title="Rock Paper Scissors", description="Type either rock, paper, or scissors", color=0xFF0000)
    #await message.channel.send(embed=embedVar)
    if message.content.endswith('rock'):
      winner = rps('rock')
      win = str(winner)
      embedVar = discord.Embed(title="Rock Paper Scissors", description=win, color=0xFF0000)
      await message.channel.send(embed=embedVar)
    elif message.content.endswith('paper'):
      winner = rps('paper')
      win = str(winner)
      embedVar = discord.Embed(title="Rock Paper Scissors", description=win, color=0xFF0000)
      await message.channel.send(embed=embedVar)
    elif message.content.endswith('scissors'):
      winner = rps('scissors')
      win = str(winner)
      embedVar = discord.Embed(title="Rock Paper Scissors", description=win, color=0xFF0000)
      await message.channel.send(embed=embedVar)
  
  if any(word in message.content for word in ['Aryan','aryan']):
    await message.channel.send('obeseeeee')
  
  if message.content.startswith('?joke'):
    embedVar = discord.Embed(title="Joke", description=get_joke(), color=0xFF0000)
    await message.channel.send(embed=embedVar)
  
  if message.content.startswith('?help'):
    embedVar = discord.Embed(title="Commands", description="", color=0xFF0000)
    embedVar.add_field(name="?hello", value="Says hello", inline=False)
    embedVar.add_field(name="?joke", value="tells a joke", inline=False)
    embedVar.add_field(name="?quote", value="gives random quote from zenquotes.io", inline=False)
    embedVar.add_field(name="?rps (choice)", value="rock paper scissors", inline=False)
    embedVar.add_field(name="?help", value="gives list of commands", inline=False)
    embedVar.add_field(name="Easter Eggs", value="certain messages will prompt funny reactions :eyes: :eyes:", inline=False)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('?quote'):
    quote = get_quote()
    embedVar = discord.Embed(title="Quote", description=quote, color=0xFF0000)
    await message.channel.send(embed=embedVar)
  
  if any(word in message.content for word in ['good bot','god bot', 'Good bot']):
    await message.channel.send('I know I am')
  
  if any(word in message.content for word in ['java', 'C++', 'Java', 'c++']):
    await message.channel.send('Ew')
  
  if any(word in message.content for word in ['pyton','Python', 'py', 'Py']):
    await message.channel.send('Python = poggers')

  if any(word in message.content for word in minecraft):
    await message.channel.send('Poggers')
  if any(word in message.content for word in ['Fifa', 'FIFA', 'fifa']):
    await message.channel.send('Prajwal grinds fifa')
  if any(word in message.content for word in [';', 'semicolon', 'semicolons',"Semicolon","Semicolon"]):
    await message.channel.send('Semicolons suck, Python MasterRace')

client.run(os.getenv('TOKEN'))