# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:35:18 2023

@author: hp
"""

# Exercise 3: Stripping Names
# Tidy up the code to make it easier to understand

# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

# Print the name once, so the whitespace around the name is displayed.

# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
n="\tJoaquin\t"
print(n)
print("\n", n.lstrip())#"strip" is to be used to give spaces and "l" and "r" is to designate them to left and right.
print("\n", n.rstrip())
print("\n", n.strip())
