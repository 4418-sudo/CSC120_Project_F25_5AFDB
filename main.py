import random 

game_name = ("Totally,Real")

name = "Tester"

player = {
    "name": "Tester",
  "health": 100,
  "coin": 0, 
  "x": 0,
  "y": 0
}
def check_event():
    events = ["Find a coin", "Meet a monster", "do nothing"]
    event = random.choice(events) 
    if event == "Find a coin": 
        player['coin'] += 1 
    elif event == 'Meet a monster':
        player["health"] -= 10

map_size = 9
bar_width = map_size*2-1
thick_bar = "="*bar_width
thin_bar = '-'*bar_width
def draw_ui(x, y):
    print(thick_bar)
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end = " ") # two spaces
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end = " ")
            else:
                print(".", end = " ")
        print()
    print(thick_bar)
    print("Health:", player["health"])   
    print(thin_bar)
    print("Coin:", player["coin"])
    print(thick_bar)

def move(direction):
    if direction == 'w' and player['y'] > 0: 
        player['y'] -= 1
    elif direction == 'd' and player['x'] < map_size - 1:
        player['x'] += 1
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] +=1
    elif direction == 'a' and player['x'] > 0:
        player['x'] -=1
    else:
        print("You cannot move that way!")

def main():
    draw_ui(0,0)
    direction = input("Your next move (w/a/s/d/q)")
    while direction != 'q':
#TODO: call function move() and send the parameter direction
        move(direction)
 #TODO: if player is at the gate 'M':
        if player['y'] == map_size -1 and player['x'] == map_size -1: 
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
    main()
