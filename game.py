import random

class Player:
    def __init__(self, name = "Jorden"):
        # TODO: initialize instance attributes using keys and values of dictionary `player`
        # For example, dict `player` has entry x:0, initialize attribute as `self.x = 0`
        initial_state = {'x': 0, 'y': 0, 'coin': 0}
        self.x = initial_state['x']
        self.y = initial_state['y']
        self.coin = initial_state['coin']
        self.name = name
        self.health = 100
  
    def move(self, direction, map_size):
        # TODO: modify the code of function move()
        # hint: only `player[x]` and `player[y]` needs to be modified
        # we don't have dict anymore, we use class attributes to store the values
        # No need to modify the logic, just attributes
        new_x = self.x
        new_y = self.y

        if direction == 'w': 
            new_x = self.x - 1
        elif direction == 's':
            new_x = self.x + 1
        elif direction == 'a':
            new_y = self.y - 1
        elif direction == 'd':
            new_y = self.y + 1
        if 0 <= new_x < map_size and 0 <= new_y < map_size:
            self.x = new_x
            self.y = new_y
        else: 
            print("You cannot move that way!")

class GameMap:
    def __init__(self, size = 9):
        # TODO: initialize an instance attribute `size` with value 9
        self.size = size
        self.coin_x = random.randrange(size)
        self.coin_y = random.randrange(size)
        self.monster_x = random.randrange(size)
        self.monster_y = random.randrange(size)
    def draw(self, player):
        # TODO: move the code of function `draw_ui(x, y)` here and modify the code
        # `draw_ui(x, y)` accepts two arguments, x and y, this instance method
        # only accept one argument `player` because we can use `player.x` to get
        # the value of x, and it is similar for `player.y`
        print('-' * (self.size * 2 + 3))

        for x in range(self.size):
            row = "| "
            for y in range(self.size):
                if x == player.x and y == player.y:
                    row += "C "
                elif x == self.coin_x and y == self.coin_y:
                    row += "VC "
                elif x == self.monster_x and y == self.monster_y:
                    row += "M "
                else:
                    row += ". "
            print(row + "| ")
        print("Health:", player.health)

class Game:
    def __init__(self):
        # TODO: initialize some instance attributes include: game_name, name, and events
        self.game_name = "Simple Grid Adventure "
        self.name = ""
        self.events = {'coin': 1}
        self.player = Player() # initialize a class as the attribute
        self.map = GameMap()
        self.map_size = self.map.size

    def check_event(self):
        # TODO: reformat the function `check_event()`
        # hint: `player["coin"]` can be get using `self.player.coin`
        if self.player.x == self.map.coin_x and self.player.y == self.map.coin_y:
            if self.events['coin'] > 0:
                print(f'You found {self.events['coin']} coins!')
            self.player.coin += self.events['coin']
            self.events['coin'] = 0
        if self.player.x == self.map.monster_x and self.player.y == self.map.monster_y:
            print(f'You have been attacked by the monster!')
            self.player.health -= 10 
        else:
            print("It's an empty spot now")

    def play(self):
        # TODO: put the code of function `main()` here
        # some function calling and dictionary operations must be modified
        print(f'--- Welcome to {self.game_name} ---')
        running = True
        while running:
            self.map.draw(self.player)
            move_input = input("Move (w/a/s/d) or q to quit: ").lower()
            direction = -1
            if move_input == "w":
                direction = 0
            if move_input == "a":
                direction = 2
            if move_input == "s":
                direction = 1
            if move_input == 'd':
                direction = 3
            if move_input == 'q':
                running = False
            if direction is not -1:
                self.player.move(move_input, self.map.size)
            else:
                print("Invalid input. Use w, a, s, or d.")
            if self.player.x == self.map.size -1 and self.player.y == self.map.size -1: 
                running = False  
            self.check_event()
        print(f'--- Game Over! Final coins: {self.player.coin} ---')

if __name__ == "__main__":
    Game().play()
