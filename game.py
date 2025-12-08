 import random Python

 class Player:
 def __init__(self):
 # TODO: initialize instance attributes using keys and values of dictionary `player`
 # For example, dict `player` has entry x:0, initialize attribute as `self.x = 0`

 def move(self, direction, map_size):
 # TODO: modify the code of function move()
 # hint: only `player[x]` and `player[y]` needs to be modified
 # we don't have dict anymore, we use class attributes to store the values
 # No need to modify the logic, just attributes

 class GameMap:
 def __init__(self):
 # TODO: initialize an instance attribute `size` with value 9

 def draw(self, player):
 # TODO: move the code of function `draw_ui(x, y)` here and modify the code
 # `draw_ui(x, y)` accepts two arguments, x and y, this instance method
 # only accept one argument `player` because we can use `player.x` to get
 # the value of x, and it is similar for `player.y`

 class Game:
 def __init__(self):
 # TODO: initialize some instance attributes include: game_name, name, and events
 self.player = Player() # initialize a class as the attribute
 self.map = GameMap()
   
def check_event(self):
# TODO: reformat the function `check_event()`
# hint: `player["coin"]` can be get using `self.player.coin`

 def play(self):
 # TODO: put the code of function `main()` here
 # some function calling and dictionary operations must be modified
  
if __name__ == "__main__":
Game().play(
