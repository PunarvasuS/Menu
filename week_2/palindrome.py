import re

index = []

class Palindrome:
  def __call__(self, n):
    str(n)
    for i in range(0, int(len(n)/2)):
      if n[i] != n[len(n)-i-1]:
        index.append(i)
        return False
    new_n = (re.sub('[^a-zA-Z0-9]', '', n)).lower()
    if new_n == new_n[::-1]:
      index.clear()
      return True

def tester():
  pal_of = Palindrome()
  str_input = str(input("Enter a string or number: "))
  func = pal_of(str_input)
  if func:
    print(str_input + " is a palindrome.")
  elif func == False:
    print(str_input + " is not a palindrome.")
    print("It went wrong at index/indices " + str(index))
  else:
    print("Oh no! Something went wrong!")
  index.clear()