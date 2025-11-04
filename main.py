import random 

game_name = ("Totally,Real")

print(f"Welcome to {game_name}!"))
print("=" * (len(game_name) + 15)) 

print("Before we begin, what is your character's name ?")
name = input(">")

print("Great, {name}! Let's begin the adventure!")

player = {
    "name": name,
  "health": 100,
  "coin": 0 
}

events = ["Find a coin", "Meet a monster", "do nothing"]

event = random.choice(events) 
print(f"While exploring, you {event}!")

if event == "find a coin": 
    player['coin']: +=1 
  print(f'{player['name']} found a coin, {player['name']} now has {player['coin']}coins.')
elif event == 'meet a monster':
  player["health"] -= 10
  print(f'{player['name']} got hurt during the combat with monster, health is now {player['health']}.')
else:
  print("Nothing happened this time.")
  
