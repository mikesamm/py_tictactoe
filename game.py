# game_grid = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def print_grid():
#   # iterate through game_grid to print latest game grid
#   for row in game_grid:
#     for square in row:
#       print(square, end=',')
#     print()


# LEAVING OFF WITH GETTING THE PLAYER INPUT AND CHECKING FOR VALIDITY, NEEDS TO BE LOOP IF NOT VALID

def get_player_input():
    player_input = input(f"Player {current_player}, what's your move?: ")
    # TODO: check player input
    match = False
    # iterate through game_grid for matching number
    for i in range(len(game_grid)):
      for j in range(len(game_grid[i])):
        if game_grid[i][j] == player_input:
          # place current_player mark on square
          match = True
          game_grid[i][j] = f'{current_player}'

def game_loop():
  game_grid = [ ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

  test_loops = 0
  # set first current player
  current_player = 'X'

  while test_loops <= 5:
    # print game_grid
    # print_grid()
    # iterate through game_grid to print latest game grid
    for row in game_grid:
      for square in row:
        print(square, end=',')
      print()
    # TODO: check win or draw condition to end game loop
    # ask for player input
    # player inputs number for open square

    get_player_input()
    # player_input = input(f"Player {current_player}, what's your move?: ")
    # # TODO: check player input
    # match = False
    # # iterate through game_grid for matching number
    # for i in range(len(game_grid)):
    #   for j in range(len(game_grid[i])):
    #     if game_grid[i][j] == player_input:
    #       # place current_player mark on square
    #       match = True
    #       game_grid[i][j] = f'{current_player}'

    print('\n')
    # change current_player
    if current_player == 'X':
      current_player = 'O'
    else:
      current_player = 'X'
    test_loops += 1

game_loop()
# upon win or draw, display message