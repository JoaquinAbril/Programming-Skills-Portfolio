# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:28:51 2023

@author: hp
"""

# Exercise 4: Large Shirts
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(shirt_size='large', message_in_the_shirt='I love Python!'):
    print()
    print("I'm going to make a " + (shirt_size) + " t-shirt.")
    print("It will say, " + (message_in_the_shirt))
make_shirt()
make_shirt(shirt_size='medium')
print()
make_shirt('extra extra large', 'Programmers < gamers.')