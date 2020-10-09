# Learning Python

_[ # variables ](#variables)_

_[ # functions ](#functions)_

_[ # conditional statements ](#conditional-statements)_

_[ # loops ](#loops)_

## Ch2

- ### variables: 
  - declaring and re-declaring
  - local and global variables in functions  
  `f=0`, `f="abc"`, `global f`

- ### functions:
  - basic function `def func():`
  - with arguments `def func(arg1, arg2):`
  - with default value for an argument `def func(num, x=1):`
  - with variable number of arguments `def func(*args):`

  ```
  def power(num, x=1):
      result = 1
      for i in range(x):
         result = result * num
      return result
    
  print (power(2))            # 2
  print (power(2, 3))         # 8
  print (power(x=3, num=2))   # 8    
  ```   
- ### conditional statements:  
  - conditional statements  "a **if** C **else** b" 
  ```
  st = "x is less than y" if ( x < y) else "x is greater than or the same as y"
  ```
  - conditional flow uses if, elif, else  
  ```
  def main():
    x, y = 10, 100

    if (x < y):
      st = "x is less than y"
    elif( x == y):
      st = "x is the same is y"
    else:
      st = "x is greater than y"  

   print (st) 
  ```
- ### loops:


## Ch3


## Ch4


## Ch5


*credentials: https://www.linkedin.com/learning/learning-python-2/
