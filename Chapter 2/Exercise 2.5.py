# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:44:29 2023

@author: hp
"""

# Exercise 5: USB Shopper ☑️
# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

# You will to use the arithmetic operators to complete this exercise.
USBsticks= 50//6
price= USBsticks * 6
change= 50 - price
print("She can buy",USBsticks,"USB sticks for the price of",price,"pounds. She will have",change,"pounds left")