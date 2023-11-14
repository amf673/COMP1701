# Otto does geometry
# 
# A. Fedoruk & COMP 1701 001
# 
# Nov 6, 2023

import turtle as t
import random

import ordinal as o

# Constants for directions in the turtle graphic cartesion plane. 

EAST = 0
WEST = 180
NORTH = 90
SOUTH = 270

# Canvas size for generating coordinates 
CANVAS = 400

# Colours
RED = "red"
GREEN = "forestgreen"
BLUE = "blue"
YELLOW = "yellow"
ORANGE = "DarkOrange"
PURPLE = "purple3"
BLACK = "black"
WHITE = "white"

def polygon(tur:t.Turtle, x:int, y:int, len_side: int, sides: int, colour: str, fill:bool) -> None:
    """Draw a sides sided polygon at position (x,y) with len_side sides, in colour colour"""
    angle = int(360/sides)
    tur.penup()
    tur.goto(x,y)
    if fill:
        tur.fillcolor(colour)
        tur.begin_fill()
    tur.pencolor(colour)
    tur.pendown()
    for _ in range(sides):
        tur.forward(len_side)
        tur.left(angle)
    if fill: 
        tur.end_fill()
    tur.penup()

def circ(tur:t.Turtle, radius:int, x:int, y:int, colour:str, fill:bool)->None:
    """Draw a circle with turtle tur with centre at x,y, radius radius in colour colour"""
    
    if fill:
        tur.fillcolor(colour)
        tur.begin_fill()
    tur.penup()
    tur.goto(x, y - radius)
    tur.pencolor(colour)
    tur.pendown()
    tur.circle(radius)
    if fill:
        tur.end_fill()
    tur.penup()

def triangle(tur:t.Turtle, len_side:int, x:int, y:int, colour:str)->None:
    """ Draw a non-filled triangle"""
    polygon(tur, x, y, len_side, 3, colour, False)

def triangle_filled(tur:t.Turtle, len_side:int, x:int, y:int, colour:str)->None:
    """ Draw a filled triangle"""
    polygon(tur, x, y, len_side, 3, colour, True)

def square(tur:t.Turtle, len_side:int, x:int, y:int, colour:str, fill:bool)->None:
    """Draw a square with turtle tur with bottom left corner at x,y, sides of length len_side in colour colour"""
    polygon(tur, x, y, len_side, 4, colour, fill)

def pentagon(tur:t.Turtle, len_side:int, x:int, y:int, colour:str)->None:
    polygon(tur, x, y, len_side, 5, colour,False)

def get_coord()-> int:
    """ Return a random coord """
    return random.randint(-CANVAS, CANVAS)

def get_rand_colour()->str:
    """Return a random colour string from the 7 we have defined"""
    n = random.randint(0,6)
    if n == 0:
        c = RED
    elif n == 1:
        c = BLUE
    elif n == 2:
        c = GREEN
    elif n == 3:
        c = YELLOW
    elif n == 4:
        c = ORANGE
    elif n == 5: 
        c = PURPLE
    else:
        c = BLACK
    return c

def counted_loop()->None:
    
    PROMPT = "How many shapes would you like? "
    otto = t.Turtle()
    otto.speed('fast')
    otto.shape('turtle')
    otto.pensize(5)

    circles = int(input(PROMPT))

    # Since we know how many times to loop we can use a counted Loop. 
    #   i is the loop control variable
    #   0 to < n will give n iterations

    # i = 0
    filled = False 
    while circles > 0:
        
        circ(otto, 100, get_coord(), get_coord(), get_rand_colour(), True)
        square(otto, 50, get_coord(), get_coord(), get_rand_colour(), filled)
        filled = not filled
        # Now we need to update our loop control variable
        circles = circles - 1
        print( f"Printed the {o.ordinal(circles)} circle")
        
    t.mainloop()

def sentinel_loop() -> None:

    PROMPT = "What colour circle? (STOP to end) "   

    otto = t.Turtle()
    otto.speed('fast')
    otto.shape('turtle')
    otto.pensize(5)

    # We want to draw coloured circles until we enter STOP. 
    # Since we don't know how many circles before hand we 
    # can't use a counted loop, so we use a sentinel loop. 

    count = 0
    colour = input(PROMPT)
    while colour != "STOP":
        circ(otto, 100, get_coord(), get_coord(), colour, True)
        count = count + 1
        colour = input(PROMPT)

    print( f"We drew {count} shapes.")
    t.mainloop()

def concentric_circles()->None:
    otto = t.Turtle()
    otto.speed('fast')
    otto.shape('turtle')
    otto.pensize(5)

    radius = 300
    while radius > 0:
        circ(otto, radius, 0, 0, get_rand_colour(), False)
        radius = radius // 2
        print(radius)


    t.mainloop()

def sandbox()->None:
    otto = t.Turtle()
    otto.speed('fast')
    otto.shape('turtle')
    otto.pensize(5)

    triangle(otto, 75, -100, 100, RED)
    square(otto, 75, -100, -100, GREEN, False)
    pentagon(otto, 75, 100, 100, BLUE)
    circ(otto, 75, 100, -100, PURPLE, False)

    polygon(otto, -300, 0, 75, 12, ORANGE, True)
    polygon(otto, -300, -300, 5, 100, PURPLE, True)
    
    t.mainloop()

def func()-> float: 
    
    i = 0
    sum = 0 
    more = input("more numbers? y/n")
    while (more == "y"): 
        num = int(input("Enter a number: "))
        sum = sum + num 
        i = i + 1
        more = input("more numbers? y/n")
        
    print(sum, i, sum/i)


def main():
    # counted_loop()
    # sentinel_loop()
    concentric_circles()
    # sandbox()
    # func() 

main()