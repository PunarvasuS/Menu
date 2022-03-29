# Factorial of a number using recursion
def recur_factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    num = n * recur_factorial(n-1)
    return num

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def factorial():
  num = int(input("Enter a number for factorial: "))
  # check if the number is negative
  if num < 0:
      print("Sorry, factorial does not exist for negative numbers.")
  else:
      print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

def recur_fibonacci(n):  
  if n < 0:
    print("Incorrect input")
  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:  
    return(recur_fibonacci(n-1) + recur_fibonacci(n-2))  

def output_fibonacci():
  # take input from the user  
  nterms = int(input("How many terms would you like? "))  
  # check if the number of terms is valid  
  if nterms <= 0:  
     print("The Fibonacci sequence does not exist for negative numbers.")  
  else:  
     print("Your sequence:")
     for i in range(nterms):
         print(recur_fibonacci(i), end=" ")
  print()

'''
def find_factors():
  list = []
  num_input = int(input("What number what you like to find all factors of? ")
  for x in range(1, x + 1):
    if num_input % x == 0:
      list.append(x)
'''