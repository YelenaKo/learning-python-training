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
  - while 
  ```  
  while ( x<5 ):  # 0, 1, 2, 3, 4
    print (x)
    x = x+1
  ```  
  - for
  ```
    for x in range(5, 10):  # 5, 6, 7, 8, 9
      print(x)
  ```
  - over a collection
  ```
    days=["Mon","Tue","Wed"]  
    for d in days :
      print (d)
  ```
  - break and continue statements
  ```
    for x in range (5, 10):  
      if ( x==7): break   # 5, 6
      print (x)
  ```
  ```
    for x in range (5, 10):  
      if ( x % 2 == 0 ): continue #5, 7, 9
      print (x)
  ```
  - enumerate() function to get index
  ```
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]  
    for i, d in enumerate(days) :
      print (i, d) # 0 Mon, 1 Tue, 2 Wed...
  ```


## Ch3


## Ch4


## Ch5


*credentials: https://www.linkedin.com/learning/learning-python-2/
