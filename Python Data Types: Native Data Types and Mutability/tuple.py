"""
A Python tuple is almost identical to a list:

It can hold multiple values in a single variable
It’s ordered: the order of items is preserved
A tuple can have duplicate values
It’s indexed: you can access items numerically
A tuple can have an arbitrary length

The only differences:

A tuple is immutable; it can not be changed once you defined it.
A tuple is defined using parentheses () instead of square brackets []
"""

my_numbers = (1, 2, 3)
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)

# A tuple can also be created by using the tuple() constructor from that class
# We have to use this method in reason to create tuple always

my_tuple = tuple([10, 3, 5])

# *l1 unpack list 1
l1 = [1, 2, 3]
l2 = [4, 5, 6]
t = (*l1, *l2)

print(t)

# Multiple assignment using a Python tuple
person = ('Erik', 38, True)
name, age, registered = person

# Example
def get_user_by_id(userid):
    # fetch user from database
    # ....
    return name, age
  
name, age = get_user_by_id(4)

# Indexed access
# A tuple can be accessed using index numbers like [0] and [1]:
my_mixed_tuple = ('Hello', 123, True)
my_mixed_tuple[0]
my_mixed_tuple[2]

# Append to a Python Tuple
""" Because a tuple is immutable, you can not apend data to a tuple after it’s created. 
For the same reason, you can’t remove data from a tuple either. You can, of course, create a new tuple from the old 
one, and append the extra item(s) to it this way:
"""
t1 = (1, 2, 3)
t2 = (*t1, 'Extra', 'Items')

# Converting Python tuples
# Convert Tuple to List
t = (1, 2, 3)
list(t)
l = [*t]

# Convert tuple to set
s = set(t)
s = {*t}

# Convert tuple to string
str(t)