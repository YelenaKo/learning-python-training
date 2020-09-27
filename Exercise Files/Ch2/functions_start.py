#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


#function with variable number of arguments
def multi_add(*args): # the * means I can pass in a variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result



func1()         # I am a function
print (func1()) # I am a function
print (func1)   # None

func2(10, 20)          # 10 20
print( func2(10, 20))  # 10 20 
                       # none

print(cube(3))   #27

print (power(2))            # 2
print (power(2, 3))         # 8
print (power(x=3, num=2))   # 8

print(multi_add(4, 5, 10, 4)) # 23