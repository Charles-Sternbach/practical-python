"""
Date: 9-13-26
Author: Charles Sternbach
Purpose:
    Write your first python program. Try to run this program in the terminal.
"""

# hello.py
print('hello world')

### Statements & Comments
# A python program is a sequence of statements
a = 3 + 4
# This is a comment
b = a * 2
print(b)

### Variables
height = 442 # valid
_height = 442 # valid
height2 = 442 # valid
# 2height = 442 # invalid

### Types
# Variables do not need to be declared with the type of the value
# The type is associated with the value on the right hand side, 
#   not the name of the variable
height = 442           # An integer
height = 442.0         # A Floating point
height = 'Really tall' # A string

# Python is dynamically typed.
# The perceived type of a variable might change as the program executes 
#   depending on the current value assigned to it.

### Case Sensitivity
# Python is case sensitive. Upper and lower case letter are considered different letters
# These are all different variables.
name = 'Charles'
Name = 'Sailor Moon'
NAME = 'Rei Hino'

# Language statements are always lower case
# while x < 0: # OK
# WHILE X < 0: # Error

### Looping
# The while statement executes a loop
# The statements indented below the 'while' will execute as long as the 
# expression after the 'while' is 'true'

x = 0
while x < 10:
    print(x)
    x += 1

### Conditionals
# The 'if' statement is used to execute a conditional
if a > b:
    print('Computer says no')
elif a == b: # You can check for multiple conditions by adding extra checks using 'elif'
    print('Computer says yes')
else:
    print('Computer says maybe')

print('Hello', end=' ')
print('My name is', 'Jake')

### User input
# To read a line of user input, use the 'input()' function
# name = input('Enter your name: ')
# print('Your name is', name)

### Pass statement
# The keyword 'pass' is sued to specify an empty code block
if a > b:
    pass
else:
    print('Computer says false')
    
# This is also called a "no-op" statement. It does nothing.
# It serves as a placeholder for statements, possibly to be added later
