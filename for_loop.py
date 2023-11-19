# For loop demo 
# COMP 1701 Fall 2023

# Counted Loop General Form 

reps = 11

loop_control = 0 
while loop_control < reps:
    print(loop_control)
    loop_control = loop_control + 1

loop_control = reps
while loop_control > 0: 
    print(loop_control)
    loop_control = loop_control - 1



# Explore the range function 

# 
a = range( 0, 5, 1) # return a sequence of numbers from 0 to 4 incrementing by 1
b = range( 1, 10, 2) # return a sequence of numbers from 1 to 10 incrementing by 2. 1,3,5,7,9
c = range(12) # using defaults return a sequence of numbers from 0 to 11. 
d = range(10, 0, -1) 

# Lets look at these ranges

print(a)
print(type(a))

# To really see the range in action, lets use a for loop

print("range a")
for i in a: 
    print(i)

print("range b")
for i in b:
    print(i)

print("range c")
for i in c: 
    print(i)

print("range d")
for i in d: 
    print(i)

