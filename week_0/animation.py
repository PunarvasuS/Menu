import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
one_color = u"\u001b[37m"
second_color = u"\u001b[31m"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# print car with colors and leading spaces
def car_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    if position%4==0:
      print(one_color)
    else:
      print(second_color)
    sp = " " * position
    print()
    print(sp + " ____________________")
    print(sp + " | |         0     \ \ ")
    print(sp + " | |        /|\     \ \______")
    print(sp + " | |        / \           | | ")
    print(sp + " | |______________________/ / ")
    print(sp + "   ___                  ___ ")
    print(sp + "  /   \                /   \   ")
    print(sp + " |  O  |              |  O  |  ")
    print(sp + "  \___/                \___/   ")
    print(RESET_COLOR)

# car function, iterface into this file
def car():
  # loop control variables
  start = 0  # start at zero
  distance = 30  # how many times to repeat
  step = 2  # count by 2

  # loop purpose is to animate car driving
  for position in range(start, distance, step):
      car_print(position)  # call to function with parameter
      time.sleep(.1)