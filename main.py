import random 


game_name = "Totally,Real"
#print("Welcome to " + game_name + "!")
    

name = "tester"

#print("great, " +  name + "! Let's begin the adeventure!")
    
# Players initial stats 
player = {
        "name": name,
        "health": 100,
        "coin": 0,
        "x": 0,
        "y": 0
    }
def check_event():
    events = ["find a coin", "meet a monster", "do nothing"] 

    event = random.choice(events)
    

    if event == "find a coin":
        player["coin"] += 1

    elif event == "meet a monster":
        player["health"] -= 10 
        
map_size = 9

def draw_ui(x, y):

    for i in range(map_size):
        for j in range(map_size):
            if i == x and j == y:
                print("C", end = " ") # two spaces
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end = " ")
            else:
                print(".", end = " ")
        print("\n")
    print("Health:", player["health"])
    print("====================")
    print("Coin:", player["coin"])

def move(direction):
    if direction == 'w' and player['x'] > 0: 
        player['x'] -= 1
    elif direction == 'd' and player['y'] < map_size - 1:
        player['y'] += 1
    elif direction == 'a' and player['y'] > 0:
        player['y'] -= 1 
    elif direction == 's' and player['x'] < map_size - 1:
        player['x'] += 1 
    else:
        print("You cannot move that way!")

def main():  
    draw_ui(0,0)
    direction = input("Your next move (w/a/s/d/q)")       
    while direction != 'q': 
 #TODO: call function move() and send the parameter direction
        move(direction)
 #TODO: if player is at the gate 'M':
        if player['x'] == (map_size-1) and player['y'] == (map_size-1):
            print("Congratulations! You reach the gate for next level.")
 #TODO: break the while loop, main() terminates
            break
 #TODO: call function check_event
        check_event()
 #TODO: call function draw_ui() to draw a new map, remember to send the latest coordination of the player
        draw_ui(player['x'], player['y'])
 #TODO: ask for next move (same with 2nd line in this function)
        direction = input("Your next move (w/a/s/d/q)")

if __name__ == '__main__':
    main ()