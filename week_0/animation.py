import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
ROAD_COLOR = u"\u001B[70;1"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
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

# ship function, iterface into this file
def ship():
  # loop control variables
  start = 0  # start at zero
  distance = 30  # how many times to repeat
  step = 2  # count by 2

  # loop purpose is to animate ship sailing
  for position in range(start, distance, step):
      ship_print(position)  # call to function with parameter
      time.sleep(.1)