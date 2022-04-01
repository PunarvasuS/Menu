import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
primary_color = u"\u001b[34m"
secondary_color = u"\u001b[35m"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# print ship with colors and leading spaces
def welcome_print(position):
    print(ANSI_CLEAR_SCREEN)
    print(ANSI_HOME_CURSOR)
    if position%4==0:
      print(primary_color)
    else:
      print(secondary_color)
    shift=position%4
    sp = " " * shift
    print()
    print(sp + " \        / |---- |     |---- |----| |\  /| |----")
    print(sp + "  \  /\  /  |--   |     |     |    | | \/ | |--")
    print(sp + "   \/  \/   |---- |____ |---- |----| |    | |----")
    print(sp + "")
    print(sp + "")
    print(sp + "")
    print(sp + "")
    print(sp + "")
    print(sp + "")
    print(RESET_COLOR)

# ship function, iterface into this file
def welcome_animation():
  # loop control variables
  start = 0  # start at zero
  distance = 30  # how many times to repeat
  step = 2  # count by 2

  # loop purpose is to animate ship sailing
  for position in range(start, distance, step):
      welcome_print(position)  # call to function with parameter
      time.sleep(.1)