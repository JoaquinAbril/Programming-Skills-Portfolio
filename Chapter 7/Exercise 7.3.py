# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:26:53 2023

@author: hp
"""

# Exercise 3: T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(shirt_size, text_of_a_message):
    print("I'm going to make a " + (shirt_size) + " t-shirt.")
    print("It will say, "+ (text_of_a_message) +"!")
    
make_shirt('small', 'ang pogi ko')
print()
make_shirt(text_of_a_message="wow", shirt_size='large')