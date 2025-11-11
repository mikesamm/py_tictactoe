game_grid = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9']
]

# player move storage lists
x_squares = []
o_squares = []

current_player = 'X'
is_game_ended = False

def print_grid():
  for row in game_grid:
    for square in row:
      print(square, end=',')
    print()

# get and check player input
def get_player_input():
  match = False

  while match == False:
    player_input = input(f"Player {current_player}, what's your move?: ")

    # iterate through game_grid for matching number
    for i in range(len(game_grid)):
      for j in range(len(game_grid[i])):
        if game_grid[i][j] == player_input:
          match = True
          # place current_player mark on square
          game_grid[i][j] = f'{current_player}'
          # add player choice in respective storage list
          if globals()["current_player"] == 'X':
            globals()["x_squares"].append(player_input)
          else:
            globals()["o_squares"].append(player_input)

    if match == False:
      print("Please pick a valid square.")

  # update player turn
  if globals()["current_player"] == 'X':
    globals()["current_player"] = 'O'
  else:
    globals()["current_player"] = 'X'

def is_win():
  win_conditions = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']
  ]

  # check and compare intersections of storage list and win conditions
  for win_condition in win_conditions:
    x_intsct = set(globals()["x_squares"]).intersection(win_condition)
    list_x_intsct = list(x_intsct)
    list_x_intsct.sort()
    if list_x_intsct == win_condition:
      print("\nX wins!\n")
      exit()
  for win_condition in win_conditions:
    o_intsct = set(globals()["o_squares"]).intersection(win_condition)
    list_o_intsct = list(o_intsct)
    list_o_intsct.sort()
    if list_o_intsct == win_condition:
      print("\nO wins!\n")
      exit()

def is_draw():
  occupied_squares = 0

  # count occupied squares
  for i in range(len(game_grid)):
    for j in range(len(game_grid[i])):
      if game_grid[i][j] == 'X' or game_grid[i][j] == 'O':
        occupied_squares += 1
  if occupied_squares == 9:
    print("Grab a sketch pad, because it's a draw...")
    exit()

def game_loop():

  while is_game_ended == False:
    print_grid()

    is_win()
    is_draw()

    get_player_input()
    print('\n')

game_loop()