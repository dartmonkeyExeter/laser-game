#Laser Maze by 101Comoputing.net - www.101computing.net/laser-maze/
import random, time, os

points = 100
          
#Initialise maze, bombs, laser source and exit gate
maze = [[" -","--","--","--","--","--","--","--","--","--","--","- "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" -","--","--","--","--","--","--","--","--","--","--","- "]
       ]

def drawMaze():
  print("")
  print("    1 2 3 4 5 6 7 8 9 10")
  for i in range(0,12):
    line = ""
    for j in range(0,12):
       line = line + maze[i][j]
    if i>0 and i<10:
      print(" " + str(i) + line)
    elif i==0 or i==11:
      print("  " + line)
    elif i==10:
      print("10" + line)

def shoot(points):
  global direction
  state="shooting"
  row = source[0]
  col = source[1]
  
  while state=="shooting":
      os.system("cls")
      if direction=="right":
        col = col + 1
      ##Add code here to allow laser to move in all 4 directions  
      elif direction=="left":
        col = col - 1
      elif direction=="up":
        row = row + 1
      elif direction=="down":
        row = row - 1
        
      if maze[row][col]=="  ":
        print("")
        maze[row][col]="++"
      elif maze[row][col]=="[]":
        print("Exit Gate Reached! Level Cleared!")
        points += 50
        state="win"
      elif maze[row][col]=="<>":
        print("Laser beam hits a bomb! Game Over!")
        state="lost"
      elif maze[row][col]==" |" or maze[row][col]=="| " or maze[row][col]=="--":
        print("Laser beam hits a wall! Game Over!")
        state="lost"
      elif maze[row][col]==">>":
        print("Laser beam hits it source! Game Over!")
        state="lost"
      elif maze[row][col]=="\\\\": # clockwise
        if direction=="right":
          direction="up"
        elif direction=="left":
          direction="down"
        elif direction=="up":
          direction="right"
        elif direction=="down":
          direction="left"
      elif maze[row][col]=="//": # anticlockwise
        if direction=="right":
          direction="down"
        elif direction=="left":
          direction="up"
        elif direction=="up":
          direction="left"
        elif direction=="down":
          direction="right"
  
      ## Add code here to redirect the laser in a different direction (top, right, bottom, left)  when a reflector wall // or \\ is hit.  

      drawMaze()
      time.sleep(0.2)
  return points, state




##Collect inputs (row and column numbers) to find out where do the user wants to point reflection walls: // and \\


def place_reflectors():
  while True:
    reflector_type = input('reflector type ( // or \\\\ ): ')
    if reflector_type != "//" and reflector_type != '\\\\':
      print("invalid reflector type, try again")
      continue
    break

  while True:
    while True:
        refl_row = input('row: ')
        try:
          refl_row = int(refl_row)
          if refl_row > 10 or refl_row < 1:
            print("please enter a valid number")
            continue
          break
        except ValueError:
          print("please enter a number")

    while True:
        refl_col = input('column: ')
        try:
          refl_col = int(refl_col)
          if refl_col > 10 or refl_col < 1:
            print("please enter a valid number")
            continue
          break
        except ValueError:
          print("please enter a number")
    
    if maze[refl_row][refl_col]=="  ":
      maze[refl_row][refl_col]=reflector_type
      drawMaze()
      break
    else:
      print("sorry, something already there, try again.")
      continue
      

##Add reflection walls to the maze as instructed by the user
numberOfBombs = 3
points = 100
while True:
  maze = [[" -","--","--","--","--","--","--","--","--","--","--","- "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" -","--","--","--","--","--","--","--","--","--","--","- "]
       ]
  source = (random.randint(1,10),0)
  direction = "right"
  maze[source[0]][source[1]] = ">>"

  exit = (random.randint(1,10),11)
  maze[exit[0]][exit[1]] = "[]"

  def placeBombs(numberOfBombs):
    i = 1
    while i <= numberOfBombs:
      row = random.randint(1,10)
      col = random.randint(1,10)
      if maze[row][col+1] == "[]" or maze[row][col-1] == ">>":
        continue
      maze[row][col] = "<>"
      i += 1

  placeBombs(3)    
  drawMaze()    
  while True:
    y_or_n = input(f"would you like to buy a reflector for 20 points? you currently have {points} points. (y/n)").lower().strip()
    if y_or_n == "y" and points >= 20:
      points -= 20
      place_reflectors()
    else:
      break


  points, state = shoot(points)
  if state == "win":
    print("you won! moving on to next level.")
  else:
    print("game over")
    break
  numberOfBombs += 1
