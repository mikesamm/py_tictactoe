game_grid = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9']
]

# player move storage lists
x_squares = []
o_squares = []

# set first current player
current_player = 'X'

is_game_ended = False

# def print_grid():
#   # iterate through game_grid to print latest game grid
#   for row in game_grid:
#     for square in row:
#       print(square, end=',')
#     print()

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

def is_win():
  # win: vertical, horizontal, or diagonal line is complete
  # define win conditions
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
  # check storage lists for winning combination
  # does x_squares contain all 3 numbers in one of the winning conditions?
  # does o_squares contain all 3 numbers in one of the winning conditions?

def is_draw():
  # draw: no available squares left
  occupied_squares = 0
  for i in range(len(game_grid)):
    for j in range(len(game_grid[i])):
      if game_grid[i][j] == 'X' or game_grid[i][j] == 'O':
        occupied_squares += 1
  if occupied_squares == 9:
    print("Grab a sketch pad, because it's a draw...")
    globals()["is_game_ended"] = True
    exit()

def game_loop():

  while globals()["is_game_ended"] == False:
    # print game_grid
    # print_grid()
    # iterate through game_grid to print latest game grid
    for row in game_grid:
      for square in row:
        print(square, end=',')
      print()

    is_win()
    is_draw()

    get_player_input()
    print('\n')

    # update player turn
    if globals()["current_player"] == 'X':
      globals()["current_player"] = 'O'
    else:
      globals()["current_player"] = 'X'

game_loop()