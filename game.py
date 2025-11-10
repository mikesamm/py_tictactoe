game_grid = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def game_loop():
  # print game_grid
  # check win or draw condition to end game loop
  # ask for player input
  # player inputs number for open square
  # edit game grid /end of loop

def print_grid():
  # iterate through game_grid to print latest game grid
  for row in game_grid:
    for square in row:
      print(square, end=',')
    print()

print_grid()
# upon win or draw, display message