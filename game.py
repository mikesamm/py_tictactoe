# game_grid = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def print_grid():
#   # iterate through game_grid to print latest game grid
#   for row in game_grid:
#     for square in row:
#       print(square, end=',')
#     print()

def game_loop():
  game_grid = [ ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

  test_loops = 0
  current_player = 'X'

  while test_loops <= 5:
    # set current player
    # print game_grid
    # print_grid()
    # iterate through game_grid to print latest game grid
    for row in game_grid:
      for square in row:
        print(square, end=',')
      print()
    # check win or draw condition to end game loop
    # ask for player input
    # print(f"Player {current_player}, what's your move?")
    # player inputs number for open square
    player_input = input(f"Player {current_player}, what's your move?: ")
    # iterate through game_grid for matching number
    for i in range(len(game_grid)):
      for j in range(len(game_grid[i])):
        if game_grid[i][j] == player_input:
          # place current_player mark on square
          game_grid[i][j] = f'{current_player}'
    print(f"Player {current_player} moved here: " + player_input + '\n')
    # change current_player
    if current_player == 'X':
      current_player = 'O'
    else:
      current_player = 'X'
    test_loops += 1

game_loop()
# upon win or draw, display message