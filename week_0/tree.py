import math

star_color = u"\u001b[37m"
leaves_color = u"\u001b[32m"
trunk_color = u"\u001b[33m"
menu_color = u"\u001b[37m"

try:
  layers = int(input("How many layers of the pyramid (enter an integer): "))
except:
    print("That\'s not an integer! Please run again.")
    exit()
star = "* "
x = 1
spaceNum = layers

print("Here's your tree:")

while x <= layers:
  if x==1:
    print(star_color)
  else:
    print(leaves_color)
  print((spaceNum * " ") + star)
  star += "* "
  spaceNum -= 1
  x += 1
print(trunk_color)
print(" " * math.floor(layers/1.11) + "***")
print(" " * math.floor(layers/1.11) + "***")

print(menu_color)