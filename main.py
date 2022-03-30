
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from tri2 import swap
from week_0 import animation
from week_1 import InfoDb
from week_2 import factorial, fibfac, palindrome, combo


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
  print()
  title = "Function Menu" + banner
  menu_list = main_menu.copy()
  buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def math_func():
  title = "Input Sub Menu" + banner
  buildMenu(title, math_list)

def patterns_func():
  title = "Patterns Sub Menu" + banner
  buildMenu(title, patterns_list)

def misc_func():
  title = "Misc Sub Menu" + banner
  buildMenu(title, misc_list)

# menu builds:
  
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
  ["Patterns", patterns_func],
  ["Math", math_func],
  ["Misc", misc_func]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu

math_list = [
  ["Swap", swap.swapTester],
  ["Factorial IMP", fibfac.factorial],
  ["Fibonacci", fibfac.output_fibonacci],
  ["Factorial OOP", factorial.tester],
  ["Palindrome", palindrome.tester],
  ["Combinations OOP", combo.comb_test_oop],
  ["Combinations IMP", combo.comb_test_imp],
# ["Find Factors", fibfac.find_factors]
]

patterns_list = [
  ["Car Animation", animation.ship],
  ["Numpad", "tri2/matrix.py"],
  ["Tree Printer", "week_0/tree.py"],
]

misc_list = [
  ["Stats of List (CreateTask)", "tri2/createtask.py"],
  ["InfoDb Loops", InfoDb.InfoDb_loops]
]

# def buildMenu

def buildMenu(banner, options):
  print()
  # header for menu
  print(banner)
  # build a dictionary from options
  prompts = {0: ["Exit", None]}
  for op in options:
      index = len(prompts)
      prompts[index] = op

  # print menu or dictionary
  for key, value in prompts.items():
      print(key, '->', value[0])

  # get user choice
  choice = input("Type your choice> ")

  # validate choice and run
  # execute selection
  # convert to number
  try:
      choice = int(choice)
      if choice == 0:
          # stop
          return
      try:
          # try as function
          action = prompts.get(choice)[1]
          action()
      except TypeError:
          try:  # try as playground style
              exec(open(action).read())
          except FileNotFoundError:
              print(f"File not found!: {action}")
          # end function try
      # end prompts try
  except ValueError:
      # not a number error
      print(f"Not a number: {choice}")
  except UnboundLocalError:
      # traps all other errors
      print(f"Invalid choice: {choice}")
  # end validation try

  buildMenu(banner, options)  # recursion, start menu over again

if __name__ == "__main__":
  menu()