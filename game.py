game_grid = [ ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


# def print_grid():
#   # iterate through game_grid to print latest game grid
#   for row in game_grid:
#     for square in row:
#       print(square, end=',')
#     print()

# set first current player
current_player = 'X'
is_game_ended = False

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
    if match == False:
      print("Please pick a valid square.")

def is_win_draw():
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
  # win: vertical, horizontal, or diagonal line is complete

def game_loop():
  # test_loops = 0

  while globals()["is_game_ended"] == False:
    # print game_grid
    # print_grid()
    # iterate through game_grid to print latest game grid
    for row in game_grid:
      for square in row:
        print(square, end=',')
      print()
    # TODO: check win or draw condition to end game loop
    is_win_draw()

    get_player_input()
    print('\n')

    # update player turn
    if globals()["current_player"] == 'X':
      globals()["current_player"] = 'O'
    else:
      globals()["current_player"] = 'X'
    # test_loops += 1

game_loop()
# upon win or draw, display message