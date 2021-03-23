# Functions' example
# python doesn't allow to overright the function

# Basic function
def say_hi():
    print('Hi')

say_hi() #Call function

# Python function parameters and arguments
def say_hi_with_name(name):
    print(f'Hi {name}')

say_hi_with_name('John')

# Variable scope
def say_hi_variable():
    print(f'Hi {name}')
    answer = "Hi" # answer is not known outside of the function

name = "John" # name is a top-level variable that is visible everywhere
say_hi_variable()
# print(answer) #NameError: name 'answer' is not defined

# Python function with multiple arguments
def welcome(name, location):
    print("Hi", name, "welcome to", location)

welcome('erik', 'this tutorial')

# Default values and named parameters
def welcome(name='learner', location='this tutorial'): # function has default arguments' values
    print("Hi", name, "welcome to", location)

welcome() # use default arguments' values
welcome(name='John') # use assigned name's value and default location's value
welcome(location='this epic tutorial') # use default name's value and assigned location's value
welcome(name='John', location='this epic tutorial') # use assigned name's value and assigned location's value

welcome('Erik', 'your home') # we can use not called parameters. In this case parameter will be called in turn
