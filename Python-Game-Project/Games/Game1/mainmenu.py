print("Enter 1 if you want to play Snakes and Ladder \n"
      "Enter 2 if you want to play Game 2 \n"
      "Enter 3 if you want to play Game 3 \n")

game_sel = int(input("Select the game you want to play "))

if game_sel == 1:
      exec(open('Game1.py').read())
elif game_sel == 2:
      exec(open('Game2.py').read())
elif game_sel == 3:
      exec(open('Game3.py').read())
else:
      print("Invalid Selection")
