# def swap(num1, num2):  
#   temp = num1
#   num1 = num2
#   num2 = temp
#   return num1, num2

# def ifLowSwap(num1, num2):
#   if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp
#   return num1, num2
  
# print(1, 2)
# thing1, thing2 = swap(1, 2)
# print(thing1, thing2)
# print()

# print(2, 1)
# thing1,thing2 = ifLowSwap(1,2)
# print(thing1,thing2)
# print()

# print(1, 2)
# thing1, thing2 = ifLowSwap(1, 2)
# print(thing1, thing2)
# print()

def swapTester():
    int1 = int(input("Enter a number: "))
    int2 = int(input("Enter a second number: "))

    print("Before: num1 = {0} and num2 = {1}".format(int1, int2))
    temp = int1
    int1 = int2
    int2 = temp
    print("After: num1 = {0} and num2 = {1}".format(int1, int2))