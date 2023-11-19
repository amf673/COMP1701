""" 
ask user to enter a number between 1 and 100
set result = ""

while number > 0
    if number is odd
        set bit = 1
    else
        set bit = 0
    write bit to result on the left hand side
    set number = number / 2, rounded down to whole number

display result

"""

def binary(number:int)-> str:
    bin_str = ""

    return bin_str

def main():
    number = int(input("Enter a number to convert to binary: "))
    print( binary(number))
    
main()