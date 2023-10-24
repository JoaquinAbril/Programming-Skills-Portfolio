# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:01:14 2023

@author: hp
"""

# Exercise 5: Favorite Fruit 
# •Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# •Make a list of your three favorite fruits and call it favorite_fruits.
# •Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement,such as You really like bananas!
favorite_fruits=["mango","durian","banana"]
if "mango" in favorite_fruits:
    print("You really like mangoes!")
if "durian" in favorite_fruits:
    print("you really like durians!")
if "banana" in favorite_fruits:
    print("you really like bananas!")

elif "chico" in favorite_fruits:
    print("you really like chicos!")
else:
    print("you really like strawberries!")

