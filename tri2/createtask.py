from statistics import *

numList = []

print(
    'Hello user! This program outputs the mean, median, and mode of your inputted list! Try it!'
)

def OR(input, first, second):
    bool = input == first or input == second
    return bool


while True:
    addInput = input('Would you like to add a number to the list? (y/n)')
    if OR(addInput, 'y', 'yes'):
        try:
            itemInput = float(input('What number would you like to add?'))
        except:
            print('Oh no! That wasn\'t an expected answer. Exiting...')
            break
        numList.append(itemInput)
        print('Number inputted.')
    elif OR(addInput, 'n', 'no'):
        print('Ok!')
        break
    else:
        print('Oh no! That wasn\'t an expected answer. Exiting...')
        break

try:
  mean = mean(numList)
  median = median(numList)
  mode = mode(numList)
  min = min(numList)
  max = max(numList)
  print('The list is: ')
  for x in range(len(numList)):
      print(numList[x], end=" ")
  print()
  
  statInput = input('Would you like to see the statistics of the list? (y/n)')
  
  if OR(statInput, 'y', 'yes'):
      print()
      print('The mean is ' + str(mean) + '.')
      print('The median is ' + str(median) + '.')
      print('The mode is ' + str(mode) + '.')
      print('The range is ' + str(min) + ' --> ' + str(max) + '.')
  elif OR(statInput, 'n', 'no'):
      print('Ok! This is the end of the program.')

except:
  print('You didn\'t enter any data. No statistics can be outputted. This is the end of the program.')