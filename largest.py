#
#
# COMP 1701 Fall 2023 Lab 5
#
# 

PROMPT = "Enter a numnber, <CR> to quit: "

response = input( PROMPT)
largest = 0 

while response != "": 
    number = int(response)
    response = input( PROMPT)
    

print("The largest number is: {largest}")