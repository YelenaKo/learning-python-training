# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)
    # the result is:
        # 0

# # re-declaring the variable works
f="abc"
print(f)
    # the result is:
        # 0
        # abc

# # ERROR: variables of different types cannot be combined
# print("this is a string" + 123)

print("this is a string " + str(123))
    # the result is:
        # 0
        # abc
        # this is a string 123

# Global vs. local variables in functions
#local
def someFunction():
    f="def"
    print(f)

someFunction() 
print(f)         
    # the result is:
        # 0
        # abc
        # this is a string 123
        # def      <---
        # abc      <---

# global
def someFunctionG():
    global f
    f="def"
    print(f)

someFunctionG() 
print(f)        
    # the result is:
        # 0
        # abc
        # this is a string 123  
        # def  
        # abc 
        # def      <---
        # def      <---

del f
print(f) 
    # the result is:
        # 0
        # abc
        # this is a string 123  
        # def  
        # abc 
        # def 
        # def
        # NameError: name 'f' is not defined  <---

